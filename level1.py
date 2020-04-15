ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Method 1

cipherDictionary = {
    'a':'c',
    'b':'d',
    'c':'e',
    'd':'f',
    'e':'g',
    'f':'h',
    'g':'i',
    'h':'j',
    'i':'k',
    'j':'l',
    'k':'m',
    'l':'n',
    'm':'o',
    'n':'p',
    'o':'q',
    'p':'r',
    'q':'s',
    'r':'t',
    's':'u',
    't':'v',
    'u':'w',
    'v':'x',
    'w':'y',
    'x':'z',
    'y':'a',
    'z':'b'
}

plaintext = ''

for character in ciphertext:
    if character in cipherDictionary:
        plaintext += cipherDictionary.get(character)
    else:
        plaintext += character

print(plaintext)

# Method 2

plaintext = ''

for character in ciphertext:
    if character.isalpha():
        distanceFromA = ord(character) - ord('a')
        letterPosition = (distanceFromA + 2) % 26
        plaintext += chr(letterPosition + ord('a'))
    else:
        plaintext += character

print(plaintext)

# Method 3

translationTable = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print('map'.translate(translationTable))
