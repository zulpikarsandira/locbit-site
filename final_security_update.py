import re

def final_update():
    with open('security.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        ('REMARKABLE', 'SECURE PROTOCOLS'),
        ('Trusted by worldwide', 'Audited by experts'),
        ('Trusted by teams', 'Trusted by professionals'),
        ('We specialize in branding, UI/UX design, digital experiences, and product design.', 'We specialize in AES-256 encryption, BLE routing, and offline data sovereignty.'),
        ('We help brands and products stand out through branding, UX, and thoughtful digital design.', 'We guarantee private, off-grid communication through robust cryptographic protocols.'),
        ('Hi! I’m Jenifer. I’m the Design Manager at Locbit and I’m here to answer any questions you might hav', 'Hi! I’m Ijal. I’m the Security Engineer at Locbit and I’m here to answer your questions regarding our encryption.'),
        ('Early-stage teams turning ideas into products people love. We help define identity, UX, and launch-ready experiences.', 'Security-conscious individuals and teams operating in remote or low-connectivity environments.'),
        ('Companies ready to scale their brand and digital presence. We refine systems, improve usability, and elevate perception.', 'Field researchers, disaster response units, and expedition groups requiring reliable off-grid comms.'),
        ('In-house teams building complex digital products. We support with UX strategy, UI systems, and product validation.', 'Activists and journalists requiring total forward secrecy, metadata protection, and untraceable hardware footprints.'),
        ('Agencies and studios needing a design partner. We plug in seamlessly for branding, UI/UX, and execution.', 'Enterprise teams establishing air-gapped internal networks without server reliance or internet exposure.'),
        ('Clear thinking, close collaboration, and purposeful execution.', 'Mathematical certainty, zero-knowledge architecture, and perfect execution.'),
    ]

    count = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            count += 1
        else:
            # try finding a partial match string since html might format differently
            pass

    # Fix image for Ijal / Jenifer
    # The original template uses a portrait for Jenifer, let's just leave the image as is for now since it's a generic portrait.
    
    with open('security.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied {count}/{len(replacements)} final security replacements.")

if __name__ == '__main__':
    final_update()
