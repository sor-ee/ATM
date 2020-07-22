money = float(input("Enter money with draw : "))
money1 = money//1000
money = money%1000

money2 = money//500
money =money%500

money3 =money//100
money = money%100

print ("Cash B1000 : ",money1)
print ("Cash B500 : ",money2)
print ("Cash B100 : ",money3)

