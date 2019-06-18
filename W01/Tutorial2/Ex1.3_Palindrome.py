inp = input('Enter a string: ').lower().replace(' ', '')

mid_id = len(inp) // 2
left = inp[:mid_id]

if len(inp) % 2 == 0:
    right = inp[mid_id:][::-1]
else:
    right = inp[mid_id + 1:][::-1]

if left == right:
    print('Palindrome')
else:
    print('Not a palindrome')
