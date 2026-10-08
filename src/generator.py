from api_client import generate_text
from prompts import CONTENT_TYPES, TONES, LENGTHS

def build_prompt(content_type: str, topic: str, tone: str, length: str) -> str:
    if content_type not in CONTENT_TYPES:
        raise ValueError(f"Invalid content type: {content_type}")
    if tone not in TONES:
        raise ValueError(f"Invalid tone: {tone}")
    if length not in LENGTHS:
        raise ValueError(f"Invalid length: {length}")
    if not topic.strip():
        raise ValueError("Topic cannot be empty")

    base = CONTENT_TYPES[content_type]["template"].format(topic=topic.strip())
    return f"{base}\n{TONES[tone]}\n{LENGTHS[length]}\nReturn only the content, with no extra commentary"

def generate_content(content_type: str, topic: str, tone: str = "professional", length: str = "medium") -> str:
    prompt = build_prompt(content_type, topic, tone, length)
    return generate_text(prompt)

if __name__ == "__main__":
    print(generate_content("blog", "The Future of AI in Healthcare", "friendly", "long"))