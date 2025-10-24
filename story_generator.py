import requests
import json
import os
import time

# Load API key securely from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

#QUESTIONS TO USER
def generate_story(genre, paragraphs, keywords):
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
            print(f"Attempt {attempt + 1} of {max_retries}...")
            response = requests.post(
                API_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=30
            )

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
            print(f"HTTP Error: {e}")
            if attempt < max_retries - 1 and e.response.status_code in [429, 400]:
                wait_time = 2 ** attempt
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                return f"Failed due to HTTP error: {e}"
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            return f"Connection error: {e}"

    return "Failed after all retries."

def main():
    print("--- AI Story Generator ---")

    if not API_KEY:
        print("ERROR: Gemini API key not found. Set it as an environment variable 'GEMINI_API_KEY'.")
        return

    genre = input("Enter genre (e.g., Sci-Fi, Horror): ").strip()
    while not genre:
        genre = input("Genre cannot be empty. Try again: ").strip()

    while True:
        try:
            paragraphs = int(input("Enter number of paragraphs: "))
            if paragraphs > 0:
                break
            print("Enter a positive number.")
        except ValueError:
            print("Invalid number. Try again.")

    keywords = input("Enter 3–5 keywords (comma separated): ").strip()
    while not keywords:
        keywords = input("Keywords cannot be empty. Try again: ").strip()

    print("\n--- Generating Story ---\n")
    story = generate_story(genre, paragraphs, keywords)

    print("\n" + "="*50)
    print("GENERATED STORY")
    print("="*50)
    print(story)
    print("="*50)

if __name__ == "__main__":
    main()