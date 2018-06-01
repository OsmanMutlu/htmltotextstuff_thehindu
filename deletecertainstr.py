import sys
import codecs
import re
import shutil

filename = sys.argv[1]

#This is the folder containing texts
text_path = re.sub(r"(.*\/)[^\/]*$", r"\g<1>", filename)

#These are the starting lines of the comment section
stoplist = ["ShareArticle","Updated:","MoreIn","SpecialCorrespondent","METRO PLUS","EDUCATION PLUS","PROPERTY PLUS","CINEMA PLUS","DISTRICT PLUS"]

try:
    with codecs.open(filename, "r", "utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    ofilename = re.sub(r".*\/([^\/]*)$", r"\g<1>", filename)
    print("FILE IS EMPTY!!! : " + ofilename)
    with open(text_path + "empty_files","a") as g:
        g.write(ofilename + "\n")
    shutil.move(filename, text_path + "empties/" + ofilename)
    sys.exit()

firsttime = True
for i in range(0,len(lines)):
    firstline = lines[i]
    firstline = re.sub(r"\n|\r", r"", firstline)
    if firsttime:
        if re.search(r"\d{2}:\d{2} IST", firstline):
            firsttime = False
        continue
    else:
        j = i
        n = len(lines)
        while j < n:
            line = re.sub(r"\n|\r| ", r"", lines[j])
            time = re.search(r"\d{2}:\d{2}IST", line)
            if time or any(line == word for word in stoplist):
                del lines[j]
                n = n - 1
                continue
            j = j + 1
        break

if all(len(line)==0 for line in lines) or len(lines) < 2:
    ofilename = re.sub(r".*\/([^\/]*)$", r"\g<1>", filename)
    print("FILE IS EMPTY!!! : " + ofilename)
    with open(text_path + "empty_files","a") as g:
        g.write(ofilename + "\n")
    shutil.move(filename, text_path + "empties/" + ofilename)

else:
    with codecs.open(filename, "w", "utf-8") as f:
        for line in lines:
            if line:
                line = re.sub(r"\n|\r", r"", line)
                f.write(line + "\n")
