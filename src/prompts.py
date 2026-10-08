CONTENT_TYPES = {
    "blog": {
        "label": "Blog Post",
        "template": (
            "Write a blog post: {topic}.\n"
            "Include a catchy title, a short introduction, 3 section with "
            "subheading, and a conclusion."
        ),
    },
    "email": {
        "label": "Email",
        "template": (
            "Write an email about: {topic}.\n"
            "Include a subject line, a greeting, a clear body, and a polite closing."
        ),
    },
    "caption": {
        "label": "Social media caption",
        "template": (
            "Write 3 different social media captions about: {topic}.\n"
            "Add relevant emojis and 3-5 hashtags to each one."
        ),
    },
    "product": {
        "label": "Product description",
        "template": (
            "Write a product description for: {topic}.\n"
            "Highlight the key benefits, who it is for, and end with a short "
            "call to action."
        ),
    },
}

TONES = {
    "professional": "Use a professional, polished tone.",
    "friendly": "Use a warm, friendly, conversational tone.",
    "funny": "Use a light, humorous tone with a bit of wit.",
}

LENGTHS = {
    "short": "Keep it short (around 100 words).",
    "medium": "Make it medium length (around 250 words).",
    "long": "Make it detailed (around 500 words).",
}