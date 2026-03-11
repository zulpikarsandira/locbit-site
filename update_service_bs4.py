from bs4 import BeautifulSoup
import re

def parse_and_update():
    with open('service.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Update Hero H1
    h1 = soup.find('h1', string=re.compile('Service', re.IGNORECASE))
    if h1: h1.string = 'Technology'

    # Update Hero Paragraph
    hero_p = soup.find('p', string=re.compile('Delivering tailored digital solutions'))
    if hero_p: hero_p.string = 'Explore the core protocols, custom hardware bridges, and security abstractions that power Locbit.'

    # Update H2s
    h2s = soup.find_all('h2')
    h2_replacements = {
        'Understand': 'System Architecture',
        'Strategy': 'Resource Utilization',
        'Design': 'Network Topology',
        'A focused approach to meaningful design': 'A deeply optimized approach to decentralized routing',
        'Developer FAQ': 'Developer FAQ',
        'REMARKABLE': 'ENGINEERED',
    }
    for h2 in h2s:
        t = h2.get_text(strip=True)
        if t in h2_replacements:
            h2.string = h2_replacements[t]

    # Content replacements for the "Services" boxes
    ps = soup.find_all('p', class_='paragraph-regular')
    for p in ps:
        t = p.get_text(strip=True)
        if 'We help brands build clear' in t:
            p.string = 'Locbit enforces absolute data sovereignty by routing all connectivity over localized Bluetooth paths rather than internet-connected mesh authorities.'
        if 'We specialize in branding, UI/UX design' in t:
            p.string = 'Locbit encrypts payloads using AES-256 primitives immediately on-device before attempting any external hardware broadcast.'

    # Find the "Branding Design", "UI/UX Design", "Digital Experience" divs
    smalls = soup.find_all('div', class_='font-size-sm')
    for s in smalls:
        t = s.get_text(strip=True)
        if 'Branding Design' in t: s.string = 'Go Modules'
        if 'UI/UX Design' in t: s.string = 'JNI / Gomobile Bridge'
        if 'Digital Experience' in t: s.string = 'BLE Mesh Routing'
        if 'Product Design' in t: s.string = 'Secure Enclave Storage'

    with open('service.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Updated service.html using BS4 parsing.")

if __name__ == '__main__':
    parse_and_update()
