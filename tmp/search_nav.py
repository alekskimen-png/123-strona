with open('/gnojnik.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('nav-links')
ul_start = content.rfind('<ul', 0, idx)
ul_end = content.find('</ul>', idx) + 5
nav = content[ul_start:ul_end]

# Save to file for reading
with open('/tmp/nav_output.txt', 'w', encoding='utf-8') as f:
    f.write(nav)
