"""从 textbook/ 生成大纲目录与汉字统计：python scripts/gen_outline.py v1.19"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TB = os.path.join(ROOT, 'textbook')
ver = sys.argv[1] if len(sys.argv) > 1 else 'dev'
files = sorted(f for f in os.listdir(TB) if f.endswith('.md') and (f.startswith('0') or f.startswith('第')))
files.append('附录_参考来源与官方资料.md')
out = [f'# AI 时代的 FDE · 大纲目录与字数统计（{ver}）', '',
       '> 由 `scripts/gen_outline.py` 从 `textbook/` 自动生成。字数口径：**汉字数**（仅中文字符，不含代码块）。', '']
total = 0
for f in files:
    t = open(os.path.join(TB, f), encoding='utf-8').read()
    body = re.sub(r'```.*?```', '', t, flags=re.S)
    n = len(re.findall(r'[\u4e00-\u9fff]', body))
    total += n
    out.append(f'### 「{f}」  —  汉字约 {n} 字')
    out.append('')
    fence = False
    for line in t.splitlines():
        if line.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,4}) (.+)$', line)
        if m:
            out.append('  ' * (len(m.group(1)) - 1) + '- ' + m.group(2).strip())
    out.append('')
out.insert(4, f'**全书合计：汉字约 {total} 字（{len(files)} 个文件）**')
out.insert(5, '')
p = os.path.join(ROOT, 'misc', f'教材大纲目录_{ver}.md')
open(p, 'w', encoding='utf-8', newline='').write('\n'.join(out).rstrip() + '\n')
print(p, total)
