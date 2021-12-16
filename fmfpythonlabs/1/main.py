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
            
def count_words(my_string):

    res = sum([i.strip(string.punctuation).isalpha() for i in my_string.split()])
    return res

def del_spaces(my_string):

    return my_string.split()
    
def add_spaces(my_string):

    my_string = "  ".join(my_string)
    return my_string

def main():

    choice = input('Що робити?:')
    choice = check_input(choice)
    
    if choice == 1:
    
        file3 = open("output1.txt","w")
        my_string = str(input("Введіть рядок: "))
        words = count_words(my_string)
        my_string = del_spaces(my_string)
        my_string = add_spaces(my_string)
        file3.write("Кількість слів: " + str(words) + "\n")
        file3.write(my_string)
        file3.close()
        file3 = open("output1.txt","r")
        output = file3.read()
        print(output)
        main()
    
    if choice == 2:
    
        file1 = open("input.txt","r")
        file2 = open("output2.txt","w")
        my_string = file1.read()
        file2.write("Початковий рядок:\n" + my_string + "\n")
        words = count_words(my_string)
        my_string = del_spaces(my_string)
        my_string = add_spaces(my_string)
        file2.write("Кількість слів: " + str(words) + "\n")
        file2.write(my_string)
        file2.close()
        file2 = open("output2.txt","r")
        output = file2.read()
        print(output)
        main()
    
    if choice == 3:
    
        print(" ")
        
    if choice != 1 and choice != 2 and choice != 3:
    
            print("Помилка. ")
            main()
    
    
main()
