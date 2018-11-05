"""
Модуль з найчастіше використовуваними функціями
"""
def my_sqrt(x):
    """
    Добуває квадратний корінь з числа "x" 
    Приклад у файлі ty.py
    """ 
    return x**0.5
def test_int(x):#
    """
    Перевірка на коректність введених данних(їхня належність до класу int)
    Аргумент-x, як правило число введене користувачем
    Повертає- булеві значення True якщо користувач ввів "правильні данні", Fasle- не коректні 
    Приклад у файлі ty.py
    """ 
    try:
        int(x)
        return True
    except:
        return False
def float_test(X):
        """
    Перевірка на коректність введених данних(їхня належність до класу float)
    Аргумент-x, як правило число введене користувачем
    Повертає- булеві значення True якщо користувач ввів "правильні данні", Fasle- не коректні 
    Приклад у файлі ty.py
    """
        try:
            float(X)
            return True
        except ValueError:
            return False
if __name__=='_main__':
    print("Нестерчук Артем КМ-82 Вариант-14")
    print("Лабораторная робота №1,Завдання 1 ")
    end_of_program = False
    while end_of_program == False:
        while True:                             
            weeks=input("Введите количество недель ")
            month=input("Введите количество месяц месяцев ")
            years=input("Введите количество лет ")
            if float_test(weeks)==False or float_test(month)==False or float_test(years)==False:
                print("Пожалуйста введите цыфры") 
                continue
            else:
                weeks=float(weeks)
                month=float(month)
                years=float(years)
                if weeks <0 or years <0 or month <0 :
                    print("Введите положительные числа")
                    continue 
                else:
                    weeks*=7
                    month*=30
                    years*=365
                    suma=float((weeks+month+years))
                    print(suma)
                    break      
        repeat_program = input ("Введите 1 для завершения ")
        if repeat_program =='1':
            end_of_program = True