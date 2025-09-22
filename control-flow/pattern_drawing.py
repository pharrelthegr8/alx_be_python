length = int(input("Enter the size of the pattern: "))

x = 0
while x < length:
    for i in range(length):
        print("*", end="")
    print() #simply outputs a newline and moves the cursor to the next line.
    x += 1
