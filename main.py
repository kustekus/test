while True:
    operations = ["+", "-", "/", "*"]
    a=int(input("Введите первое число: "))
    print(f"Список операций:",end=" ")
    print(*operations)
    op=input("Введите операцию: ")
    b=int(input("Введите второе число: "))

    if op == operations[0]:
        rez = a + b
    elif op == operations[0]:
        rez = a - b
    elif op == operations[0]:
        rez = a / b
    elif op == operations[0]:
        rez = a * b
    else:
        print("Выбрана неверная операция, попробуйте снова")
        continue
