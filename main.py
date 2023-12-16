while True:
    operations = ["+", "-", "/", "*"]
    a=int(input("Введите первое число: "))
    print(f"Список операций:",end=" ")
    print(*operations)
    op=input("Введите операцию: ")
    b=int(input("Введите второе число: "))
