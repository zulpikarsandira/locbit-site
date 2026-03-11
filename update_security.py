import re

def update_security():
    with open('security.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        # Hero section
        ('CREATIVE</h1>', 'LOCBIT</h1>'),
        ('REMARKABLE</h1>', 'SECURITY</h1>'),
        ('We help brands and digital products find clarity through branding, UI/UX, and thoughtful design systems.', 
         'Locbit guarantees communication privacy through decentralized Bluetooth topologies and device-level cryptography.'),
        
        # Tags below hero
        ('>Branding <', '>AES-256 <'),
        ('>UI/UX<', '>Decentralized<'),
        ('>Digital Experiences<', '>No Logs<'),
        ('>Product Design<', '>P2P<'),

        # About section
        ('We don\u2019t just design interfaces. We shape how brands are seen, felt, and experienced.',
         'We don\u2019t just send messages. We build air-gapped security boundaries that governments can\u2019t breach.'),
        ('Designing with intention', 'Cryptography with intention'),
        ('Every brand has a story \u2014 our role is to translate it into clear identities, thoughtful interfaces, and digital experiences that feel natural and purposeful.',
         'Every message is sovereign \u2014 our architecture is designed to enforce maximum user privacy by avoiding central authorities, enforcing Perfect Forward Secrecy, and leveraging off-grid BLE connectivity.'),

        # "What we do" -> "Security Protocols"
        ('>What we do<', '>Security Protocols<'),
        # Tabs
        ('>BRANDING Design<', '>END-TO-END ENCRYPTION<'),
        ('We build brand identities that feel intentional, distinctive, and built to last. From early-stage positioning to full rebrands, we help define how your brand looks, sounds, and shows up everywhere.',
         'Locbit implements AES-256-GCM encryption natively on your device. Cryptographic keys are exchanged securely over BLE using ECDH, meaning data is mathematically impossible to intercept over the air.'),
        ('>UI/UX DESIGN<', '>FORWARD SECRECY<'),
        ('>DIGITAL EXPERIENCES<', '>OFF-GRID ROUTING<'),
        ('>PRODUCT DESIGN<', '>ZERO DATA RETENTION<'),

        # Works -> Security Audits
        ('>Selected work<', '>Security Architecture<'),

        # Approach -> Approach
        ('A focused approach to meaningful design', 'A strictly governed approach to off-grid security'),
        ('>Understand<', '>Key Exchange<'),
        ('We align on goals, users, and context before making design decisions.', 'ECDH handshake securely establishes an ephemeral key between peers over Bluetooth.'),
        ('>Explore<', '>Encrypt Frame<'),
        ('We test ideas, explore directions, and shape early concepts.', 'Data payloads are wrapped in AES-256 envelopes using the synchronized session key.'),
        ('>Design<', '>Transmit BLE<'),
        ('We craft identities, interfaces, and systems with clarity and intent.', 'Data is broadcast over adaptive Bluetooth Low Energy channels without IP routing mechanisms.'),
        ('>Deliver<', '>Wipe State<'),
        ('We refine, document, and hand off work ready to scale.', 'Upon session termination, memory buffers are zeroed and ephemeral keys are immediately destroyed.'),

        # Pricing -> Specifications
        ('Our Simple pricing', 'Encryption Specifications'),
        ('>STARTER PACKAGE<', '>CRYPTO CORE<'),
        ('Ideal for startups and early-stage teams looking to establish a strong visual presence.', 'Industry standard primitives ensuring absolute mathematical privacy for every bit of data.'),
        ('>PROFESSIONAL PACKAGE<', '>TRANSPORT LAYER<'),
        ('Perfect for businesses ready to scale with a polished brand and user-focused digital experience.', 'BLE-optimized framing that mitigates packet sniffing and metadata tracking.'),
        ('>PRODUCT PACKAGE<', '>DEVICE INTEGRATION<'),
        ('Designed for teams building digital products that require clarity, usability, and scalability.', 'Secure hardware enclave utilization and restricted OS-level daemon permissions.'),

        # FAQ -> FAQ
        ('You ask. We answer', 'Security Audit FAQ'),
        ('What services do you offer?', 'Is the encryption audited?'),
        ('We specialize in brand identity, UI/UX design, and digital product creation. Whether you need a full rebrand or a focused app interface, we bring clarity and purpose to every project.',
         'Our AES-256 and ECDH implementations are based on heavily audited Go cryptography primitives. Internal gray-box testing ensures memory safety.'),
        ('How long does a typical project take?', 'Can messages be traced?'),
        ('Project timelines vary. A brand identity usually takes 4-6 weeks, while a comprehensive UI/UX project can span 8-12 weeks. We\u2019ll provide a specific timeline once we understand your goals.',
         'No. Locbit uses Bluetooth Low Energy mesh routing without tying MAC addresses to user identities. No IP traces, no server logs, no metadata.'),
        ('What is your design approach?', 'What happens if my device is seized?'),
        ('We believe in purposeful, user-centric design. We start by understanding your audience and goals, then iterate through concepts, always focusing on clarity, simplicity, and impact.',
         'Data at rest is secured by Android\u2019s file-level encryption. Messages are kept in volatile memory and can be configured to auto-delete after reading.'),

        # Title / Meta
        ('Locbit - Webflow HTML Website Template', 'Locbit Security \u2014 Architecture & Cryptography'),
    ]

    count = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            count += 1
        else:
            print(f"NOT FOUND: '{old[:50]}...'")

    with open('security.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied {count}/{len(replacements)} security replacements.")

if __name__ == '__main__':
    update_security()
