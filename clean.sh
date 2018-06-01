#!/bin/sh
#Takes a full path of the html_dir without slash / charachter at the end
HTML_DIR=$1
cd $HTML_DIR
if [ ! -d ../random_boilerpipe_newstext ]; then
 mkdir ../random_boilerpipe_newstext
 mkdir ../random_boilerpipe_newstext/empties
fi
for file in http*
do
 if [ ! -f ../random_boilerpipe_newstext/$file ]; then
#  tmp=$(echo "${file%.cms}.txt")
  python /ai/work/emw/htmltotextstuff_timesofindia/boilerpipe_gettext.py $file
  python3 /ai/work/emw/htmltotextstuff_thehindu/deletecertainstr.py ../random_boilerpipe_newstext/$file
  python3 /ai/work/emw/htmltotextstuff_thehindu/addnewstime.py ../random_boilerpipe_newstext/$file
  python3 /ai/work/emw/htmltotextstuff_thehindu/addnewslink.py ../random_boilerpipe_newstext/$file
  echo "Finished $file"
 fi
done
exit 0
