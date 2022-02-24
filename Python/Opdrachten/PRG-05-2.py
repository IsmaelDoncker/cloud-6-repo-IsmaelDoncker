x= 0
while x != 100:
    
    x = input("Please enter a number:")
    x= int(x)
    if x > 100:
        print(f"{x} That is high")
    elif x == 100:
        print(f"{x} nice")
        break
    else :
        print(f"{x} That is low")
