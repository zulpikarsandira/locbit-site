from bs4 import BeautifulSoup
import os

# --- 1. Fix Navbar Logo Centering ---
html_files = [
    '/home/zulpikar/Documents/wbflow/cravia1/index.html',
    '/home/zulpikar/Documents/wbflow/cravia1/features.html',
    '/home/zulpikar/Documents/wbflow/cravia1/security.html',
    '/home/zulpikar/Documents/wbflow/cravia1/about.html',
    '/home/zulpikar/Documents/wbflow/cravia1/work.html',
    '/home/zulpikar/Documents/wbflow/cravia1/service.html',
    '/home/zulpikar/Documents/wbflow/cravia1/blog.html',
    '/home/zulpikar/Documents/wbflow/cravia1/contact.html',
    '/home/zulpikar/Documents/wbflow/cravia1/404.html',
]

for p in html_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # We want to add absolute positioning to brand-logo-wrap so it is always strictly centered.
    if 'style="position: absolute; left: 50%; transform: translateX(-50%);"' not in c:
        c = c.replace('<a class="brand-logo-wrap w-inline-block" href="index.html">',
                      '<a class="brand-logo-wrap w-inline-block" href="index.html" style="position: absolute; left: 50%; transform: translateX(-50%);">')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)

print('Navbar logos centered in all files.')

# --- 2. Update security.html Template Content ---
security_file = '/home/zulpikar/Documents/wbflow/cravia1/security.html'
with open(security_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# A. Testimonials
locbit_testimonials = [
    {"name": "Secure Operations Commander", "role": "Remote Field Team", "text": "“Locbit has completely transformed our off-grid communications. We never have to worry about cellular interception or compromised networks.”"},
    {"name": "Sarah Williams", "role": "Journalist", "text": "“Protecting my sources is my top priority. With Locbit’s AES-256 encryption, I can securely transmit data without leaving any metadata trails.”"},
    {"name": "Chris Alvarez", "role": "Disaster Response Lead", "text": "“In disaster zones where infrastructure is down, Locbit’s mesh framework keeps our entire response team connected.”"}
]

cards = soup.select('.testimonial-card')
for idx, card in enumerate(cards):
    t_data = locbit_testimonials[idx % len(locbit_testimonials)] # cycle through if more cards exist
    
    p = card.find('p', class_='paragraph-regular')
    if p: p.string = t_data["text"]
    
    name = card.select_one('.client-info-block .font-size-lg')
    if name: name.string = t_data["name"]
    
    role = card.select_one('.client-info-block .font-size-xs')
    if role: role.string = t_data["role"]

# B. Industries (WHO WE WORK WITH)
locbit_industries = [
    "Journalism & Media",
    "Activists & NGOs",
    "Disaster Response",
    "Remote Field Teams",
    "Secure Facilities"
]

industry_lists = soup.select('ul[role="list"]._w-we-do-list')
for industry_ul in industry_lists:
    items = industry_ul.select('li.w-we-do-list-item div')
    for idx, item in enumerate(items):
        if idx < len(locbit_industries):
            item.string = locbit_industries[idx]
        else:
            item.string = locbit_industries[0]

# C. Security Audit FAQ
locbit_faqs = [
    {"q": "Is Locbit's encryption open source?", "a": "Yes, our core cryptographic libraries and mesh routing protocols are fully open source, allowing independent security researchers to audit the code for vulnerabilities and backdoors."},
    {"q": "How does Locbit protect against metadata analysis?", "a": "Unlike traditional messaging apps, Locbit obscures routing data. Because packets bounce through decentralized nodes, it is cryptographically difficult for observers to determine the original sender or final recipient."},
    {"q": "Has Locbit undergone independent security audits?", "a": "Absolutely. We regularly contract third-party cybersecurity firms to conduct penetration testing and full code audits on our application and underlying mesh framework. Summaries of these audits are available upon request."},
    {"q": "What happens if a device is physically compromised?", "a": "Locbit features full disk encryption integration and a remote wipe capability. Additionally, auto-deleting messages ensure that sensitive data does not persist on the device longer than necessary."},
    {"q": "Does Locbit store any user data on central servers?", "a": "No. The Locbit architecture is entirely decentralized. Your messages, keys, and metadata are never stored on any central server, meaning there is nothing for third parties to hack or subpoena."}
]

faq_items = soup.select('.faq-accordion-item-v2')
for idx, item in enumerate(faq_items):
    f_data = locbit_faqs[idx % len(locbit_faqs)]
    
    q = item.select_one('.faq-top-v2 .capitalize')
    if q: q.string = f_data["q"]
    
    a = item.select_one('.faq-bottom p')
    if a: a.string = f_data["a"]

# Write changes back to security.html
with open(security_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Template content in security.html replaced with Locbit data.')
