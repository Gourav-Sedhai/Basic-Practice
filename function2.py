def we_cond(temp):
    if temp > 7:
        return 'warm'
    else:
        return 'cold'

tem = float((input("Enter temperature:")))
print(we_cond(tem))