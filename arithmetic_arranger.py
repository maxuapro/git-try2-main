list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49"]
list2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
list3 = ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, res=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    new_list = []
    for el in problems:
        new_list.append(el.split(' '))

    for el in new_list:
        if not (el[1] == '+' or el[1] == '-'):
            return "Error: Operator must be '+' or '-'."

        if el[0].isnumeric() == False or el[2].isnumeric() == False:
            return "Error: Numbers must only contain digits."

        if len(el[0]) > 4 or len(el[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if len(el[0]) > len(el[2]):
            el.append(len(el[0]))
            el.append(int(el[0]) + int(el[2])) if el[1] == '+' else el.append(int(el[0]) - int(el[2]))
        else:
            el.append(len(el[2]))
            el.append(int(el[0]) + int(el[2])) if el[1] == '+' else el.append(int(el[0]) - int(el[2]))

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    counter = 1
    for el in new_list:
        counter += 1
        line1 += ' ' * ((el[3] + 2) - len(el[0])) + el[0]
        line1 += '    ' if counter <= len(problems) else ''
        line2 += el[1] + ' ' * ((el[3] + 1) - len(el[2])) + el[2]
        line2 += '    ' if counter <= len(problems) else ''
        line3 += '-' * (el[3] + 2)
        line3 += '    ' if counter <= len(problems) else ''
        line4 += ' ' * (el[3] + 2 - len(str(el[4]))) + str(el[4])
        line4 += '    ' if counter <= len(problems) else ''
    if not res:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3
    else:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4

    return arranged_problems


print(arithmetic_arranger(list, True))
