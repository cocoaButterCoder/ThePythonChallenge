import re, requests

baseURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
response = requests.get(baseURL + '8022')

while True:
    response.raise_for_status

    nextNothingRegex = re.compile(r'\d+')
    matchObject = re.findall(nextNothingRegex, response.text)

    nextNothing = matchObject[-1]
    print(nextNothing)
    response = requests.get(baseURL + nextNothing)
