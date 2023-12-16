import random
while True:
    a=random.randint(1,100)
    b=random.randint(1,100)
    operations=["+","-"]
    op=random.choice(operations)
    if op=="+":
        rez=a+b
        otv=int(input(f"Чему равно: {a} + {b}? "))
    else:
        rez=a-b
        otv=int(input(f"Чему равно: {a} - {b}? "))
    if otv==rez:
        print("Ответ верный!")
    else:
        print("Ответ неверный!")
