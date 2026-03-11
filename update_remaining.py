from bs4 import BeautifulSoup

def update_remaining():
    # Update Blog
    with open('blog.html', 'r', encoding='utf-8') as f:
        soup_b = BeautifulSoup(f.read(), 'html.parser')
    h1 = soup_b.find('h1')
    if h1 and 'Read our' in h1.get_text(): h1.string = 'Latest Updates'
    
    ps = soup_b.find_all('p', class_='paragraph-large')
    for p in ps:
        if 'Thoughts, updates' in p.get_text():
            p.string = 'Technical changelogs, security bulletins, and development updates.'

    # just replace the first few blog listing texts
    badges = soup_b.find_all('div', class_='font-size-sm')
    if len(badges) >= 3:
        badges[0].string = 'Release Notes'
        badges[1].string = 'Security'
        badges[2].string = 'Architecture'
        
    titles = soup_b.find_all('div', class_='listing-title')
    if len(titles) >= 3:
        titles[0].string = 'Version 1.2: Enhanced Battery Optimization for BLE Scanning'
        titles[1].string = 'Forward Secrecy: How Locbit destroys keys post-session'
        titles[2].string = 'Building the Java-to-Golang Native Bridge'

    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(str(soup_b))
        
    # Update Contact
    with open('contact.html', 'r', encoding='utf-8') as f:
        soup_c = BeautifulSoup(f.read(), 'html.parser')
        
    h1 = soup_c.find('h1')
    if h1: h1.string = 'Contact Us'
    
    c_p = soup_c.find('p', class_='paragraph-large')
    if c_p: c_p.string = 'Reach out for security audits, bug bounties, or enterprise network integration inquiries.'

    # Update generic addresses
    addr = soup_c.find(string=lambda t: t and '456 Innovation' in t)
    if addr: addr.replace_with('Decentralized / Remote Operations')
    
    tel = soup_c.find(string=lambda t: t and '(555)' in t)
    if tel: tel.replace_with('secure@locbit.xyz')
    
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(str(soup_c))

    # Update 404
    with open('404.html', 'r', encoding='utf-8') as f:
        soup_4 = BeautifulSoup(f.read(), 'html.parser')
        
    h1_4 = soup_4.find('h1')
    if h1_4: h1_4.string = 'Connection Lost'
    
    p_4 = soup_4.find('p', class_='paragraph-large')
    if p_4: p_4.string = 'The requested peer endpoint could not be found or the routing table has expired.'
    
    with open('404.html', 'w', encoding='utf-8') as f:
        f.write(str(soup_4))
        
    print("Updated blog, contact, and 404 pages.")

if __name__ == '__main__':
    update_remaining()
