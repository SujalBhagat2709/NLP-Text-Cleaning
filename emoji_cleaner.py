import re

def remove_emojis(text):
    
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "]+",
        flags=re.UNICODE
    )

    return emoji_pattern.sub(r'', text)


if __name__ == "__main__":
    
    sample = "I love NLP 😍🚀"
    
    print(remove_emojis(sample))