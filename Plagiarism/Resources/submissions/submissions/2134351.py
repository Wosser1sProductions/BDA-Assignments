amount = int(input("Enter the amount of money to be paid (in eurocents)"))

euro_2 = int(amount/200)
amount = amount - (euro_2* 200)
print("2-euros:", euro_2)
euro_1 = int(amount/100)
amount = amount - (euro_1* 100)
print("1-euros:",euro_1)
cent_50 = int(amount/50)
amount = amount - (cent_50 * 50)
print("50c-euros:",cent_50)
cent_20 = int(amount/20)
amount = amount - (cent_20 * 20)
print("20c-euros:",cent_20)
cent_10 = int(amount/10)
amount = amount - (cent_10 * 10)
print("10c-euros:",cent_10)
cent_5 = int(amount/5)
amount = amount - (cent_5 * 5)
print("5c-euros:",cent_5)
cent_2 = int(amount/2)
amount = amount - (cent_2 * 2)
print("2c-euros:",cent_2)
cent_1 = amount
print("1c-euros:",cent_1)