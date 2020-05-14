for i in range(0, 5):
    num = 64
    for j in range(0, 2*i+1):
        num=num+1
        ch = chr(num)
        print(ch, end=" ")
    print("\r")