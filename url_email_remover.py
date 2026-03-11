import re

def remove_urls_emails(text):
    
    text = re.sub(r"http\S+", "", text)
    
    text = re.sub(r"www\S+", "", text)
    
    text = re.sub(r"\S+@\S+", "", text)
    
    return text.strip()


if __name__ == "__main__":
    
    sample = "Visit https://example.com or email test@mail.com"
    
    result = remove_urls_emails(sample)
    
    print(result)