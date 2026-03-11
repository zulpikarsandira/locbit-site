from bs4 import BeautifulSoup
import re

with open('security.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- TEXT CONTAINERS ---")
for text in ['REMARKABLE', 'Branding', 'BRANDING Design', 'Explore', 'Design', 'Deliver', 'We specialize in', 'What is your design approach?']:
    elem = soup.find(string=re.compile(text, re.IGNORECASE))
    if elem:
        print(f"FOUND: '{text}' -> {repr(elem.parent)}")
    else:
        print(f"MISSING: '{text}'")
