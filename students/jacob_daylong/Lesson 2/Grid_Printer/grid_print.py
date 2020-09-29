#Grid Printer

print("grid_print manual")
print(("+ " + "- " * 4) + "+ " + "- " * 4 + "+")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print(("+ " + "- " * 4) + "+ " + "- " * 4 + "+")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print("| " + "  " * 4 + "| " + "  " * 4 + "|")
print(("+ " + "- " * 4) + "+ " + "- " * 4 + "+")
print()


def grid_print(n):
        i=0
        print(("+ " + "- " * n) + "+ " + "- " * n + "+")
        while i < n:
         print("| " + "  " * n + "| " + "  " * n + "|")
         i += 1
        print(("+ " + "- " * n) + "+ " + "- " * n + "+")
        i=0
        while i < n:
         print("| " + "  " * n + "| " + "  " * n + "|")
         i += 1
        print(("+ " + "- " * n) + "+ " + "- " * n + "+")


print("grid_print(10)")
grid_print(10)
print()

def grid_print2(n, m):
    i = 0
    while i < n:
        print(n * (("+ " + "- " * m))+ "+")
        x = 0
        while x < m:
            print(n * ("| " + "  " * m )+"|")
            x += 1
        i += 1
    print(n * (("+ " + "- " * m))+ "+")

print("grid_print2(4,4)")
grid_print2(4,4)