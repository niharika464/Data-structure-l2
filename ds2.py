def onsquaretime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("@",end="")
            iteration+=1
        print("")
    print("when n is-",n,"iteration is-",iteration)


onsquaretime(5)
onsquaretime(2)
onsquaretime(6)
onsquaretime(4)
onsquaretime(9)

