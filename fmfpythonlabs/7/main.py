import matplotlib.pyplot as plt
import numpy as np

print("1. Побудова поверхні.\n2. Побудова кривої у просторі.\n3. Побудова графіку функції.\n4. Вихід з програми.")

def check_input_int(input):
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

def get_input():
  left = input("x from : ")
  left = check_input_int(left)
  right = input("to : ")
  right = check_input_int(right)
  dots = input("amout of dots: ")
  dots = check_input_int(dots)

  return left, right, dots

def get_color_surface():
  print("Виберіть колір\n1. viridis\n2. plasma\n3. inferno\n4. magma\n5. cividis")
  color = input()
  color = check_input_int(color)
  colors = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

  return colors[color-1]

def get_color():
  print("Виберіть колір\n1. red\n2. green\n3. blue\n4. gray\n5. black")
  color = input()
  color = check_input_int(color)
  colors = ['red', 'green', 'blue', 'gray', 'black']

  return colors[color-1]



def surface(left, right, dots, color): 
  fig = plt.figure()
  ax = plt.axes(projection="3d")
  x = np.linspace(left, right, num = dots)
  y = np.linspace(left, right, num = dots)
  X, Y = np.meshgrid(x, y)
  Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
  ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                  cmap=color, edgecolor='none')
  plt.show()

def curve(left, right, dots, color):
  fig = plt.figure()
  ax = plt.axes(projection="3d")
  dots = 1/dots
  x = np.arange(left, right, step = dots)
  y =  np.exp(-x) * np.cos(2*np.pi*x)
  z = np.sin(x)
  plt.figure()
  ax.plot3D(x, y, z, color = color)
  plt.show()

def graph(left, right, dots, color):
  dots = 1/dots
  x = np.arange(left, right, step = dots)
  y =  np.exp(-x) * np.cos(2*np.pi*x)
  plt.figure()
  plt.plot(x, y, color = color)
  plt.show()

def main():
  choice = input('Що робити?:')
  choice = check_input_int(choice)

  if choice == 1:
    color = get_color_surface()
    left, right, dots = get_input()
    surface(left, right, dots, color)
    main()

  if choice == 2:
    color = get_color()
    left, right, dots = get_input()
    curve(left, right, dots, color)
    main()

  if choice == 3:
    color = get_color()
    left, right, dots = get_input()
    graph(left, right, dots, color)
    main()


  if choice == 4:
    print("Роботу завершено")

main()
