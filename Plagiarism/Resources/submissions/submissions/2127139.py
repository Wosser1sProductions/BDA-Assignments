een_cent = int(input("Hoeveel een centjes heb je?"))
twee_cent = int(input('Hoeveel twee centjes heb je?'))
vijf_cent = int(input('Hoeveel vijf centjes heb je?'))
tien_cent = int(input('Hoeveel tien centjes heb je?'))
twintig_cent = int(input('Hoeveel twintig centjes heb je?'))
som = ((een_cent)+(twee_cent*2)+(vijf_cent*5)+(tien_cent*10)+(twintig_cent*20))
som = round(som,2)
print("You have", som, "euro!")
