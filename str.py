while True:
    print("Введите пароль")
    a=str(input())
    if len(a) >= 6 and a.isalnum():# цифры и буквы :
        print("yes")
    else:
        print ("no")
    if a.find ('!',) > 0:
        print('ou')
