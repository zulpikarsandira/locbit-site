import os
from bs4 import BeautifulSoup
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    if 'WHO USES' in content.upper() or 'you ask' in content.lower():
        print(f"{f} contains WHO USES/you ask")

with open('index.html') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    h1s = soup.find_all(['h1', 'h2'])
    for h in h1s[:5]:
        print("index.html header:", h.text.strip())

