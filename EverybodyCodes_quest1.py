filename = '/Users/sanderarmus/Kool/EverybodyCodes/everybody_codes_e2024_q01_p3.txt'
with open(filename, 'r') as file: 
    tähed = file.read()
#tähed = input("sisesta tähed")
i=2
vastus=0
potions = {"A":0, "B":1, "C":3, "D":5, "x":0}
while i < ((len(tähed))):
    kolmik=[tähed[i], tähed[i-1], tähed[i-2]]
    j=0
    xarv=0
    while j<(len(kolmik)):
        if(kolmik[j]=="x"):
            xarv+=1
        j+=1
    if xarv==2:
        vastus += (potions[(tähed[i])])+(potions[(tähed[i-1])])+(potions[(tähed[i-2])])
        print (vastus)
    elif xarv==1:
        vastus += (potions[(tähed[i])])+(potions[(tähed[i-1])])+(potions[(tähed[i-2])] + 2)
        print(vastus)
    elif xarv ==0:
        vastus += (potions[(tähed[i])])+(potions[(tähed[i-1])])+(potions[(tähed[i-2])] + 6)
        print(vastus)
    else:
        vastus+=0
    i+=3
print (vastus)
        


