import os
for f in ['index.html', 'script.js', 'style.css', 'app.py', 'kalkulator.py', 'ai-style.css']:
    if os.path.exists(f):
        size = os.path.getsize(f)
        print(f"{f}: {size} bytes")
