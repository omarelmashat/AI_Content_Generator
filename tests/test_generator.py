import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from generator import build_prompt


def test_prompt_contains_topic_tone_and_length():
    prompt = build_prompt("blog", "healthy habits", "friendly", "short")
    assert "healthy habits" in prompt
    assert "friendly" in prompt
    assert "100 words" in prompt


def test_empty_topic_raises():
    with pytest.raises(ValueError):
        build_prompt("blog", "   ", "friendly", "short")


def test_unknown_content_type_raises():
    with pytest.raises(ValueError):
        build_prompt("poem", "spring", "friendly", "short")


def test_unknown_tone_raises():
    with pytest.raises(ValueError):
        build_prompt("blog", "spring", "angry", "short")


def test_unknown_length_raises():
    with pytest.raises(ValueError):
        build_prompt("blog", "spring", "friendly", "huge")