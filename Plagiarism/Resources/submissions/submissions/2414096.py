injfdkls = input("oke")

def probleem(i,j,oke):
    if i*2>=len(oke) or j*2<=0:
        return ""
    print(oke[i*2:j*2])
    i-=1
    probleem(i,j,oke)
    j-=1
    probleem(i,j,oke)
    
probleem(len(injfdkls)-1,len(injfdkls), injfdkls)
print ("")



