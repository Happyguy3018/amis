print("Нестерчук Артем КМ-82 Вариант-14")
print("Лабораторная робота №1,Завдання 3 ")
end_of_program = False
while end_of_program == False:
    def test_float(y):
        try:
            float(x)
            return True
        except ValueError:
            return False
    while True:    
        x=input("Введите число х: ")
        if test_float(x)==False:
            print("Введите число")
            continue
        else:
            x=float(x)
            if x>13:
                x=-3/(x+1)
                x=float(x)
            else:
                x=(-x**3)+9
                x=float(x)
            print(x)
            break
    repeat_program = input ("Введите 1 для завершения ")
    if repeat_program =='1':
        end_of_program = True