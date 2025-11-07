#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-line f-string fixer - bir nechta qatorga bo'lingan f-stringlarni bir qatorga yig'ish
"""
import re

print("📖 app.py faylini o'qiyapman...")
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔧 Multi-line f-stringlarni tuzatish...")

# Pattern 1: print(f"text {\n    var}") -> print(f"text {var}")
# Pattern 2: logger.xxx(f"text {\n    var}") -> logger.xxx(f"text {var}")

changes = 0
max_iter = 200  # Maksimum iteratsiya (xavfsizlik uchun)

for i in range(max_iter):
    prev = content
    
    # Pattern: f"...{\s+\n\s+...}"
    # Misol: f"Text {\n            var}"
    pattern = r'(f"[^"]*)\{\s*\n\s*([^}]+)\}'
    
    def fix(match):
        global changes
        prefix = match.group(1)
        var = match.group(2).strip()
        changes += 1
        return f'{prefix}{{{var}}}'
    
    content = re.sub(pattern, fix, content)
    
    # Agar o'zgarish bo'lmasa, to'xtatish
    if content == prev:
        break

print(f"✅ {changes} ta multi-line f-string tuzatildi!")
print("💾 Faylga yozish...")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✨ Tayyor! Endi test qiling: python -c 'import app'")
