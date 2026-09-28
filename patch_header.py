import re

with open('assets/css/v2.css', 'r') as f:
    css = f.read()

# Add padding-top to body
css = re.sub(
    r'(body\.v2-body\s*\{[^}]+)(overflow-x:\s*clip;)',
    r'\1\2\n  padding-top: 70px;',
    css
)

# Change .v2-header to fixed
css = re.sub(
    r'(\.v2-header\s*\{[\s\S]*?)position:\s*sticky;',
    r'\1position: fixed;\n  width: 100%;\n  left: 0;',
    css
)

with open('assets/css/v2.css', 'w') as f:
    f.write(css)

print("Patched v2.css")
