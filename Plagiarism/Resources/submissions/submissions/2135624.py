# write your code hereyear = int(input("Give a year "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print(year, "is a leap year")
        if year % 100 == 0 and year % 400 != 0:
            print(year, "is not a leap year")
    else:
        print(year, "is not a leap year")
else:
    print(year, "is not a leap year")