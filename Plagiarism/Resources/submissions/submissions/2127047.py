eenEurocent = int(input("aantal 1 eurocenten: "))
tweeEurocent = int(input("aantal 2 eurocenten: "))
vijfEurocent = int(input("aantal 5 eurocenten: "))
tienEurocent = int(input("aantal 10 eurocenten: "))
twintigEurocent = int(input("aantal 20 eurocenten: "))

totaal = eenEurocent * 1 + tweeEurocent * 2 + vijfEurocent * 5 + tienEurocent * 10 + twintigEurocent * 20
print("You have", "{:.2f}".format(totaal/100), "euro!")