def get_answer():
    answer = input("What is the capital of California?")
    answer = str.lower(answer)
    return answer


def main():
    capital = get_answer()
    if capital != "sacramento":
        print("That is incorrect, please check your spelling and try again!")
        main()
    else:
        print("Correct! The answer is Sacramento")

main()