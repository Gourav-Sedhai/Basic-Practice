# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()
import time
import os

while True:
    if os.path.exists("f/fruit.txt"):
        with open("f/fruit.txt") as file:
            print(file.read())
    else:
        print("Doesnot exist")
    time.sleep(3)