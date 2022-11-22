
while True:
    a = input("Loginni kiritng: ")
    b = input("Parolni kiriting: ")
    if a == "Ibrohim" and b == "123":
        print("Dasturga kirdingiz")
        break
    elif a != 'Ibrohim':
        print("Login xato")
    elif b != '123':
        print("Parol noto'g'ri")
    else:
        print("Xatolik")
        