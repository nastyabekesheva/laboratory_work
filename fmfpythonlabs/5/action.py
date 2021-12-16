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
def string_to_list(my_str):
    return list(my_str.split(" "))
    
def list_to_string(my_sl):
    str1 = " "
    return (str1.join(my_sl))

def del_odd(my_str):
    my_sl = string_to_list(my_str)
    for i in range(len(my_sl)):
        if i % 2 != 0:
            my_sl.pop(i)
    return list_to_string(my_sl)
    
def reverse(my_str):
    my_sl1 = []
    my_sl = string_to_list(my_str)
    for i in range(len(my_sl)):
        sl = len(my_sl[i])
        t = my_sl[i][sl::-1]
        my_sl1.append(t)
    return list_to_string(my_sl1)

def action():

    choice = input("Що робити?:")
    choice = check_input(choice)
    
    if choice == 1:
    
        file1 = open("output1.txt","w")
        my_str = str(input("Введіть рядок: "))
        file1.write("Початковий рядок:\n" + my_str + "\n")
        my_str = del_odd(my_str)
        my_str = reverse(my_str)
        
        file1.write("Рядок:\n" + my_str + "\n")
        file1.close()
        file1 = open("output1.txt","r")
        output = file1.read()
        print(output)
        action()
    
    if choice == 2:
    
        file0 = open("input.txt","r")
        file2 = open("output2.txt","w")
        my_str = file0.read()
        file2.write("Початковий рядок:\n" + my_str + "\n")
        my_str = del_odd(my_str)
        my_str = reverse(my_str)

        file2.write("Рядок:\n" + my_str + "\n")
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



