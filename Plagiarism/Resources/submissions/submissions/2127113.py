sum = (int(input("Coins of 1? ")) * 1) + (int(input("Coins of 2? ")) * 2) + (int(input("Coins of 3? ")) * 5) + (int(input("Coins of 4? ")) * 10) + (int(input("Coins of 5? ")) * 20)
print("You have ", str(sum // 100), ".", str(sum % 100), " euro!", sep="")

