def get_choice():
    print("The menu includes: Chicken, Steak, Lobster.")
    choice = input("Which single item would you prefer?")
    return choice


def main():
    meal = get_choice()
    meal = str.lower(meal)
    if meal == "steak" or meal == "chicken" or meal == "lobster":
        print("You selected " + meal + ", Excellent Choice!")
    else:
        print("You selected an item that is not offered, please check your spelling!")
        main()


main()