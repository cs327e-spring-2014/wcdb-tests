#--------------
# makefile.py
#--------------


all:
make XML.zip

clean:
rm -f *.pyc
rm -f RunXML.out
rm -f RunXML.tmp
rm -f TestXML.out
rm -f XML.html
rm -f XML.log
rm -f XML.zip

diff: RunXML.in RunXML.py XML.py
RunXML.py < RunXML.in > RunXML.tmp
diff RunXML.out RunXML.tmp
rm RunXML.tmp

turnin-list:
turnin --list lara cs327epj2

turnin-submit: XML.zip
turnin --submit lara cs327epj2 XML.zip

turnin-verify:
turnin --verify lara cs327epj2

XML.html: XML.py
pydoc -w XML

XML.log:
git log > XML.log

XML.zip: makefile \
             XML.html XML.log XML.py \
             RunXML.in RunXML.out RunXML.py \
             TestXML.py TestXML.out
zip -r XML.zip \
           makefile \
           XML.html XML.log XML.py \
           RunXML.in RunXML.out RunXML.py \
           TestXML.py TestXML.out

RunXML.out: RunXML.in RunXML.py XML.py
RunXML.py < RunXML.in > RunXML.out

TestXML.out: TestXML.py XML.py
TestXML.py >& TestXML.out
