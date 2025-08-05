import urllib.parse

def get_pollinations_url(prompt):
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}"
