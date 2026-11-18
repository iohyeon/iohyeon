"""Tistory RSS에서 최근 글을 받아 README의 BLOG-POST-LIST 구간을 바꾼다."""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

FEED = "https://develop-tracking.tistory.com/rss"
COUNT = 5
START, END = "<!-- BLOG-POST-LIST:START -->", "<!-- BLOG-POST-LIST:END -->"

req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"})
with urllib.request.urlopen(req, timeout=30) as res:
    root = ET.fromstring(res.read())

items = root.findall("./channel/item")[:COUNT]
if not items:
    sys.exit("RSS에서 글을 찾지 못했습니다")

def escape(title):
    return title.replace("[", "\\[").replace("]", "\\]")

lines = [f"- [{escape(i.findtext('title').strip())}]({i.findtext('link').strip()})" for i in items]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
if not pattern.search(readme):
    sys.exit("README에 BLOG-POST-LIST 표시가 없습니다")
updated = pattern.sub(lambda _: START + "\n" + "\n".join(lines) + "\n" + END, readme)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
print(f"{len(lines)}개 글 반영")
