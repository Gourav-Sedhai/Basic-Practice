# defining function
def maker(phrase):
    some = ("how", "why", "what")
    # to capitalize the first letter we use function capitalize()
    capitalized = phrase.capitalize()
    # if we want to use ? after sentence we use return"bracket?".format variablename and startswith is a function
    if phrase.startswith(some):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

# to store  the input given by user
results = []
while True:
    user = input("Say something: ")
    if user == "\end":
        break
    else:
        # append is used to join the inputs
        # to capitalize we used maker function
        results.append(maker(user))

# to join the output we used " ".join by 1 space 
print(" ".join(results))
