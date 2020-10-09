#!/usr/bin/python3
"""
Small utility script which counts the articles listed in the readme.
"""

counter = [0]
with open('README.md') as f:
    # Skip TOC
    for line in f:
        if line[:4] == "## 1":
            break
    section = 0
    for line in f:
        if line[0] == '-':
            counter[section] += 1
        elif line[:3] == "## ":
            section += 1
            counter.append(0)

total = 0
for (i, c) in enumerate(counter):
    total += c
    print(f"Section #{i+1} contains {c:2} article{'s' if  c!=1 else ''}.")
print(f"---------- Total of {total:2} articles.")
