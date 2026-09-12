#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""style-lint.py —— 《AI 时代的 FDE》（FDE-101）格式与体例一致性检查（零依赖）

检查项全部按**本仓库自己的** `AGENTS.md` 第 3 节写，不是照搬任何别的书：
- `#` = 篇标题（仅 00 / 第03 / 第05 / 第10 / 第13 / 第15 章开头）
- `##` = 章标题（`## 第N章 ...`）/ 附录（`## 附录 A：...`）
- `###` = 节（`### N.x ...`）
- 每篇末章有 `### 本篇收尾 · 甲乙方对照：<问题>`（不占编号）——篇末章为 02/04/09/12/14/16
- §3.5 交叉引用写"第N章 N.x"，**禁止**"前文/后文/如上所述"这类模糊指代
- §3.6 **要求**保留"教材提炼 / 信息截至 YYYY 年 MM 月 / 待核验"标注
  → 因此本脚本**不检查、也不允许清理**这些标注（与 FDE-102 的口径相反）

**刻意不检查的**（已评估，属本仓库既有写法而非缺陷）：
- 中英文之间是否加空格：本书写作 `FDE是什么`（不加空格），全书一致，故不设检查项；
  若将来决定改为 `FDE 是什么`，应先全书统一再加检查项。

用法：
    python scripts/style-lint.py        # ERROR 时退出码 1
    python scripts/style-lint.py -v     # 逐条列出明细
"""
from __future__ import print_function

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTBOOK = os.path.join(ROOT, 'textbook')
VERBOSE = '-v' in sys.argv or '--verbose' in sys.argv

# `#` 篇标题允许出现的文件 → 允许个数（AGENTS.md 3.1；00 为书名 + 第一篇共 2 个，附录 1 个总标题）
H1_EXPECT = {
    '00_封面与全书导读.md': 2,
    '第03章_Palantir的平台与FDE体系.md': 1,
    '第05章_Phase1_Discovery.md': 1,
    '第10章_FDE角色体系.md': 1,
    '第13章_中国云服务商的FDE实践图谱.md': 1,
    '第15章_AI_FDE落地_Echo共识与对齐.md': 1,
    '附录_参考来源与官方资料.md': 1,
}
# 每篇末章（应有 `### 本篇收尾`）
SECTION_TAIL = [2, 4, 9, 12, 14, 16]

UNIT_RIGHT = ('月', '日', '年', '小时', '分钟', '次', '人', '台', '卡', '天',
              '周', '季', '千字', '百万', '万', '亿', '元', 's', 'kWh', 'tokens')

ERRORS = []
WARNS = []


def err(f, line, msg):
    ERRORS.append((f, line, msg))


def warn(f, line, msg):
    WARNS.append((f, line, msg))


def strip_noise(t):
    t = re.sub(r'(?ms)^```.*?^```', '\n', t)
    t = re.sub(r'`[^`\n]*`', ' ', t)
    t = re.sub(r'https?://\S+', ' ', t)
    return t


def main():
    if not os.path.isdir(TEXTBOOK):
        print('[FATAL] 找不到 %s' % TEXTBOOK)
        return 2
    files = sorted(f for f in os.listdir(TEXTBOOK) if f.endswith('.md'))
    if not files:
        print('[FATAL] textbook/ 下没有 markdown 文件')
        return 2

    for f in files:
        raw = io.open(os.path.join(TEXTBOOK, f), encoding='utf-8').read()
        lines = raw.split('\n')
        prose = strip_noise(raw)
        m = re.match(r'第(\d+)章', f)
        ch = int(m.group(1)) if m else 0

        # 1. 引号口径（硬约束）：一律半角 "，mermaid 内用 &quot;
        #    原因：正文要复用进课件 PPT，全角引号在 PPT 文本框与生成链路里会出问题
        for i, l in enumerate(lines, 1):
            if re.search(r'[“”‘’「」]', l):
                err(f, i, '全角/弯引号——一律半角 "（mermaid 内用 &quot;）：%s' % l.strip()[:34])

        # 2. 章标题：第NN章_*.md 必须含 `## 第N章`，编号与文件名一致
        if ch:
            got = re.findall(r'(?m)^##\s+第\s*(\d+)\s*章\s', raw)
            if len(got) != 1:
                err(f, 0, '应有且仅有 1 个 `## 第%d章` 标题，实际 %d 个' % (ch, len(got)))
            elif int(got[0]) != ch:
                err(f, 0, '章标题编号 %s 与文件名 第%d章 不一致' % (got[0], ch))

        # 3. `#` 篇标题只允许出现在指定文件，且个数固定
        h1 = re.findall(r'(?m)^#\s+(.+)$', raw)
        if f in H1_EXPECT:
            if len(h1) != H1_EXPECT[f]:
                err(f, 0, '篇标题 `#` 应为 %d 个，实际 %d 个' % (H1_EXPECT[f], len(h1)))
        elif h1:
            err(f, 0, '不该有 `#` 篇标题（AGENTS.md 3.1 限指定文件），实际 %d 个：%s'
                % (len(h1), h1[0][:30]))

        # 4. `### 本篇收尾` 只在每篇末章，且篇末章必须有
        n_tail = len(re.findall(r'(?m)^###\s*本篇收尾', raw))
        if ch in SECTION_TAIL and n_tail != 1:
            err(f, 0, '本篇末章应有 1 个 `### 本篇收尾`，实际 %d 个' % n_tail)
        if ch and ch not in SECTION_TAIL and n_tail:
            err(f, 0, '非篇末章不应有 `### 本篇收尾`')

        # 5. `### N.x` 编号连续（仅章节文件）
        if ch:
            nums = [int(x) for x in re.findall(r'(?m)^###\s+%d\.(\d+)\s' % ch, raw)]
            if nums and nums != list(range(1, len(nums) + 1)):
                err(f, 0, '小节编号不连续：%s' % nums)

        # 6. mermaid 图与图题一一配对
        n_mer = len(re.findall(r'(?m)^```mermaid', raw))
        n_cap = len(re.findall(r'(?m)^\*图\s*%d-\d+' % ch, raw)) if ch else len(re.findall(r'(?m)^\*图\s', raw))
        if n_mer != n_cap:
            err(f, 0, 'mermaid 图 %d 张，图题 %d 条——每张图都要带 `*图 N-x：标题*`' % (n_mer, n_cap))

        # 7. 裸代码块
        for i, l in enumerate(lines, 1):
            if re.match(r'^```\s*$', l):
                before = sum(1 for x in lines[:i - 1] if re.match(r'^```', x))
                if before % 2 == 0:
                    err(f, i, '裸代码块（未标语言）')

        # 8/9. 连续 Alert / 嵌套 Alert
        for i in range(len(lines) - 1):
            if re.match(r'^> \[!\w+\]\s*$', lines[i]) and re.match(r'^> \[!\w+\]', lines[i + 1]):
                err(f, i + 1, '连续 Alert 标记（渲染为空框）')
        for i, l in enumerate(lines, 1):
            if re.match(r'^> > \[!\w+\]', l):
                err(f, i, '嵌套 Alert：%s' % l.strip()[:32])

        # 10. 单位被空格拆坏（只有真带空格才算错）
        for mt in re.finditer(r'\d+\s*元\s*/\s*月', prose):
            if ' / ' in mt.group(0):
                err(f, 0, '价格单位被拆开：%s' % mt.group(0))
        for mt in re.finditer(r'tokens?\s*/\s*(日|次|s)\b', prose):
            if ' / ' in mt.group(0):
                err(f, 0, '单位被拆开：%s' % mt.group(0))

        # 11. 文件尾
        if not raw.endswith('\n'):
            err(f, len(lines), '文件末尾缺换行')
        elif raw.endswith('\n\n'):
            err(f, len(lines), '文件末尾多余空行')

        # 12. `- [ ]` 前必须有空行
        for i, l in enumerate(lines, 1):
            if re.match(r'^- \[ \]', l):
                prev = lines[i - 2] if i >= 2 else ''
                if prev.strip() and not re.match(r'^[-*]|\d+\.|^\s', prev):
                    err(f, i, '复选框列表前缺空行（会渲染成纯文本）')

        # 13. 混合分隔链（可判定的除外：单位 / 路径 / 比例）
        TOKEN = r'[\u4e00-\u9fffA-Za-z0-9][\u4e00-\u9fffA-Za-z0-9.+#%\-]*'
        for mt in re.finditer(r'(?<![\w/])(' + TOKEN + r'(?:\s*/\s*' + TOKEN + r')+)(?![\w/])', prose):
            c = mt.group(1)
            if ' / ' in c and re.search(r'\S/\S', c):
                items = re.split(r'\s*/\s*', c)
                if any(it in UNIT_RIGHT for it in items):
                    continue
                warn(f, 0, '混合链（同一串里 / 与 " / " 并存）：%s' % c)

        # 15. 嵌套子列表缩进 2 空格（应 4）
        for i, l in enumerate(lines, 1):
            if re.match(r'^  \d+\.\s', l) and not re.match(r'^    ', l):
                warn(f, i, '疑似嵌套子列表只缩进 2 空格（应 4 空格）')

        # 16. 引用块内"依赖版面"的指代
        for i, l in enumerate(lines, 1):
            if l.startswith('>') and re.search(r'见上表|见下表|见上图|见下图|如上图|如上表|如下图所示|见右图|见左图', l):
                warn(f, i, '引用块内依赖版面的指代：%s' % l.strip()[:40])

        # 17. 模糊指代（本仓库 AGENTS.md 3.5 明令禁止：交叉引用要写"第N章 N.x"）
        for i, l in enumerate(lines, 1):
            mt = re.search(r'前文|后文|如上所述|详见上文|见下文|如前所述', l)
            if mt:
                warn(f, i, '模糊指代「%s」（3.5 要求写"第N章 N.x"）：%s' % (mt.group(0), l.strip()[:44]))

        # 18. 章号后的空格全/半角混用（`第1章　X` 用了全角空格 U+3000）
        for i, l in enumerate(lines, 1):
            if re.search(r'第\d+章\u3000', l):
                warn(f, i, '章号后用了全角空格（全书其余处为半角空格）：%s' % l.strip()[:40])

    def show(title, items):
        print('=' * 74)
        print('%s：%d' % (title, len(items)))
        print('=' * 74)
        if not items:
            return
        shown = items if VERBOSE else items[:30]
        for f, line, msg in shown:
            print('  %-42s L%-5s %s' % (f[:42], line or '-', msg))
        if len(items) > len(shown):
            print('  … 另有 %d 条（用 -v 看全部）' % (len(items) - len(shown)))

    show('ERROR（必须修）', ERRORS)
    print()
    show('WARN（建议修）', WARNS)
    print()
    if ERRORS:
        print('✗ 体例检查未通过：%d 个 ERROR' % len(ERRORS))
        return 1
    print('✓ 体例检查通过（0 ERROR，%d WARN）' % len(WARNS))
    return 0


if __name__ == '__main__':
    sys.exit(main())
