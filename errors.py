# print(1)
# int(9)
# int (999)
# print(2)
# print (3)

# a = 1
# b = "2"
# c = 3
# print(int(2.5))
# print(c/0)    

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You are dividing by zero"

print(divide(1,1))
print("End of program")