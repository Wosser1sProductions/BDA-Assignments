# write your code here
amount_of_money=int(input("amount of money"))
coins_2_euro=int(amount_of_money//200)
coins_1_euro=int((amount_of_money%200)//100)
coins_50_cents=int((amount_of_money%100)//50)
coins_20_cents=int((amount_of_money%50)//20)
coins_10_cents=int((amount_of_money%20)//10)
coins_5_cents=int((amount_of_money%10)//5)
coins_2_cents=int((amount_of_money%5)//2)
coins_1_cents=int((amount_of_money%2)//1)

print("2-euros: " + str(coins_2_euro))
print("1-euros: " + str(coins_1_euro))
print("50c-euros: " + str(coins_50_cents))
print("20c-euros: " + str(coins_20_cents))
print("10c-euros: " + str(coins_10_cents))
print("5c-euros: " + str(coins_5_cents))
print("2c-euros: " + str(coins_2_cents))
print("1c-euros: " + str(coins_1_cents))
