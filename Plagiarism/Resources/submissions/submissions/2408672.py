def isgetal (n):
    for i in range(0,11):
        if n == str(i):
            return True
        elif i==10:
            return False

           
def convert(number):
    number = str(number)
    if len(number)<1:
        break
    if isgetal (number[0])== True:
        number = convert(number[1:])
        return int(number)
        

