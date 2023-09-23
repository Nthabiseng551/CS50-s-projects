from cs50 import get_int

def main():
    height = get_height()
    for i in range(1, height + 1):
        for j in range(i, height):
            print(" ", end="")
        for k in range(1, i + 1):
            print("#", end="")
        print()

def get_height():
    while True:
        n = get_int("Height: ")
        if n >= 1 and n <= 8:
            break
    return n

main()