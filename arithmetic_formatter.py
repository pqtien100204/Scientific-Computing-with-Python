import re
def arithmetic_arranger(problems, answer = False):
    if len(problems) > 5:
        return "Error: Too many problems"
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
#Errors in problems
    for problem in problems:
#Specifying element in a problem
        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if firstNumber.isdigit() and secondNumber.isdigit():
            pass
        else:
            return "Error: Numbers must only contain digits."
        
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        
        try:
            firstNumber.isdigit() == False
            secondNumber.isdigit() == False
        except:
            return "Error: Numbers must only contain digits."

        if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error: Numbers cannot be more than four digits."
#The optional part of solving problems
        sum = ""
        if operator == "+":
            sum = str(int(firstNumber) + int(secondNumber))
        elif operator == "-":
            sum = str(int(firstNumber) - int(secondNumber))
#Arranging arithmetic problems
        length = max(len(firstNumber), len(secondNumber)) #to know to width of the display which takes the longest number in a problem
    #The rjust() method will right align the string, using a specified character (space is default) as the fill character. string.rjust(length, character)
        width = length + 2
        top_line = str(firstNumber).rjust(width + 1)
        second_line = operator.rjust(2) + str(secondNumber).rjust(width - 1)
        line = ""
        result = str(sum).rjust(width + 1)
        for dash in range(width): #The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
            line += "-"
#Arranging problems       
        if problem != problems[-1]: #Python list index -1 returns the last element of the list.
            first += top_line + '    '
            second += second_line + '    '
            lines += line + '    ' 
            sumx += result + '    '
        else:
            first += top_line
            second += second_line
            lines += line
            sumx += result
#Solve problem or not
    if answer == True:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else: 
        string = first + "\n" + second + "\n" + lines
    return string
    

print(arithmetic_arranger(['1 + 2', '123 + 494849']))