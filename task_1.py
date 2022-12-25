s = 'Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян\n'
with open('test.txt', 'w') as f:
    f.write(s)

with open('test.txt', 'a') as f:
    f.write(s)

with open('test.txt') as f:
    for line in f:
        print(line, end='')
