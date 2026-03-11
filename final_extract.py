from bs4 import BeautifulSoup

with open('security.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- H2 and H3 HEADINGS ---")
for tag in soup.find_all(['h2', 'h3']):
    text = tag.get_text(strip=True)
    if text: 
        print(tag.name.upper() + ":", repr(text))
        
print("\n--- FAQS ---")
for faq in soup.find_all(class_='faq-list'):
    print(repr(faq.get_text(strip=True)[:200]))

print("\n--- CONTENT BLOCKS ---")
for p in soup.find_all('p'):
    t = p.get_text(strip=True)
    if len(t) > 30 and 'address' not in t.lower():
        print("P:", repr(t[:100]))
