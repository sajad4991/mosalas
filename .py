a = input("ertefa ro vard konid : ")
a = int(a)
b = input("fasele az divare chghadr bashad : ")
b = int(b)
if b > 60 or b < 50:
    print("to inghad ba hoosh hasti k befahmi bayad 50 o 60 bezani:D rerun kon plz")  
b = int(b)
c = " "
d = "#"
for u in range(a):
    print((b-u)*c,(2*u+1)*d)
