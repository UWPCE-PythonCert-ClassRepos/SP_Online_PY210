def print_grid(w, h, n = 5):
    for i in range(h):
        print('+', end='')
        for j in range(w):
          print("-" * n + '+', end='')
        print()
        for i in range(3):
          for j in range(w):
            print("|" + ' ' * n, end='')
          print('|')


    print('+', end='')
    for j in range(w):
      print("-" * n + '+', end='')
    print()

print_grid(5, 5)


