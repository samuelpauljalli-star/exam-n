import re

with open(r'c:\websites 000\exam n\exam.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content, count = re.subn(r'(        "id": 100,.*?        \]\n    )\},.*?(];)', r'\1}\n\2', content, flags=re.DOTALL)

if count > 0:
    with open(r'c:\websites 000\exam n\exam.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success! Replaced {count} times.")
else:
    print("Failed to replace.")
