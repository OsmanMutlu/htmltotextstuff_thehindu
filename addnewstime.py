import sys
import codecs
import re
import lxml.html
from fuzzywuzzy import fuzz

stoplist = ["METRO PLUS","EDUCATION PLUS","PROPERTY PLUS","CINEMA PLUS","DISTRICT PLUS"]

filename = sys.argv[1]

try:
    with codecs.open(filename, "r", "utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    sys.exit()

text_path = re.sub(r"(.*\/)[^\/]*$", r"\g<1>", filename)

hfilename = re.sub(r".*\/([^\/]*)$", r"\g<1>", filename)

with codecs.open(hfilename, "rb", "utf-8") as g:
    html_file = g.read()

doc = str(html_file)
place = re.search(r'var datelineStr\s*=\s*"([^"]*)"', doc)

if place:
    place = place.group(1)

doc = lxml.html.document_fromstring(html_file)
title = doc.xpath("//h1[@class='artcl-nm-stky-text']/text()")

if not place:
    place = doc.xpath("//meta[contains(@property,'section')]/@content")
    place = str(place[0])

if not title:
    title = doc.xpath("//title/text()")

if title:
    title = re.sub(r"\n|\r", r"", str(title[0]))

    if not any(fuzz.ratio(title,line)>70 for line in lines):
        lines.insert(0,title)
else:
    with codecs.open(text_path + "no_title", "a", "utf-8") as h:
        h.write(re.sub(r".*\/([^\/]*)$", r"\g<1>", filename))

if place:
    place = re.sub(r"\n|\r", r"", place)
    if place in stoplist:
        lines.insert(0,place)

with codecs.open(filename, "w", "utf-8") as f:
    for line in lines:
        if line:
            line = re.sub(r"\n|\r", r"", line)
            f.write(line + "\n")
