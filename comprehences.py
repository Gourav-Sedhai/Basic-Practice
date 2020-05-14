temps = [222, 334, 423, 434, -66666]

new_temp = [temp / 10 if temp != -66666 else 0 for temp in temps]

print(new_temp)
