import os
from bs4 import BeautifulSoup

def update_nav_links():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Mapping exact nav link text to href
    nav_map = {
        'Overview': 'index.html',
        'Features': 'features.html',
        'Security': 'security.html',
        'About': 'about.html',
        'Credits': 'work.html',
        'Technology': 'service.html',
        'Updates': 'blog.html',
        'Contact': 'contact.html',
    }
    
    for filename in html_files:
        changed = False
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all a tags that have 'nav-link' somewhere in their class
        links = soup.find_all('a', class_=lambda c: c and 'nav-link' in c)
        
        for link in links:
            text_div = link.find('div', class_='nav-link-text')
            if text_div:
                link_text = text_div.get_text(strip=True)
                if link_text in nav_map:
                    target_href = nav_map[link_text]
                    if link.get('href') != target_href:
                        link['href'] = target_href
                        changed = True
                            
        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated nav inside: {filename}")

if __name__ == '__main__':
    update_nav_links()
    print("Done checking all files.")
