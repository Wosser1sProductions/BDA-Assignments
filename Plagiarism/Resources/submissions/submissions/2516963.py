var_n = input("n")
var_m = input("m")

varvorige = ""

def maaksubsets(varvorige,var_n,var_m):
    for i in range (1, var_n):
        varvorige += str(i)
        if len(varvorige) <= (var_m*2)-1:
            maaksubsets(varvorige,i,var_m)
        if len(varvorige)==(var_m*2)-1:
            print (varvorige)
maaksubsets(varvorige,int(var_n),int(var_m))