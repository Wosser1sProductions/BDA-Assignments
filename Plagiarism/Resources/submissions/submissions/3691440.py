amount=int(input())
twoeur=amount//200
oneeur=(amount-twoeur*200)//100
fiftyc=(amount-twoeur*200-oneeur*100)//50
twentyc=(amount-twoeur*200-oneeur*100-fiftyc*50)//20
tenc=(amount-twoeur*200-oneeur*100-fiftyc*50-20*twentyc)//10
fivec=(amount-twoeur*200-oneeur*100-fiftyc*50-20*twentyc-10*tenc)//5
twoc=(amount-twoeur*200-oneeur*100-fiftyc*50-20*twentyc-10*tenc-5*fivec)//2
onec=(amount-twoeur*200-oneeur*100-fiftyc*50-20*twentyc-10*tenc-5*fivec-twoc*2)
print(twoeur)
print(oneeur)
print(fiftyc)
print(twentyc)
print(tenc)
print(fivec)
print(twoc)
print(onec)
