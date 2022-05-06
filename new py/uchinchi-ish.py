def fun():
    sorov = input("salom deb yozing: ")
    if sorov=="salom":
        print('salom deb yozdingiz 😜')
    if sorov!="salom":
        print('salom deb yozmadingiz 🤬')
        sorov = input("salom deb yozing: ")
fun()