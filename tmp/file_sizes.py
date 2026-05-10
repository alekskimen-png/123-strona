import os
for f in ['index.html', 'style.css', 'script.js']:
    size = os.path.getsize(f)
    print(f"{f}: {size} bytes")