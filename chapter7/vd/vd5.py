while True:
    print()
    password=input()
    if len(password)<8:
        print("khong hop le!")
    if password.isalnum() or password.lower():
        break
    print()