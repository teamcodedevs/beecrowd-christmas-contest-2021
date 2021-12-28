from sys import stdin

list_gift = {}
for l in stdin:
    input_line = l.rstrip()
    if input_line and input_line != '-- --':
        items = input_line.split()
        if len(items) == 1:
            gift = list_gift.get(input_line)
            if not gift:
                print('404 not found\n')
            else:
                print(f'Child: {input_line}\nGift {gift}\n')
        else:
            name, gift = items
            list_gift[name] = gift
