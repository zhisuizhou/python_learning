dic = {}
while True:
    a = input("add or look up a word(a/l/exit)")
    
    if a is "a":
        b = input("type the word :")
        c = input("type the definition :")
        dic[b] = c
        print(dic)
    elif a is "l":
        print(dic)
        d = input("type the word :")
        print(d)
        
        if d in dic :

            print(dic[d])
            
        else :
             print("that word isn't in the dictionary yet")
    elif a == "exit":
        break
    else:
        print("input is wrong, try again")
