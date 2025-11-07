#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: print( yoki logger.xxx( ichidagi multi-line f-stringlar
# Misol:
#   print(
#       f"Text {
#           var}")
# Ga aylanishi kerak:
#   print(f"Text {var}")

count = 0
max_iterations = 100  # Cheksiz loop oldini olish

for iteration in range(max_iterations):
    prev_content = content
    
    # Pattern 1: print( va logger ichidagi multi-line f-strings
    pattern = r'((?:logger\.\w+|print)\(\s*)\n\s*(f"[^"]*)\{\s*\n\s*([^}]+)\}'
    
    def replacer(match):
        global count
        prefix = match.group(1)
        fstring_start = match.group(2)
        var = match.group(3).strip()
        count += 1
        return f'{prefix}{fstring_start}{{{var}}}'
    
    content = re.sub(pattern, replacer, content, flags=re.MULTILINE)
    
    # Agar o'zgarish bo'lmasa, to'xtatish
    if content == prev_content:
        break

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ {count} ta o'zgarish amalga oshirildi!")
