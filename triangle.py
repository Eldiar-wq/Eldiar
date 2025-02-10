a = int(input("Бірінші қабырғаны енгізіңіз: "))
b = int(input("Екінші қабырғаны енгізіңіз: "))
c = int(input("Үшінші қабырғаны енгізіңіз: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Теңқабырғалы үшбұрыш")
    elif a == b or a == c or b == c:
        print("Теңбүйірлі үшбұрыш")
    else:
        print("Әртүрлі қабырғалы үшбұрыш")
else:
    print("Мұндай үшбұрыш жоқ!")
