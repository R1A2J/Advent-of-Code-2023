file = open('puzzle1.txt', 'r')
sum_first_puzzle, sum_second_puzzle = 0, 0
lines = file.readlines()
count = {int(each[5:each.index(':')]): 1 for each in lines}
for a in count: 
    count1 = 0
    while count1 != count[a]: 
        matches, worth = 0, 0
        winning_numbers = lines[a - 1][(lines[a - 1].index(':') + 2):lines[a - 1].index("|")].split()
        index = 0
        while index != len(winning_numbers):
            winning_numbers[index] = int(winning_numbers[index])
            index += 1
        numbers = lines[a - 1][(lines[a - 1].index("|") + 1):].split()
        index = 0
        while index != len(numbers):
            numbers[index] = int(numbers[index])
            index += 1
        for c in winning_numbers:
            if c in numbers:
                matches += 1
                if not count1:
                    if not worth:
                        worth += 1
                    else:
                        worth *= 2
        if not count1:
            sum_first_puzzle += worth
            sum_second_puzzle += count[a]
        for b in range(1, matches + 1):
            if (a + b) not in count:
                break
            else:
                count[a + b] += 1
        count1 += 1
print(sum_first_puzzle, sum_second_puzzle) #18653 5921508
