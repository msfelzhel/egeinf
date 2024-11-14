for x in '0123456789ABCDEFGHI':
    s = int('98897' + x + '21',19) + int('2' + x + '923',19)
    if s%18 == 0:
        print(x,s/18)