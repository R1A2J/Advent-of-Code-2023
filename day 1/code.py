file = open('puzzle1.txt', 'r')
sum_first_puzzle, sum_second_puzzle = 0, 0
digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
for each in file:
    digits_in_text_forward, digits_in_text_reverse, index = [], [], 0
    while all([type(d) == str for d in digits_in_text_forward]) and index < len(each):
        for digit in digits:
            if each[index:(index + len(str(digit)))] == str(digit):
                digits_in_text_forward.append(digit)
                break
        index += 1
    index = len(each) - 1
    while all([type(d) == str for d in digits_in_text_reverse]) and index >= 0:
        for digit in digits:
            if each[index:(index + len(str(digit)))] == str(digit):
                digits_in_text_reverse.append(digit)
                break
        index -= 1
    if digits_in_text_forward:
        if type(digits_in_text_forward[-1]) == int:
            sum_first_puzzle += digits_in_text_forward[-1] * 10 + digits_in_text_reverse[-1]
        sum_second_puzzle += digits[digits_in_text_forward[0]] * 10 + digits[digits_in_text_reverse[0]]
print(sum_first_puzzle, sum_second_puzzle) #54159, 53866
