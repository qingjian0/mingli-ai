# -*- coding: utf-8 -*-
# 修复脚本

with open('app/knowledge/data/meihua/meihua_yishu.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有中文引号
content = content.replace('"', "'")
content = content.replace('"', "'")

with open('app/knowledge/data/meihua/meihua_yishu.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 已修复')
