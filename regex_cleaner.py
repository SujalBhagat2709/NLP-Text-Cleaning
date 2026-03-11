import re

def regex_clean(text):
    
    text = text.lower()
    
    text = re.sub(r"[^\w\s]", "", text)
    
    text = re.sub(r"\d+", "", text)
    
    text = re.sub(r"\s+", " ", text).strip()
    
    return text


if __name__ == "__main__":
    
    sample = "Hello!!! This is NLP 2026."
    
    cleaned = regex_clean(sample)
    
    print("Original:", sample)
    print("Cleaned:", cleaned)