with open('../gnojnik.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('nav-links')
if idx >= 0:
    # Find the ul containing nav-links
    ul_start = content.rfind('<ul', 0, idx)
    ul_end = content.find('</ul>', idx) + 5
    nav_section = content[ul_start:ul_end]
    print(nav_section)
    
    # Check if chipasach is already there
    if 'chipasach' in nav_section:
        print("\n--- CHIPASACH ALREADY IN NAV ---")
    else:
        print("\n--- CHIPASACH NOT IN NAV - NEED TO ADD ---")
else:
    print("nav-links not found")
