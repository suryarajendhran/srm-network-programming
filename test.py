num = raw_input("Enter appropriate input:")
#program 1
# num = input("Enter a number")
# square = num*num
# if square > 99:
#     print square
#     print "Big"
# elif (square>49) & (square<100):
#     print square
#     print "Medium"
# else:
#     print "Too small to bother with"
# A 100-91
# B 90-81
# C 80-71
# D 70-61
# E 60-51
# F <50
#program 2
# def grade(input):
#     if(input > 90):
#         return "A"
#     elif(input < 91 and input > 80):
#         return "B"
#     elif(input < 81 and input > 70):
#         return "C"
#     elif(input < 71 and input > 60):
#         return "D"
#     elif(input < 61 and input > 49):
#         return "E"
#     else:
#         return "F"

# name = raw_input("Enter name: ")
# year_of_study = int(input("Enter year of study: "))
# mark_1 = int(input("Enter the mark in first subject: "))
# mark_2 = int(input("Enter the mark in second subject: "))
# grade_1 = grade(mark_1)
# grade_2 = grade(mark_2)
# print "\nName: ", name
# print "Year of study: ", year_of_study
# print "Grade in first subject: ", grade_1
# print "Grade in second subject: ", grade_2


#progam 3
# def func(inputlist):
#     newlist = list()
#     for inputItem in inputlist:
#         if inputItem in newlist:
#             print "already present"
#         else:
#             newlist.append(inputItem)
#     return newlist
# inputlist = {2:1, 4:0, 3:0, 4:1, 2:1, 4:5, 3:0}
# print(func(list(inputlist.keys())))

#program 4
#Incorrect code:
# def factorial(num, fact):
#     if num < 1:
#         return fact
#         print('fact returned')
#     else:
#         fact = fact*num
#         print('num=',num)
#         print('fact=',fact)
#         factorial(num-1, fact)
#Correct code:
# def factorial(num):
#    return 1 if num<1 else num * factorial(num-1)
#print(factorial(num))

#program 5
#splitstring = list()
#splitstring = num.replace(',',' ').replace('_',' ').replace('.',' ').split()
#print 'Split strings are:', splitstring

#program 4
def findDivisorSum(data):
    divisorSum=0
    for i in range(1,data):
        if data%i  is 0:
            divisorSum = divisorSum + i
    #print 'Divisor sum is ', divisorSum
    if divisorSum==data: #note: Did not return true when using 'is' for '=='
        return True
    else:
        return False
print findDivisorSum(int(num))









































