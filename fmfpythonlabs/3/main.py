import string

print("1) Данні з клавіатури.\n2) Данні з файлу.\n3) Завершити роботу програми. ")

def check_input(input):
    try:
        value = int(input)
        return int(input)
        
    except ValueError:
        try:
            value = float(input)
            print("Помилка.")
            action()
            
        except ValueError:
            print("Помилка. ")
            action()
def string_to_list(my_string):
    return list(my_string.split(" "))
    
def list_to_string(my_sl):
    str1 = " "
    return (str1.join(my_sl))

def del_ka(my_string):
    ka = 0
    my_sl = string_to_list(my_string)
    for i in range(len(my_sl)):
        if "ka" in my_sl[i]:
            my_sl[i] = ''
            ka += 1
    return list_to_string(my_sl), ka

def del_ak(my_string):
    ak = 0
    my_sl = string_to_list(my_string)
    for i in range(len(my_sl)):
        if "ak" in my_sl[i]:
            my_sl[i] = ''
            ak += 1
    return list_to_string(my_sl), ak

def action():

    choice = input("Що робити?:")
    choice = check_input(choice)
    
    if choice == 1:
    
        file1 = open("output1.txt","w")
        my_string = str(input("Введіть рядок: "))
        file1.write("Початковий рядок:\n" + my_string + "\n")
        my_string, ka = del_ka(my_string)
        my_string, ak = del_ak(my_string)
        file1.write("Рядок:\n" + my_string + "\n")
        file1.write("Кількість ітерацій з \'ka\': " + str(ka) + "\n")
        file1.write("Кількість ітерацій з \'ak\': " + str(ak) + "\n")
        file1.close()
        file1 = open("output1.txt","r")
        output = file1.read()
        print(output)
        action()
    
    if choice == 2:
    
        file0 = open("input.txt","r")
        file2 = open("output2.txt","w")
        my_string = file0.read()
        file2.write("Початковий рядок:\n" + my_string + "\n")
        my_string, ka = del_ka(my_string)
        my_string, ak = del_ak(my_string)
        file2.write("Рядок:\n" + my_string + "\n")
        file2.write("Кількість ітерацій з \'ka\': " + str(ka) + "\n")
        file2.write("Кількість ітерацій з \'ak\': " + str(ak) + "\n")
        file2.close()
        file2 = open("output2.txt","r")
        output = file2.read()
        print(output)
        action()
    
    if choice == 3:
    
        print(" ")
        
    if choice != 1 and choice != 2 and choice != 3:
    
            print("Помилка. ")
            action()
    
    
action()


