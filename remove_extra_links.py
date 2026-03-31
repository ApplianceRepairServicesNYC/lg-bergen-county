#!/usr/bin/env python3
"""
Remove appliance-links and service-area-links sections from all city pages.
"""

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove appliance-links div
    content = re.sub(
        r'\s*<div class="appliance-links"[^>]*>.*?</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    # Remove service-area-links div
    content = re.sub(
        r'\s*<div class="service-area-links"[^>]*>.*?</div>\s*',
        '\n',
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = '/Users/globalaffiliate/lg-bergen-county/nj'
    updated = 0

    for city_dir in os.listdir(base_dir):
        city_path = os.path.join(base_dir, city_dir)
        if os.path.isdir(city_path):
            index_file = os.path.join(city_path, 'index.html')
            if os.path.exists(index_file):
                if fix_file(index_file):
                    updated += 1
                    print(f"Updated: {index_file}")

    print(f"\nTotal files updated: {updated}")

if __name__ == '__main__':
    main()
