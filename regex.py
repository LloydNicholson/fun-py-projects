import re

# patterns = ['term1', 'term2']
email = 'nichlloyd@gmail.com'
email2 = 'jg.1.h@retplanL1ail.com'
email3 = 'j#1m@s.c'

emailpat = r'(\D|[^#$%&*!]+\w+\W*\d*\W*\D)(@)(\w+\d*)(.co.\w+|.com)\b'

match1 = re.match(emailpat, email)
match2 = re.match(emailpat, email2)
match3 = re.match(emailpat, email3)

if match1:
    print(match1)
    print(match1.groups())
    print('Valid email address')
if match2:
    print(match2)
    print(match2.groups())
    print('Valid email address')
if match3:
    print(match3)
    print(match3.groups())
else:
    print('Invalid email')

text = 'This is a string with term1'
text2 = '4 5?R2578 Helsasoaso o4'

# pat = r'(H.+o)([\D])'
#
# match = re.search(pat, text2)
# print(match)
# print(match.groups())
