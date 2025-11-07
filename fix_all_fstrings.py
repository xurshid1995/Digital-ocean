#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-line f-stringlarni bir qatorga yig'ish
"""
import re

def fix_multiline_fstrings(content):
    """
    Multi-line f-stringlarni topib, bir qatorga yig'ish
    Pattern: print( va logger.debug( ichidagi multi-line f-stringlar
    """
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Agar logger yoki print( va f" bor bo'lsa
        if ('logger.' in line or 'print(' in line) and 'f"' in line:
            # f-string boshlanishi
            if line.strip().endswith('f"') or ('{' in line and not '}' in line and not line.strip().endswith(')')):
                # Multi-line f-string, keyingi qatorlarni yig'ish
                collected = [line]
                i += 1
                paren_count = line.count('(') - line.count(')')
                
                while i < len(lines):
                    next_line = lines[i]
                    collected.append(next_line)
                    paren_count += next_line.count('(') - next_line.count(')')
                    
                    # F-string tugashi
                    if '")' in next_line or (paren_count <= 0):
                        break
                    i += 1
                
                # Yig'ilgan qatorlarni birlashtirish
                full_text = '\n'.join(collected)
                
                # f-string ichidagi matnni topish
                match = re.search(r'(logger\.\w+|print)\(\s*f"([^"]*(?:\{[^}]+\}[^"]*)*)"', full_text, re.DOTALL)
                if match:
                    prefix = match.group(1)
                    fstring_content = match.group(2)
                    
                    # Ichki matnni tozalash
                    cleaned = re.sub(r'\s+', ' ', fstring_content).strip()
                    
                    # Indent ni saqlash
                    indent = re.match(r'(\s*)', collected[0]).group(1)
                    
                    # Yangi qator yaratish
                    fixed_line = f'{indent}{prefix}(f"{cleaned}")'
                    fixed_lines.append(fixed_line)
                else:
                    # Agar pattern topilmasa, asl matnni qo'shish
                    fixed_lines.extend(collected)
                
                i += 1
                continue
        
        fixed_lines.append(line)
        i += 1
    
    return '\n'.join(fixed_lines)

# Faylni o'qish
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Tuzatish
print("⏳ Multi-line f-stringlarni tuzatish...")
fixed_content = fix_multiline_fstrings(content)

# Saqlash
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("✅ Multi-line f-strings fixed!")
print("ℹ️  Iltimos, git diff bilan o'zgarishlarni tekshiring")
