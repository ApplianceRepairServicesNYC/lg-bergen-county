#!/usr/bin/env python3
"""
Remove UNIQUE CONTENT sections from all appliance pages.
"""

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove the entire UNIQUE CONTENT FOR APPLIANCES section
    content = re.sub(
        r'<!-- UNIQUE CONTENT FOR [A-Z\s\-]+ - Generated [0-9\-]+ -->\s*<section class="brand-expertise.*?</section>\s*<!-- END UNIQUE CONTENT FOR [A-Z\s\-]+ -->\s*',
        '',
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = '/Users/globalaffiliate/lg-bergen-county/appliances'
    updated = 0

    for appliance_dir in os.listdir(base_dir):
        appliance_path = os.path.join(base_dir, appliance_dir)
        if os.path.isdir(appliance_path):
            index_file = os.path.join(appliance_path, 'index.html')
            if os.path.exists(index_file):
                if fix_file(index_file):
                    updated += 1
                    print(f"Updated: {index_file}")

    print(f"\nTotal files updated: {updated}")

if __name__ == '__main__':
    main()
