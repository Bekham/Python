import re

RE_DATE = re.compile(
    r"^[a-z0-9!#$%&\"*+=?^_`{|}~-][a-z0-9!#$%&\"*+=?^_`{|}~\-.]{5,30}(@)[a-z]+(\.)?[a-z]+(\.)[a-z]{2,5}\b$")
email_parse = {}
email = input('Enter your email: ')
try:
    assert RE_DATE.match(email)

except AssertionError:
    print(f'Wrong email {email}')
else:
    email_parse['username'] = RE_DATE.match(email).group(0).split('@')[0]
    email_parse['domain'] = RE_DATE.match(email).group(0).split('@')[1]
    print(f'Correct email! {email_parse}')
