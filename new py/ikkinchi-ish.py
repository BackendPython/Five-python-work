turn = 1
while turn == 1:
    inp1=int(input("Birinchi sonni kiriting: "))
    inp2=int(input("Ikkinchi sonni kiriting: "))
    q=input("Amalni kiriting: ")
    if q=="+":
        print(f"Natijangiz: {inp1+inp2}")
    elif q=="-":
        print(f"Natijangiz: {inp1-inp2}")
    elif q=="*":
        print(f"Natijangiz: {inp1*inp2}")
    elif q=="/":
        print(f"Natijangiz: {inp1/inp2}")
    else:
        print(f"'{q}' bu amal mavjud emas!")
    turn=0
    quest=input("Davom etsizmi: ").lower()
    if quest=="ha":
        turn=1
    elif quest=="":
        print("Iltimos biror ma`lumot kriting")
        quest=input("Davom etsizmi: ").lower()
    elif quest=="yoq":
        turn=0
        print("Hisoblash tugadi")
    else:
        print(f"O`zing '{quest}' san")