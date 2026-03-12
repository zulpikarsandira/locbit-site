import os
from bs4 import BeautifulSoup

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    changed = False

    # 1. Remove the Overview link in the sidebar menu
    # The sidebar navigation was moved to nav-col-left
    nav_left = soup.find('div', class_='nav-col-left')
    if nav_left:
        # Find the link that contains the text 'Overview'
        for a in nav_left.find_all('a', class_='nav-link-block'):
            if 'Overview' in a.get_text():
                # We need to remove the divider line next to it.
                # Typically it is the next sibling
                next_elem = a.find_next_sibling()
                if next_elem and next_elem.name == 'div' and 'devider-line' in next_elem.get('class', []):
                    next_elem.decompose()
                a.decompose()
                changed = True
                print(f"[{os.path.basename(filepath)}] Removed Overview link from sidebar.")
                break

    # 2. Update all href="features.html" to href="index.html"
    for a in soup.find_all('a', href=True):
        if 'features.html' in a['href']:
            a['href'] = a['href'].replace('features.html', 'index.html')
            changed = True
            
    # 3. Clean up any `/old-home-2` links (specifically found in footer and 404 page)
    for a in soup.find_all('a', href=True):
        if a['href'] == '/old-home-2':
            a['href'] = 'index.html'
            changed = True
            
        # Clean up any remaining hardcoded overview links (just in case)
        if 'old-home' in a['href']:
            a['href'] = 'index.html'
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"[{os.path.basename(filepath)}] Updated successfully.")

if __name__ == '__main__':
    base_dir = '/home/zulpikar/Documents/wbflow/cravia1'
    files = [
        'index.html',
        'about.html', 
        'security.html',
        'service.html',
        'work.html',
        'blog.html',
        'contact.html',
        '404.html'
    ]
    
    for file_name in files:
        file_path = os.path.join(base_dir, file_name)
        if os.path.exists(file_path):
            update_html(file_path)
