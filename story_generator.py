import random

def generate_multi_genre_story_with_templates():
    """
    Prompts the user for characters and a genre, then generates a unique story
    using a genre-specific template, randomized details, and a genre-appropriate twist.
    """
    print("🎬 Welcome to the Template-Driven Story Generator! 🎬")

    # --- 1. Get User Input ---
    
    hero_name = input("Enter a name for the Protagonist: ").strip().title()
    sidekick_name = input("Enter a name for the Partner: ").strip().title()
    
    # Get the genre choice
    valid_genres = ['sci-fi', 'fantasy', 'horror', 'love', 'mystery', 'comedy']
    while True:
        genre_choice = input(f"Choose a genre ({', '.join(g.title() for g in valid_genres)}): ").strip().lower()
        if genre_choice in valid_genres:
            break
        else:
            print(f"Invalid choice. Please enter one of: {', '.join(g.title() for g in valid_genres)}.")

    print(f"\n--- Preparing a tailored {genre_choice.upper()} tale for {hero_name} and {sidekick_name}... ---\n")

    # --- 2. Genre-Specific Randomized Lists ---

    story_elements = {
        'sci-fi': {
            'relaxing': ["having a cup of synth-coffee", "stargazing from the observation deck", "playing zero-g chess", "tuning the ship's quantum radio", "meditating in the anti-gravity chamber"," practicing holo-sculpting"," recalibrating the star maps"],
            'items': ["the unstable neutrino flux capacitor", "the sentient can of space beans", "the zero-gravity hamster wheel","the quantum flux stabilizer","the antimatter-infused rubber duck","the holographic map of the Andromeda galaxy"],
            'settings': ["a rusted-out orbital pizza parlor", "the core of a rogue AI mainframe", "a holographic swamp on Planet Zorp"," a derelict spaceship drifting near a black hole"," a bustling intergalactic bazaar","the neon-lit underbelly of a cyberpunk metropolis"],
            'obstacles': ["a swarm of nanobots disguised as butterflies", "a grumpy android demanding a software update"," a temporal rift that randomly rewinds time"," a space pirate with a penchant for bad poetry"," a malfunctioning teleportation pad"," an alien diplomat who only speaks in riddles"],
            'solution': ["ingenious hacking skills", "a well-timed photon blast", "a clever use of a gravity well", "an unexpected alliance with a space-faring creature", "an old star map revealing a hidden passage"],
            'adjectives': ["quantum","cryptic", "synthetic", "chrome-plated", "luminous"],
            'actions': ["teleported", "phasered", "hyper-jumped", "beamed","recalibrated","decrypted"],
            # Serious, surprising twist
            'twists': ["It was revealed that the entire planet they were on was actually a single, colossal sleeping organism.", "The item granted them unlimited power, but only after erasing all their memories.", "Their 'partner,' Sidekick, was a deep-cover operative from a future timeline, sent only to retrieve the Item.",""
            "The mission was a simulation designed to test their loyalty to an intergalactic council.","The Item was actually a sentient being that chose them as its new companions.","The true villain was not the obstacle they faced, but the very organization that sent them on the mission.","The Item was a key to a prison holding an ancient cosmic entity, and retrieving it risked unleashing chaos upon the universe."]
        },
        'fantasy': {
            'items': ["the legendary three-leaf clover of luck", "the talking goblet of lukewarm tea", "the staff that only conjures tiny bubbles","the enchanted rubber chicken","the crown of invisible squirrels","the map that leads to nowhere","the sword that hums show tunes","the magical mirror that reveals one's darkest secrets","the cloak that makes the wearer slightly less noticeable","the potion that turns anything into slightly better cheese"],
            'settings': ["the Whispering Forest of the Dryad Clowns", "a floating castle made of gingerbread", "the belly of a mildly annoyed griffin","a village where everyone rides unicycles","a labyrinthine library filled with mischievous books","a mountain that sings opera at dawn","a swamp that smells like old socks","a desert where the sand occasionally forms into tiny sand people"],
            'obstacles': ["a confused wizard who lost his spectacles", "a bridge troll who charges tolls in interpretive dance"," a riddle-speaking sphinx with a cold", "a band of mischievous pixies playing pranks"," a dragon who hoards rubber ducks"," a giant who is afraid of heights"," a witch who only casts spells in limerick form"],
            'adjectives': ["ancient", "enchanted", "mystical", "glimmering","whimsical","bewitched","fanciful","spellbinding"],
            'actions': ["sashayed", "galloped", "chanted", "flew","pranced","ambled","soared","danced","twirled","glided"],
            # Dramatic, mythical twist
            'twists': ["The 'King' they were serving was, in fact, the legendary Item itself, testing their worthiness.", "Upon claiming the Item, all magic in the realm vanished, leaving them powerless.", "The Item was a key that unlocked a new villain—a shadow of their own deepest flaw."]
        },
        'horror': {
            'items': ["the cursed spork of eternal doom", "a porcelain doll that only giggles", "a shadow that eats socks"],
            'settings': ["an old lighthouse where the light bulb is a spooky eyeball", "a basement that smells like fear and mothballs", "a graveyard where the tombstones play soft jazz"],
            'obstacles': ["a ghost that insists on giving bad advice", "a zombie who is very particular about his grammar"],
            'adjectives': ["eerie", "dreadful", "spooky", "clammy"],
            'actions': ["crept", "shivered", "stumbled", "dashed"],
            # Ominous, unresolved twist
            'twists': ["They escaped, only to realize the Item had been absorbed by one of them, who began to slowly transform.", "The terror did not end; the sound of the object's giggling followed them everywhere they went.", "The only way to leave the setting was to permanently replace the monstrous obstacle they had defeated."]
        },
        'love': {
            'items': ["a single, perfect, wilted daisy", "a misdelivered love letter", "a tiny, heart-shaped piece of toast"],
            'settings': ["a cafe where everyone cries happy tears", "a bench under the town's cheesiest statue", "the roof during a very inconvenient rainstorm"],
            'obstacles': ["a rival who knits too well", "a misunderstanding involving a poodle and a sandwich"],
            'adjectives': ["swooning", "awkward", "velvety", "crush-worthy"],
            'actions': ["blushed", "stumbled", "whispered", "gazed"],
            # Surprising, dramatic relationship twist
            'twists': ["The two characters realized the Item was simply a distraction, and their true destiny was to become rivals in a new, competitive knitting league.", "Hero was unknowingly trying to deliver the Item to Sidekick's secret long-distance penpal.", "The person they thought they loved was actually the Obstacle in disguise, hoping to gain their trust."]
        },
        'mystery': {
            'items': ["a tarnished silver locket with no picture", "a coded message written on a napkin", "a shoe that is suspiciously empty"],
            'settings': ["an abandoned museum dedicated to spoons", "the dimly lit back room of a donut shop", "a secret library hidden behind a refrigerator"],
            'obstacles': ["a silent butler who points vaguely", "a coded keypad demanding the square root of a banana"],
            'adjectives': ["shady", "clandestine", "puzzling", "suspicious"],
            'actions': ["snooped", "deduced", "slipped", "eavesdropped"],
            # Surprising, anticlimactic truth twist
            'twists': ["The villain wasn't after the Item at all; they were trying to hide the fact that they worked at the donut shop all along.", "The coded message simply read, 'You owe me five dollars.'", "The entire mystery was staged by the police to see if Detective Hero was paying attention."]
        },
        'comedy': {
            'items': ["a bucket of imaginary chickens", "a self-aware whoopie cushion", "a pair of pants that only sing opera"],
            'settings': ["a circus where the clowns are sadists", "a public restroom where the mirror talks back", "the stage during an amateur magician's failed act"],
            'obstacles': ["a mime stuck in an actual invisible box", "a banana peel that multiplies on contact"],
            'adjectives': ["giggle-inducing", "slapstick", "absurd", "bonkers"],
            'actions': ["galumphed", "yodeled", "tangoed", "skipped"],
            # Absurd, funny twist
            'twists': ["The entire quest was an elaborate, poorly funded prank organized by a grumpy duck.", "The Item granted them the ability to communicate with housepets, which was instantly annoying.", "The prize was simply a coupon for unlimited free stale crackers."]
        }
    }
    
    # --- 3. Randomly Select Plot Elements ---
    
    genre_data = story_elements[genre_choice]
    
    item = random.choice(genre_data['items'])
    setting = random.choice(genre_data['settings'])
    obstacle = random.choice(genre_data['obstacles'])
    adjective = random.choice(genre_data['adjectives'])
    action = random.choice(genre_data['actions'])
    final_twist = random.choice(genre_data['twists']) # Uses the genre-specific twist list

    # --- 4. Genre-Specific Templates ---

    # SCI-FI Template (Serious Tone)
    sci_fi_template = f"""
    Report: Mission {adjective.title()} Echo

    {hero_name} and their genius partner {sidekick_name}, were {random.choice(genre_data['relaxing'])} when they received a distress call from the headquarters. The mission - to retrieve {item} from the hostile environment of {setting}. 
    The two {action} across the solar system, through asteroid fields and nebulae, only to be confronted by {obstacle}. 
    Both of them were in a fix until {sidekick_name} finally employed {random.choice(genre_data['solution'])} and neutralized the threat.
    They finally found {item}. They secured the item and prepared to return to base.
    Once at the base, the two replayed the data from the item, and their past adventures. After the analysis, they discovered a shocking truth:
         {final_twist}
    This discovery changed everything. They were in much deeper waters than they had initially thought. This was only the beginning of a much larger saga.
    MISSION TO BE CONTINUED...
    """

    # FANTASY Template (Dramatic Tone)
    fantasy_template = f"""
    *** The Ballad of the {adjective.title()} Betrayal ***
    
    Brave Sir {hero_name} and his sworn brother, {sidekick_name}, faced the high demand: find the lost {item} hidden deep within the cursed {setting}. 
    They {action} through ancient perils, only to be stopped by the formidable presence of {obstacle}. 
    {hero_name} defeated the threat using both steel and wisdom! 
    They claimed the {item}, but the true reward was the revelation: {final_twist}
    The realm would never be the same.
    """

    # HORROR Template (Ominous Tone)
    horror_template = f"""
    *** Incident Report: The {adjective.title()} Night of the Whispers ***
    
    The air was cold and filled with dread when **{hero_name}** and **{sidekick_name}** arrived at **{setting}**. 
    They sought the vile, whispering **{item}**. They {action} down the darkened hallway, when the terrifying **{obstacle}** appeared! 
    {sidekick_name} distracted the entity with a desperate, unhinged plea, allowing them to seize the {item}. 
    But they should have left it alone. The final, terrible realization struck them: {final_twist}
    The horror had only just begun.
    """
    
    # LOVE Template (Emotional Tone)
    love_template = f"""
    *** A {adjective.title()} Tale of Star-Crossed Secrets ***
    
    **{hero_name}** was desperate to find the precious **{item}**—a symbol of their devotion—that was lost somewhere at the fateful **{setting}**! 
    Their confidante, **{sidekick_name}**, offered support. They {action} past the nervous crowd, navigating their own deep feelings. 
    Their romantic mission was nearly destroyed by the sudden appearance of **{obstacle}**. 
    They overcame the obstacle with a moment of emotional honesty, and as they recovered the {item}, they learned a devastating truth about their relationship: {final_twist}
    Love is rarely simple.
    """

    # MYSTERY Template (Suspenseful Tone)
    mystery_template = f"""
    *** The Case of the {adjective.title()} Truth ***
    
    Detective **{hero_name}** and their sharp-eyed assistant, **{sidekick_name}**, were on the hunt for the critical **{item}** that would crack the case. 
    The trail led them to the secluded **{setting}**. They quietly {action} the premises until they were confronted by **{obstacle}**. 
    {sidekick_name} used a keen observation to bypass the trap, and they found the {item}! 
    But the truth it revealed about the identity of the culprit was surprisingly mundane and yet utterly shocking: {final_twist}
    The case was closed, but the puzzle remains.
    """

    # COMEDY Template (Absurd/Funny Tone)
    comedy_template = f"""
    *** The {adjective.title()}, Absurd, and Utterly Pointless Quest ***

    {hero_name} and {sidekick_name} woke up and decided to pursue the infamous {item} at {setting}. They immediately {action} off a curb.
    Their biggest challenge was the nonsensical presence of {obstacle}.
    After a chaotic three-minute wrestling match involving a tiny hat, they won!
    They claimed the {item}, but then realized the horrible, hilarious truth: {final_twist}
    Fin. Now go get a snack.
    """
    
    # Map genre choice to template
    template_map = {
        'sci-fi': sci_fi_template,
        'fantasy': fantasy_template,
        'horror': horror_template,
        'love': love_template,
        'mystery': mystery_template,
        'comedy': comedy_template,
    }

    final_story = template_map[genre_choice]

    # --- 5. Output ---
    
    print("\n" + "="*70)
    print(f"🎉 YOUR TAILORED {genre_choice.upper()} STORY IS READY! 🎉")
    print("="*70)
    print(final_story)
    print("="*70)

# Run the function
if __name__ == "__main__":
    generate_multi_genre_story_with_templates()