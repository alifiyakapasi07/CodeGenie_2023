class GuessTheNumber:
    
    def get_actual_number(final_number, operations):
        ans = final_number

        for i in range(len(operations)-1, -1, -1):  # list in reverse order, from the last element to the first element (-1,-1)

            s = operations[i]   #sets the variable s to the string value of the current operation.
            
            num = int(s[4:])    #represents the second operand of the multiplication operation in "X * 5"
                                #The int() function is then used to convert this string "5" to the integer value 5

            op = s[2]           #if s is the string "X * 5", then op would be assigned the character "*".

            # Some Exception Cases
            if op == '/' and num == 0:
                return -1
            if (op == '*' and num == 0) or (op == '^' and num == 0) or op == '%':
                return -2

            # Operation applied
            if op == '+':
                ans -= num
            elif op == '*':
                ans /= num
            elif op == '-':
                ans += num
            elif op == '/':
                ans *= num
            else:
                ans = int(ans ** (1 / num))

        return ans


if __name__ == '__main__':
    final_number = 2500
    operations = ["X + 10", "X - 5", "X * 5", "X ^ 2"]

    actual_number = GuessTheNumber.get_actual_number(final_number, operations)
    print( actual_number)
