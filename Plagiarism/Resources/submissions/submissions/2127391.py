response1 = int(input("How many coins of one eurocent do you have ?"))
r1 = int(response1)
response2 = int(input("How many coins of two eurocent do you have? "))
r2 = int(response2)
response3 = int(input("How many coins of five eurocent do you have ?"))
r3 = int(response3)
response4 = int(input("How many coins of ten eurocent do you have ?"))
r4 = int(response4)
response5 = int(input("How many conins of twenty eurocent do you have ?"))
r5 = int(response5)
Total = r1*0.01 + r2*0.02 + r3*0.05 + r4*0.1 + r5*0.2
print("You have ", Total, "euro!", sep="")