#!/usr/bin/env python3
import re

with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
i = 0
changes = 0

while i < len(lines):
    line = lines[i]
    
    # Agar print( yoki logger.xxx( bor va keyingi qatorda f" bor bo'lsa
    if ('print(' in line or 'logger.' in line) and not line.strip().endswith(')'):
        # Multi-line bo'lishi mumkin
        collected = [line.rstrip()]
        i += 1
        
        # Keyingi qatorlarni yig'ish
        paren_depth = line.count('(') - line.count(')')
        while i < len(lines) and paren_depth > 0:
            next_line = lines[i]
            collected.append(next_line.rstrip())
            paren_depth += next_line.count('(') - next_line.count(')')
            i += 1
        
        # Yig'ilgan matnni birlashtirib, multi-line f-stringlarni tuzatish
        full = '\n'.join(collected)
        
        # f"...{\n    var}" -> f"...{var}"
        fixed = re.sub(r'f"([^"]*)\{\s+([^}]+)\}', lambda m: f'f"{m.group(1)}{{{m.group(2).strip()}}}', full)
        
        # Agar o'zgarish bo'lsa
        if fixed != full:
            # Indent saqlab, bir qatorga yig'ish
            indent = re.match(r'(\s*)', collected[0]).group(1)
            # Barcha bo'shliqlarni olib tashlash
            oneline = ' '.join(fixed.split())
            fixed_lines.append(indent + oneline + '\n')
            changes += 1
        else:
            fixed_lines.extend([l + '\n' for l in collected])
        
        continue
    
    fixed_lines.append(line)
    i += 1

with open('app.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print(f"✅ {changes} ta multi-line qator tuzatildi")
