

while True:
    try:

        age = int(input("Enter your age: "))

        if age > 0:
            break
        else:
            print("you gotta be joking")

    except ValueError:
        print("stop messing around")

match age:
    case age if age <=12:
        print("Child")
    case age if age <=19:
        print("Teenager")
    case age if age <=59:
        print("Adult")
    case age if age >= 60:
        print("Senior")