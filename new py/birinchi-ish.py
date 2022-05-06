# Python bot easy

# function

file = open('index.html','r')
start = file.read()
def fun2():
    inp3=int(input("Misolni yeching 3x3: "))
    if inp3==9:
        print("barakalla 🤗")
    else:
        print("yaxshilab o`rgan ikkichi 😈")
        inp3=int(input("Misolni yeching 3x3: "))
    inp4=int(input("Misolni yeching 3x10: "))
    if inp4==30:
            print("barakalla 🤗")
    else:
        print("yaxshilab o`rgan ikkichi 😈")
        inp4=int(input("Misolni yeching 3x10: "))
    inp5=int(input("Oxirgi savol 50x10: "))
    if inp5==500:
        print("barakalla 🤗")
    else:
        print("yaxshilab o`rgan ikkichi 😈")
    inp6=input("Yutuqqa kodlarni olishni istaysizmi: ").lower()
    if inp6=="ha":
            print(f"Marhamat {start}")
    else:
        print("Bekor qilding ikkichi 😈")
fun2()