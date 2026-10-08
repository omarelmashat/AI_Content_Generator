from datetime import datetime
from pathlib import Path

from generator import generate_content
from prompts import CONTENT_TYPES, TONES, LENGTHS

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"

def choose(title: str, options: dict) -> str:
    keys = list(options.keys())
    print(f"\n {title}")
    for i, key in enumerate(keys, start=1):
        label = options[key]["label"] if isinstance(options[key] ,dict) else key.capitalize()
        print(f" {i}. {label}")

    while True:
        choice = input("Choose a number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return keys[int(choice) -1]
        print("Invalid choice, try again.")


def save_to_file(content_type: str, text: str) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = OUTPUT_DIR / f"{content_type}_{timestamp}.txt"
    path.write_text(text, encoding="utf-8")
    return path

def main():
    print("=== AI Content Generator ===")

    while True:
        content_type = choose("What do you want to create?", CONTENT_TYPES)
        tone = choose("Pick a tone:", TONES)
        length = choose("Pick a length:", LENGTHS)

        topic = ""
        while not topic:
            topic = input("\nWhat is the topic? ").strip()

        print("\nGenerating...\n")
        try:
            result = generate_content(content_type, topic, tone, length)
        except Exception as e:
            print(f"Something went wrong: {e}")
        else:
            print(result)
            if input("\nSave to a file? (y/n): ").strip().lower() == "y":
                print(f"Saved to {save_to_file(content_type, result)}")

        if input("\nCreate another? (y/n): ").strip().lower() != "y":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()