n = input()
a, b = n.split('.')

if a[-1] == '9':
    print('GOTO Vasilisa.')
else:
    print(a if int(b[0]) < 5 else int(a) + 1)
