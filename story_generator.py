import requests
import json
import os
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for development so the client HTML (on a different port or file://)
# can communicate with the Flask server (on port 5000)
CORS(app)

# --- Configuration (using constants from your original code) ---
# NOTE: In a real application, you must set GEMINI_API_KEY in your environment
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"


# --- Core AI Logic Function ---
def generate_story_logic(genre, paragraphs, keywords):
    """
    Calls the Gemini API to generate a story based on user inputs.
    Includes retry logic for robustness.
    """
    if not API_KEY:
        return "ERROR: Gemini API key not found. Set it as an environment variable 'GEMINI_API_KEY'."

    prompt = (
        f"Write a {genre} story. "
        f"The story must be exactly {paragraphs} paragraphs long. "
        f"Include the following elements: {keywords}. "
        f"Ensure the story flows naturally and concludes well."
    )

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.8}
    }
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            # Console output for server debugging
            print(f"API Attempt {attempt + 1} of {max_retries} for genre: {genre}")
            response = requests.post(
                API_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=30
            )

            # Specific handling for 400 Bad Request
            if response.status_code == 400:
                error_detail = response.json()
                error_message = error_detail.get('error', {}).get('message', 'No specific error message.')
                raise requests.exceptions.HTTPError(f"400 Bad Request: {error_message}", response=response)

            response.raise_for_status()
            result = response.json()

            candidates = result.get('candidates', [])
            if candidates:
                text_part = candidates[0].get('content', {}).get('parts', [{}])[0].get('text')
                return text_part or "Error: No text returned by model."
            return "Error: No candidates returned by API."

        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP Error: {e.response.status_code} - {e.response.text}"
            if attempt < max_retries - 1 and e.response.status_code in [429, 400]:
                wait_time = 2 ** attempt
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                return f"Failed due to HTTP error: {error_msg}"
        except requests.exceptions.RequestException as e:
            return f"Connection error: {e}"

    return "Failed after all retries."


# --- Flask API Endpoint ---

@app.route('/generate_story', methods=['POST'])
def generate_story_endpoint():
    """
    Endpoint that receives user input via POST and returns the generated story.
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON payload"}), 400
        
    genre = data.get('genre', '').strip()
    paragraphs = data.get('paragraphs', 0)
    keywords = data.get('keywords', '').strip()

    # Basic server-side validation
    if not all([genre, keywords]) or not isinstance(paragraphs, int) or paragraphs <= 0:
        return jsonify({"error": "Missing or invalid input parameters (genre, paragraphs, or keywords)."}), 400

    story = generate_story_logic(genre, paragraphs, keywords)
    
    # Return the result as a JSON object
    if story.startswith("ERROR:") or story.startswith("Failed due to HTTP error:"):
        return jsonify({"story": story, "success": False, "error": story}), 500
    else:
        return jsonify({"story": story, "success": True}), 200

if __name__ == '__main__':
    # When running directly: python story_generator.py
    app.run(debug=True)