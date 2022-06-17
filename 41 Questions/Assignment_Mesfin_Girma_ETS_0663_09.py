                    #        ADVANCED PROGRAMMING ASSIGNMENT 1
                    # =============================================================
                    #              
                    # WRITTEN BY: Mesfin Girma
                    # ID: ETS0663/09
                    # SECTION:C
                    # SUBMITTED TO:Mr.EYOB
                    # SUBMISSION DATE:MAY,2022
                    # ============================================================
# How to execute and see the function in action ?
    #all functions have a Try method at the bottom just uncomment this functions one at atime and run the program
    #After execution press control plus z and recomment it so that you can latter execute another function


# Question 1:---------------
#  Write an int method cube() that returns the cube of the value inserted


def cube(num):
    return num*num*num
def Try_Cube():
    print("Questin NO 1\n")
    num = int(input("Enter an integer:  "))  
    print('the cube of a number = ',cube(num))
#Try_Cube() #uncomment this to see the function in action and recomment it after execution 


#Question 2: -------------------------------
# Write a float method triangle() that computes the area of a triangle using its two formal
#parameters h and W where h is the height and w is the length of the base of the traingle

def Triangle_area(w,h):
    return 0.5*w*h
def Try_Triangle_area():
    print("Questin NO 2\n")
    w= float(input('enter length of triangle\n'))
    h= float(input('enter the height of triangle \n')) 
    print('Area of triangle = ',(Triangle_area(w,h)) )

#Try_Triangle_area() #uncomment this to see the function in action and recomment it after execution 


#Question 3: ----------------------------------
# Write a float method rectangle() that computes and returns the area of a rectangle using its two
#float formal parameters h and w, where h is the height and w is the width of the rectangle

def Rectangle_Area(w,h):
    return 0.5*w*h
def Try_Rectangle_Area():
    print("Questin NO 3\n")
    w= float(input('enter length of triangle\n'))
    h= float(input('enter the height of triangle \n')) 
    print('Area of triangle = ',(Rectangle_Area(w,h)) )
#Try_Rectangle_Area() #uncomment this to see the function in action and recomment it after execution 



#Question 4: --------------------------------

#the formula for a line is normally gives as y=mx+b, write a method Line() that expects three float
#parameters, slope m, a y-intercept b, and an x-coordinate x, the method computes the y-coordinate assoiated
#with the line specified by m and b at x-coordinate.
def line(m,b,x):
    return m*b+x
def Try_line():
    print("Questin NO 4\n")
    m= float(input('Enter slope\n'))
    b= float(input('Enter y intercept\n')) 
    x= float(input('Enter X coordinate\n'))
    print('Y-Coordinate is = ',(line(m,b,x)) )
#Try_line() #uncomment this to see the function in action and recomment it after execution 


#Question 5:**********************************
#Write a method Intersect() with four float parameters m1,b1,m1,b2 the parameters come conceptuall in two paris
#The first pair contains the coefficients describing one line, the second pair contains coefficients describing a second line, The method
#returns 1 if te two line intersect,otherwise it should return 0;

def Intersect(m1,b1,m2,b2):
    x = (b2 - b1) / (m1 - m2)
    y1 = m1 * x + b1
    y2 = m2 * x + b2
    if (y1 == y2):
        return 1
    else:
        return 0
#How to use it
def Try_Intersect():
    print("Questin NO 5")
    m1 = float(input('insert the m1 coefficient of line 1:'))
    b1 = float(input('insert the b1 coefficient of line 1:'))
    m2 = float(input('insert the m2 coefficient of line 2:'))
    b2 = float(input('insert the b2 coefficient of line 2:'))
    if(Intersect(m1,b1,m2,b2)==1):
        print("the two lies intersect")
    else:
        print("the two lines do not intersect")
#Try_Intersect() #uncomment this to see the function in action and recomment it after execution 


#Question 6: *********************************
#pending......
def Factorial():
    print("Questin NO 6\n")
    # To take input from the user
    num = int(input("Enter a number: "))

    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    print("The factorial of",num,"is",factorial)
def Try_Factorial():
    Factorial()
#Try_Factorial() #uncomment this to see the function in action and recomment it after execution 


#Question 7: *********************************
#Write another program that accepts a number from the user and returns the Fibonacci value
#of thet number. you should use recursion in here

def Fibonacci(n):
	if n<=1:
		return n
	else:
		return(Fibonacci(n-1) + Fibonacci(n-2))

def Try_Fibonacci():
    print("Questin NO 7 \n")
    n = int(input('Enter a number, N, where N>=2 : '))

    fibo_series = []

    for i in range(0,n):
        fibo_series.append(Fibonacci(i))
        
    print("The Fibonacci Series Associeted to the number ", n ," is :" , fibo_series)
#Try_Fibonacci() #uncomment this to see the function in action and recomment it after execution 



#Question 8: ***********************************************************************
#Write a program to find the following
  # a, Prime number checking
  # b, Sum of digit

def CheckIfPrime(num):
    if num < 1:
        print('its not a prime number')
    else:
        for i in range(2, num):
            if (num % i == 0):
                return " :Prime"
            else:
                return " :not Prime"
def SumOfDegit(num):
    sum = 0
    while num > 0: 
        digit = num % 10
        sum = sum + digit
        num = num // 10
    return sum

def Try_PrimeCheck_And_SumOfDigit():
    print("Questin NO 8 \n")
    num = int(input('insert the number for prime check and sum of its digits:'))
    print("The number is", CheckIfPrime(num), "\nAnd the sum of its Digit is ",  SumOfDegit(num))

#Try_PrimeCheck_And_SumOfDigit() #uncomment this to see the function in action and recomment it after execution 


#Question 9: ***********************************************************************
# Write a program to arrange the numbers in ascending order

def OrderInAscending(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def Try_OrderInAscending():
    print("Questin NO 9 \n")
    arr = []
    x = int(input('Enter the amount of numbers to insert:'))
    for k in range(x):
        num = int(input('Enter num ' +  str(k+1) + " and press Enter: "))
        arr.append(num)

    temp = 0
    print("Elements of original array: " , arr)
    print("\nElements of array sorted in ascending order: ", OrderInAscending(arr))
#Try_OrderInAscending() #uncomment this to see the function in action and recomment it after execution 


#Question 10: ***********************************************************************
#TRIANGLE AREA

def StudentMark(size, score):
    counter = 0
    for j in range(size):
        if (score[j] > 20):
            counter = counter + 1
    return counter
def Try_StudentMark():
    print("Questin NO 10 \n")
    size = int(input('Enter the number of the students you need for calc:'))
    score = []
    for i in range(size):
        num = int(input('Enter student ' +  str(i+1) + " score3 and press Enter: "))
        score.append(num)
    print('Number of students that scored above 20 is ', StudentMark(size, score))
#Try_StudentMark() #uncomment this to see the function in action and recomment it after execution 

#RECTANGLE AREA

#Question 11: ***********************************************************************

def cellphone():
    print("Questin NO 11 \n")
    contact_number = int(input("enter the 9 digit contact number==>"))
    if (contact_number // 100000000 == 0 or contact_number // 100000000 > 9):
        print('Invalid Input')
    elif (contact_number // 100000000 == 9):
        print("mobile")
    else:
        print("fixed phone")

def Try_cellPhone():
    cellphone()

#Try_cellPhone() #uncomment this to see the function in action and recomment it after execution 


#Question 12: ***********************************************************************
def max_min():
    print("Questin NO 12 \n")
    siz = int(input('Enter the size of the list of numbers you need for calc:'))
    numlist = []

    for i in range(siz):
        num = int(input("write the numbers one-by-one:"))
        numlist.append(num)
    min = max = numlist[0]
    for i in range(siz):
        if (numlist[i] > max):
            max = numlist[i]
        if (numlist[i] < min):
            min = numlist[i]
    print('Maximum in the list==> ', max)
    print('Minimum in the list==> ', min)
def Try_max_min():
    max_min()
#Try_max_min()  #uncomment this to see the function in action and recomment it after execution 

#Question 13: ***********************************************************************

def reverse():
    print("Questin NO 13 \n")
    num = int(input("enter the number that is goining to be reversed:"))
    rev = 0
    while (num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    print('reversed number is: ', rev)

def Try_Reverse():
    reverse()

#Try_Reverse()  #uncomment this to see the function in action and recomment it after execution 

#Question 14: ***********************************************************************

def gcd():
    print("Questin NO 14 \n")
    n1 = int(input('enter the first number : '))
    n2 = int(input('enter the second number :'))
    if n1 > n2:
        small = n2
    else:
        small = n1
    for i in range(1, small + 1):
        if ((n1 % i == 0) and (n2 % i == 0)):
            gcd = i

    print("the GCD of the two numbers==>", gcd)

def Try_Gcd():
    gcd()
#Try_Reverse()  #uncomment this to see the function in action and recomment it after execution 

#Question 15: ***********************************************************************

def lcm():
    print("Questin NO 15 \n")
    n1 = int(input('enter the first number : '))
    n2 = int(input('enter the second number :'))
    for i in range(1, n1 * n2 + 1):
        if ((i % n1 == 0) and (i % n2 == 0)):
            print("the LCM of the two numbers==>", i)
            break
def Try_lcm():
    lcm()
#Try_lcm()  #uncomment this to see the function in action and recomment it after execution 


#Question 16: ***********************************************************************

def frac_sum():
    print("Questin NO 16 \n")
    sum = 0
    for i in range(1, 99, 2):
        x = i / (i + 2)
        sum = sum + x
        print(x)
    print("the sum of the fraction is ==> ", sum)
def Try_frac_sum():
    frac_sum()
#Try_frac_sum()  #uncomment this to see the function in action and recomment it after execution 

#Question 17: ***********************************************************************

def isbn():
    print("Questin NO 17 \n")
    dig9 = int(input('ENTER A 9 DIGIT NUMBER ONLY: '))
    original_dig9 = dig9
    arr = []
    if ((dig9 // 100000000) > 9 or (dig9 // 10000000 == 0)):
        print("Invalid number please enter a 9 digit number")
    else:
        for i in range(9):
            digit = dig9 % 10
            dig9 = dig9 // 10
            arr.append(digit)
    checksum = 0
    for i in range(9):
        a = arr[i] * (9 - i)
        checksum = checksum + a
    checksum = checksum % 11
    display = ((original_dig9 * 10) + checksum) - (arr[8] * 1000000000)
    print("the ISBN of the entered number is ==>", arr[8], end="")
    print(display, end="")
def Try_isbn():
    isbn()
#Try_isbn()  #uncomment this to see the function in action and recomment it after execution 
import math

#Question 18: ***********************************************************************

def exp():
    print("Questin NO 18 \n")
    x = int(input('enter the value of x for e^x =>'))
    sum = 0
    for i in range(15):
        a = x**i / math.factorial(i)
        sum = sum + a

    print(sum)
def Try_exp():
    exp()
#Try_isbn()  #uncomment this to see the function in action and recomment it after execution 


#Question 19: ***********************************************************************

def leap():
    print("Questin NO 19 \n")
    year = 2001
    leap = []
    while year <= 2100:
        if year % 4 == 0:
            leap.append(year)
        year = year + 1

    for i in range(25):
        if i % 10 == 0:
            print(leap[i])
        else:
            print(leap[i], end=" ")
def Try_leap():
    leap()
#Try_leap()  #uncomment this to see the function in action and recomment it after execution 


#Question 20: ***********************************************************************

def maxoccurence():
    print("Questin NO 20 \n")
    x = int(input('enter the number of students: '))
    student = []
    for i in range(x):
        score = int(input('Enter the numbers to find max and its occurence :'))
        student.append(score)
    i = 0
    max = student[0]
    while i < x:
        if (student[i] > max):
            max = student[i]
        i = i + 1

    j = 0
    counter = 0
    while j < x:
        if (student[j] == max):
            counter = counter + 1
        j = j + 1

    print("The maximum of the numbers' is ", max)
    print("it occurs ", counter, " times")

def Try_maxoccurence():
    maxoccurence()
#Try_maxoccurence()  #uncomment this to see the function in action and recomment it after execution 


#Question 21: ***********************************************************************

def cube_of_digits():
    print("Questin NO 21 \n")
    low = 100
    high = 1000
    for a in range(low, high):
        sum = 0
        test = a
        while test > 0:
            digit = test % 10
            test = test // 10
            cube = digit**3
            sum += cube
        if a == sum:
            print(a)
def Try_cube_of_digits():
    cube_of_digits()
#Try_cube_of_digits()  #uncomment this to see the function in action and recomment it after execution 

#Question 22: ***********************************************************************

def No_of_digit():
    print("Questin NO 22 \n")
    counter = 0
    num = 1
    while 1 == 1:
        num = int(
            input(
                'Enter a positive integer(negative number terminates) to find its number of digits'
            ))
        if (num < 0):
            print("loop terminated negative number entered")
            break
        else:
            counter = 0
            while (num > 0):
                digit = num % 10
                num = num // 10
                counter = counter + 1
            print(counter)
def Try_No_of_digit():
    No_of_digit()
#Try_No_of_digit()  #uncomment this to see the function in action and recomment it after execution 


#Question 23: ***********************************************************************

def No_of_prime():
    print("Questin NO 23 \n")
    counter = 0
    n = int(
        input("enter the maximum restriction to the prime number searching "))
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            counter += 1

    print("the number of prime numbers= ", counter)
def Try_No_of_prime():
    No_of_prime()
#Try_No_of_prime()  #uncomment this to see the function in action and recomment it after execution 

#Question 24: ***********************************************************************

def perfect_number():
    print("Questin NO 24 \n")
    sum = 0
    n = int(input("enter the number that you want to check perfection: "))
    arr = []
    for x in range(1, n):
        if n % x == 0:
            sum += x
            arr.append(x)
    if sum == n:
        print("its a perfect number ")
        print("its divisors", arr)
    else:
        print("its not a perfect number")

def Try_perfect_number():
    perfect_number()
#Try_perfect_number()  #uncomment this to see the function in action and recomment it after execution 

#Question 25: ***********************************************************************
def t_comp():
    print("Questin NO 25 \n")
    counterpos = 0
    counterneg = 0
    sum = 0
    average = 0
    while 1 == 1:
        num = int(
            input("Enter an int value,program exits if the input is zero "))
        if (num > 0):
            counterpos += 1
            sum = sum + num
        elif (num < 0):
            counterneg += 1
            sum = sum + num
        else:
            break
    average = (sum) / (counterpos + counterneg)
    print("the number of positives is", counterpos)
    print("the number of negatives is", counterpos)
    print("the total is", sum)
    print("the average is", average)

def Try_t_comp():
    t_comp()
#Try_t_comp() #uncomment this to see the function in action and recomment it after execution 

#Question 26: ***********************************************************************
def tuition():
    print("Questin NO 26 \n")
    initial_tuition = 10000.0
    sum = 0.0
    for i in range(1, 11):
        after_years = initial_tuition * 1.05
        initial_tuition = after_years
    print("after ten years tuition", initial_tuition)
    sum = initial_tuition
    for j in range(1, 5):
        initial_tuition = initial_tuition * 1.05
        sum = sum + initial_tuition
    print("four years tuition 10 years after ward==> ", sum)
def Try_tuition():
    tuition()
#Try_tuition() #uncomment this to see the function in action and recomment it after execution 

#Question 27: ***********************************************************************
def conversion():
    print("Questin NO 27 \n")
    print("1.kilograms to pounds")
    print("2.miles to kilometers")
    print("3.hour to minutes")
    N = int(input("Enter the conversion type:"))

    if (N == 1):
        kilo = float(input("Enter the kilogram amount:"))
        pound = 2.20462 * kilo
        print(kilo, "kilograms=", pound, "pounds")
    elif (N == 2):
        mile = float(input("Enter the amount of miles:"))
        kilometers = 1.60934 * mile
        print(mile, "miles=", kilometers, "kilometers")
    elif (N == 3):
        hours = float(input("Enter the amount of hours:"))
        minutes = 60 * hours
        print(hours, "hours=", minutes, "minutes")
    else:
        print("Invalid number entered")
    
def Try_conversion():
    conversion()
#Try_conversion() #uncomment this to see the function in action and recomment it after execution 


#Question 28: ***********************************************************************
def student():
    print("Questin NO 28 \n")
    size = int(input('Enter the number of students: '))
    student = []
    for i in range(size):
        name = input("Enter the name of students: ")
        score = int(input("Enter the score of the student: "))
        student.append(name)
        student.append(score)
    max1 = student[1]
    for j in range(1, 2 * size, 2):
        if (student[j] > max1):
            max1 = student[j]
            name = student[j - 1]
    max2 = 0
    for k in range(1, 2 * size, 2):
        if (student[k] != max1):
            if (student[k] > max2):
                max2 = student[k]
                name2 = student[k - 1]
    print("1st place The name of the student is ", name, " and it scores:",
          max1)
    print("2nd place The name of the student is ", name2, " and it scores:",
          max2)
def Try_student():
    student()
#Try_conversion() #uncomment this to see the function in action and recomment it after execution 


#Question 29: ***********************************************************************
def stu():
    print("Questin NO 29 \n")
    size = int(input('Enter the number of students: '))
    student = []
    for i in range(size):
        name = input("Enter the name of students: ")
        score = int(input("Enter the score of the student: "))
        student.append(name)
        student.append(score)
    max = student[1]
    for j in range(1, 2 * size, 2):
        if (student[j] > max):
            max = student[j]
            name = student[j - 1]
    print("1st place The name of the student is ", name, " and it scores:",
          max)
def Try_stu():
    stu()
#Try_stu() #uncomment this to see the function in action and recomment it after execution 
      
#Question 30: ***********************************************************************

def fivesix():
    print("Questin NO 30 \n")
    num = 100
    five_six = []
    while num <= 200:
        if ((num % 5 == 0) or (num % 6 == 0)):
            if (num % 30 != 0):
                five_six.append(num)
    num = num + 1

    for i in range(len(five_six)):
        if i % 10 == 0:
            print(five_six[i])
        else:
            print(five_six[i], end=" ")
def Try_fivesix():
    fivesix()
#Try_fivesix() #uncomment this to see the function in action and recomment it after execution 
      
#Question 31: ***********************************************************************
def ascii():
    print("Questin NO 31 \n")
    i = 1
    while i < 127 - 32:
        result = chr(i + 32)

        if i % 10 == 0:
            print(result)
        else:
            print(result, end=' ')

        i = i + 1
def Try_ascii():
    ascii()
#Try_ascii() #uncomment this to see the function in action and recomment it after execution 
      
#Question 32: ***********************************************************************
#A
def right_tri():
    print("Questin NO 32 \n")
    rows = 6
    for i in range(1, rows + 1):
        for space in range(1, (rows - i)):
            print(" ", end="")
        for symbol in range(i, 0, -1):
            print("{0}".format(symbol), end="")

        print()
def Try_right_tri():
    right_tri()
#Try_right_tri() #uncomment this to see the function in action and recomment it after execution 

#B
def upside():
    print("Questin NO 32B \n")
    rows = 6
    for i in range(1, rows + 2):
        for space in range(1, i + 2):
            print(" ", end="")
        for symbol in range(1, rows - i + 2):
            print("{0}".format(symbol), end="")
        print()
def Try_upside():
    upside()
#Try_upside() #uncomment this to see the function in action and recomment it after execution 

#Question 33: ***********************************************************************

def right_en_left():
    print("Questin NO 33 \n")
    num = int(input("Enter the amount of the row from 1-15:"))
    if (num < 1 or num > 15):
        print("Invalid Number please enter a number between 1 to 15")
    else:
        for i in range(1, num + 1):
            for j in range(1, num - i + 1):
                print(end=" ")
            for j in range(i, 0, -1):
                print(j, end="")
            for j in range(2, i + 1):
                print(j, end="")
            print()
def Try_right_en_left():
    right_en_left()
#Try_right_en_left() #uncomment this to see the function in action and recomment it after execution 

#Question 34: ***********************************************************************
def pow2pyramid():
    print("Questin NO 34 \n")
    lines = []
    for i in range(1, 9):
        lines.append([str(2**j) for j in range(i)])

    b = len(lines[-1])
    buffers = [len(x) for x in lines[-1]]

    for line in lines:
        l = len(line)
        line = [" "] * (b - len(line)) + line
        out = []
        for x, y in zip(line, buffers):
            out.append(x.rjust(y))
        print(" ".join(out + out[::-1][1:]))
def Try_pow2pyramid():
    pow2pyramid()
#Try_pow2pyramid() #uncomment this to see the function in action and recomment it after execution 


#Question 35: ***********************************************************************

def Loan():
    print("Questin NO 35 \n")
    loanAmount = int(input("Enter loan amount:"))
    numberOfYears = int(input("Enter number of years: "))
    annualInterestRate = 5000.0
    print("Interest Rate", "     ", "Monthly Payment", "      ",
          "Total Payment")
    while (annualInterestRate <= 8000.0):
        monthlyInterestRate = (annualInterestRate / 1000) / 1200
        monthlyPayment = (
            loanAmount * monthlyInterestRate /
            (1 - 1 / math.pow(1 + monthlyInterestRate, numberOfYears * 12)) *
            10)
        totalPayment = (monthlyPayment * numberOfYears * 12)
        print((annualInterestRate / 1000), "      ", monthlyPayment, "      ",
              totalPayment)
        annualInterestRate = annualInterestRate + 125.0
def Try_Loan():
    Loan()
#Try_Loan() #uncomment this to see the function in action and recomment it after execution 

#Question 36: ***********************************************************************
def hexadec():
    print("Questin NO 36 \n")
    num = int(input("enter the decimal numbet to convert it to hexa decimal:"))
    conversion_table = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    hexadecimal = ''
    while (num > 0):
        remainder = num % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        num = num // 16

    print("The hexadecimal form of", num, "is", hexadecimal)
def Try_hexadec():
    hexadec()
#Try_hexadec() #uncomment this to see the function in action and recomment it after execution 

#Question 37: ***********************************************************************
def e():
    print("Questin NO 37 \n")
    sum = 0
    for i in range(15):
        a = 1 / math.factorial(i)
        sum = sum + a
    print("e=", sum)
def Try_e():
    e()

#Try_e() #uncomment this to see the function in action and recomment it after execution 

#Question 38: ***********************************************************************
def prim():
    print("Questin NO 38 \n")
    num3 = int(input('insert the number for prime check:'))

    if num3 < 1:
        print('its not a prime number')
    else:
        for i in range(2, num3):
            if (num3 % i == 0):
                print('its not a prime number')
                break
            else:
                print('its a prime number')
                break
def Try_prim():
    prim()
#Try_prim() #uncomment this to see the function in action and recomment it after execution 

#Question 39: ***********************************************************************
def even():
    print("Questin NO 39 \n")
    num = int(input("Enter the number to check evenity:"))
    if num < 0:
        print(" The number is zero or negative")
    else:
        if (num % 2 == 0):
            print("its even")
        else:
            print('its not even, odd number')
def Try_even():
    even()
#Try_even() #uncomment this to see the function in action and recomment it after execution 

#Question 40: ***********************************************************************
def calculator():
    print("Questin NO 40 \n")
    def sum():
        print('Sum is ', num1 + num2)

    def product():
        print('Product is ', num1 * num2)

    def quoitient():
        if (num2 != 0):
            print('quoitient is ', num1 / num2)
        else:
            print('Division by zero not possible')

    def difference():
        print('Difference is ', num1 - num2)

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    print('1.Addition')
    print('2.Multiplication')
    print('3.Division')
    print('4.Subtraction')
    op = int(input('Select operation:'))

    if op <= 0 or op > 4:
        print('please enter a valid number')
    else:
        if (op == 1):
            sum()
        elif (op == 2):
            product()
        elif (op == 3):
            quoitient()
        else:
            difference()
def Try_calculator():
    calculator()
#Try_calculator() #uncomment this to see the function in action and recomment it after execution 

#Question 41: ***********************************************************************

def fact_sum():
    print("Questin NO 41 \n")
    x = int(input('Enter the limit of the summation: '))
    pro = 1
    sum = 0
    for i in range(1, x + 1):
        pro = i * pro
        sum = sum + pro
    print(sum)
def Try_fact_sum():
    fact_sum()
#Try_fact_sum() #uncomment this to see the function in action and recomment it after execution 


# =============================================================
#              END OF CODE
# ============================================================