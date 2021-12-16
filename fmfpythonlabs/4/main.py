import string

print("1) Взяти данні з клавіатури.\n2) Взяти данні з файлу.\n3) Завершити роботу програми. ")

def check_input(input):
    try:
        value = int(input)
        return int(input)
        
    except ValueError:
        try:
            value = float(input)
            print("Помилка.")
            main()
            
        except ValueError:
            print("Помилка. ")
            main()
            
def string_to_list(buff_string):

    return list(buff_string.split(" "))
    
def list_to_string(str_lst):

    str = " "
    return (str.join(str_lst))
    
def add_spaces(buff_string):

    buff_string = ' '.join(buff_string)
    return buff_string
    
def del_letters(buff_string):

    str_lst = string_to_list(buff_string)
    str_lst2 = []
    for i in str_lst:
        temp = ''.join(sorted(set(i), key=i.index))
        str_lst2.append(temp)

    return list_to_string(str_lst2)


def main():

    choice = input('Що робити?:')
    choice = check_input(choice)
    
    if choice == 1:
    
        f_1 = open("out1.txt","w")
        buff_string = str(input("Введіть рядок: "))
        f_1.write("Початковий рядок:\n" + buff_string + "\n")
        buff_string = del_letters(buff_string)
        buff_string = add_spaces(buff_string)
        f_1.write("Результат:\n" + buff_string)
        f_1.close()
        f_1 = open("out1.txt","r")
        output = f_1.read()
        print(output)
        main()
    
    if choice == 2:
    
        f_0 = open("input.txt","r")
        f_2 = open("out2.txt","w")
        buff_string = f_0.read()
        f_2.write("Початковий рядок:\n" + buff_string + "\n")
        buff_string = del_letters(buff_string)
        buff_string = add_spaces(buff_string)
        f_2.write("Результат:\n" + buff_string)
        f_2.close()
        f_2 = open("out2.txt","r")
        output = f_2.read()
        print(output)
        main()
    
    if choice == 3:
    
        print(' ')
        
    if choice != 1 and choice != 2 and choice != 3:
    
            print("Помилка. ")
            main()
    
    
main()

