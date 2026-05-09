import sys
sys.path.insert(0, '/')

# Read the file
with open('/gnojnik.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('nav-links')
if idx >= 0:
    ul_start = content.rfind('<ul', 0, idx)
    ul_end = content.find('</ul>', idx) + 5
    nav_section = content[ul_start:ul_end]
    print(nav_section)
    
    if 'chipasach' in nav_section:
        print("\n\nCHIPASACH ALREADY IN NAV")
    else:
        print("\n\nCHIPASACH NOT IN NAV - NEED TO ADD")
else:
    print("nav-links not found")
