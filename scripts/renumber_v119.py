"""v1.19 一次性重编号：原第14/15/16章 → 第16/17/18章（单遍映射，避免连锁替换）。
用法：python scripts/renumber_v119.py [--dry]
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = '--dry' in sys.argv
MAP = {'14': '16', '15': '17', '16': '18'}
RENAME = {
    '第14章_中国区FDE转型的六大挑战与应对.md': '第16章_中国区FDE转型的六大挑战与应对.md',
    '第15章_AI_FDE落地_Echo共识与对齐.md': '第17章_AI_FDE落地_Echo共识与对齐.md',
    '第16章_AI_FDE落地_Delta技术与场景.md': '第18章_AI_FDE落地_Delta技术与场景.md',
}

def m(n):
    return MAP.get(n, n)

RULES = [
    # 章号区间（先于单章号处理）
    (re.compile(r'第( ?)13( ?)[–-]( ?)14( ?)章'), lambda g: f'第{g[1]}13{g[2]}–{g[3]}16{g[4]}章'),
    (re.compile(r'第( ?)15( ?)[–-]( ?)16( ?)章'), lambda g: f'第{g[1]}17{g[2]}–{g[3]}18{g[4]}章'),
    (re.compile(r'第( ?)(0?1)( ?)[–-]( ?)16( ?)章'), lambda g: f'第{g[1]}{g[2]}{g[3]}–{g[4]}18{g[5]}章'),
    (re.compile(r'第15/16章'), lambda g: '第17/18章'),
    # 文件名
    (re.compile(r'第(1[4-6])章_'), lambda g: f'第{m(g[1])}章_'),
    # 单章号
    (re.compile(r'第( ?)(1[4-6])( ?)章'), lambda g: f'第{g[1]}{m(g[2])}{g[3]}章'),
    # 图号
    (re.compile(r'图( ?)(1[4-6])-(\d)'), lambda g: f'图{g[1]}{m(g[2])}-{g[3]}'),
    # 节号 N.x(.y)：排除百分比与"万"
    (re.compile(r'(?<![\d.])(1[4-6])\.(\d+)(?!\d)(?!\s*[%万])'), lambda g: f'{m(g[1])}.{g[2]}'),
]

TARGETS = [os.path.join('textbook', f) for f in os.listdir(os.path.join(ROOT, 'textbook')) if f.endswith('.md')]
TARGETS += ['README.md', 'index.md', 'mkdocs.yml']

def apply(text, section_rule=True):
    total = 0
    for i, (rx, fn) in enumerate(RULES):
        if not section_rule and i == len(RULES) - 1:
            continue
        text, n = rx.subn(lambda mo: fn([mo.group(0)] + list(mo.groups())), text)
        total += n
    return text, total

grand = 0
for rel in TARGETS:
    p = os.path.join(ROOT, rel)
    src = open(p, encoding='utf-8').read()
    # mkdocs.yml 无节号，只替换章号/文件名
    new, n = apply(src, section_rule=not rel.endswith('.yml'))
    grand += n
    if n:
        print(f'{n:4d}  {rel}')
        if not DRY:
            open(p, 'w', encoding='utf-8', newline='').write(new)

if not DRY:
    tb = os.path.join(ROOT, 'textbook')
    for old, new in RENAME.items():
        os.rename(os.path.join(tb, old), os.path.join(tb, new))
print('total', grand, '(dry)' if DRY else '')
