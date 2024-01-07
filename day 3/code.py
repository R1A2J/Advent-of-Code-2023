file = open('puzzle1.txt', 'r')
lines = file.readlines()
line0, line1, line2, sum1, sum2 = None, lines[0], lines[1], 0, 0

def checking_before(index, number, line):
    global a
    while (index + a) >= 0 and line[index + a].isdigit():
        number += pow(10, (abs(a) - 1)) * int(line[index + a]) 
        a -= 1
    return number

def checking_after(index, number, line):
    global a
    while (index + a) < len(line) and line[index + a].isdigit():
        number = number * 10 + int(line[index + a])
        a += 1
    return number

while True:
    index = 0
    for char in line1:
        if (ord(char) != 46) and (ord(char) != 10) and ((ord(char) < 48) or (ord(char) > 57)): #identifies a symbol
            count = []
            if line0:
                a = -1
                number = checking_before(index, 0, line0)
                a = 0
                b = checking_after(index, number, line0)
                if b:
                    count.append(b)
                    sum1 += b
                if not a:
                    a = 1
                    b = checking_after(index, 0, line0)
                    if b: 
                        count.append(b)
                        sum1 += b
            a = -1
            b = checking_before(index, 0, line1)
            if b:
                count.append(b)
                sum1 += b
            a = 1
            b = checking_after(index, 0, line1)
            if b:
                count.append(b)
                sum1 += b
            if line2:
                a = -1
                number = checking_before(index, 0, line2)
                a = 0
                b = checking_after(index, number, line2)
                if b:
                    count.append(b)
                    sum1 += b
                if not a:
                    a = 1
                    b = checking_after(index, 0, line2)
                    if b: 
                        count.append(b)
                        sum1 += b
            if len(count) == 2:
                c = 1
                for a in count:
                    c *= a
                sum2 += c
        index += 1
    line0, line1 = line1, line2
    if not line1:
        break
    else:
        if lines.index(line1) == (len(lines) - 1):
            line2 = None
        else:
            line2 = lines[lines.index(line1) + 1]

print(sum1, sum2) #539713 84159075
