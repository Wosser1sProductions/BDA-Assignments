# write your code here
year = int(input("geef een jaartal in (in cijfers): "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year), "is a leap year.")
        else:
            print(str(year), "is NOT a leap year.")
    else:
        print(str(year), "is a leap year.")
else:
    print(str(year), "is NOT a leap year.")
