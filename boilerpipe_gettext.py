from boilerpipe.extract import Extractor
import sys
import codecs

filename = sys.argv[1]

path = "../random_boilerpipe_newstext/"

with open(filename, "rb") as f:
    data = f.read()

extractor = Extractor(extractor='ArticleExtractor', html=data)

extracted_text = extractor.getText()

with codecs.open(path + filename, "w", "utf-8") as g:
    g.write(extracted_text)
