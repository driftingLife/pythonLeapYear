
def isLeapYear(newYear):
    if newYear % 4 == 0 and newYear % 100 != 0 or newYear % 400 == 0:
        return True
    else:
        return False
    
for i in range(0,3):
    a = input()
    if isLeapYear(int(a)):
        print("The ",a," is leap year.")
    else:
        print("The ",a," isn't leap year.")