import sys
import codecs
import re

filename = sys.argv[1]

#Adding the news link to the end of file

try:
    with codecs.open(filename, "r", "utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    sys.exit()

match = re.search(r"\/([^\/]*)$", filename)
if match:
    link = re.sub(r"___", r"://", match.group(1))
else:
    link = re.sub(r"___", r"://", filename)

link = re.sub(r"_", r"/", link)
lines.append("url : " + link)

with codecs.open(filename, "w", "utf-8") as f:
    for line in lines:
        line = re.sub(r"\n|\r", r"", line)
        f.write(line + "\n")
