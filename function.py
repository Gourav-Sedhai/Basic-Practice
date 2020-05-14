def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temp = [2, 3, 3, 1, 1]
student_grades = {"Raman":3, "vaman":3, "Param":3}
print (mean(monday_temp))