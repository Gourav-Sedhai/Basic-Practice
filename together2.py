def func(phrases):
    vars = ("how", "where", "what", "why")
    capitalized = phrases.capitalize()
    if phrases.startswith(vars):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

result = []
while True:
    user = input("Say Something: ")
    if user == "\end":
        break
    else:
        result.append(func(user))

print(" ".join(result))
