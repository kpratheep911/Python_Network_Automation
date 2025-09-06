n = int (input("Which Multiplication table you want ?"))

for count in range(1,21):
    product = n * count
    print(n,"x",count, "=", product)