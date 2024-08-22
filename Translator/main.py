def translate(phrase):
    output = ""
    for i in phrase:
        if i in "AEIOUaeiou":
            if i.isupper():
                output = output + "G"
            else:
                output = output + "g"
        else:
            output = output + i
    return output

print(translate(input("Enter your phrase: ")))