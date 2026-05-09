import re

with open('/gnojnik.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find nav-links section
idx = content.find('nav-links')
if idx >= 0:
    # Find the closing </ul> after nav-links
    ul_start = content.rfind('<ul', 0, idx)
    ul_end = content.find('</ul>', idx) + 5
    print("NAV SECTION:")
    print(content[ul_start:ul_end])
else:
    print("nav-links not found")
