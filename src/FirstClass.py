print("=================================================================")
print("My Friends")
print("=================================================================")

list_of_friends = ["vaibhav", "manu", "mack"]
list_of_perks = ["choclates", "cards", "pen", "tennis ball"]
print(list_of_friends)

print(str(2) + list_of_friends[0])


def give_perks(friend):
    print("Hello " + friend)
    index = list_of_friends.index(friend)
    friends_with_perks = [(list_of_friends[index], list_of_perks[index])]
    print(friends_with_perks)


give_perks("vaibhav")
give_perks("mack")
print("=================================================================")
print("=================================================================")


def cube(number):
    return number * number * number


def square(number):
    return number * number


print(cube(3))
print("=================================================================")
print("=================================================================")


def print_values(_function, _num):
    if _function == "cube":
        print("Cube of " + str(_num) + " is:" + str(cube(_num)))
    elif _function == "square":
        print("Square of " + str(_num) + " is:" + str(square(_num)))
    else:
        print("No function \"" + _function + "\" defined")


function = "cube"
num = 10
print_values(function, num)

function = "square"
num = 5
print_values(function, num)

function = "quadruple"
num = 4
print_values(function, num)

print("=================================================================")

print("draft language")
print("Change Vovels -> letter 'g'")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
