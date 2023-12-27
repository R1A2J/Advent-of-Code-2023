file = open('puzzle1.txt', 'r')
sum_first, sum_second = 0, 0
for each in file:
    canbeadded, id, red, green, blue = True, int(each[5:each.index(":")]), [], [], []
    while each:
        try:
            analyze = each[:each.index(";")].split() 
        except ValueError:
            analyze = each.split()
        for a in analyze:
            if "red" in a:
                count = int(analyze[analyze.index(a) - 1])
                red.append(count)
                if count > 12:
                    canbeadded = False;
            elif "green" in a:
                count = int(analyze[analyze.index(a) - 1])
                green.append(count)
                if count > 13:
                    canbeadded = False;
            elif "blue" in a:
                count = int(analyze[analyze.index(a) - 1])
                blue.append(count)
                if count > 14:
                    canbeadded = False;
        if ";" in each:
            each = each[(each.index(";") + 1):]
        else:
            each = None
    if canbeadded:
        sum_first += id
    sum_second += max(red) * max(green) * max(blue)
print(sum_first, sum_second) #1853 72706
