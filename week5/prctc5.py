__author__ = 'gizemakkus'
import re
text="test is% 30$ 2.15 +5.123 -2.15"
pat= "\d+"
print re.findall(pat,text)