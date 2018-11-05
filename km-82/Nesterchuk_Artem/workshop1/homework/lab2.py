print("Нестерчук Артем КМ-82 Вариант-14")
print("Лабораторная робота №1,Завдання 2 ")
end_of_program = False
while end_of_program == False:
    def test_int(x):
        try:
            int(x)
            return True
        except:
            return False
    while True:
        petals=input("Enter number of petals: ")
        if test_int(petals)==False:
            print("Введите число а если ввели то целое")
            continue
        else:
            petals=int(petals)
            if petals<0:
                print("Введите положительное число")
                continue
            else:
                if petals//2:
                    print("Поздравляю тебя любят")
                    break
                else:
                    print(":(")
                    break
    repeat_program = input ("Введите 1 для завершения ")
    if repeat_program =='1':
        end_of_program = True