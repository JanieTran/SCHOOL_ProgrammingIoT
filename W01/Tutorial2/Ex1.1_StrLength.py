str_list = [
    'a',
    'aba',
    'abc',
    'z',
    'xyz',
    'xyzzyx'
]

count = 0

for string in str_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print('The number of strings where the string length ' +
      'is 2 or more and the first and last character: ' + str(count))
