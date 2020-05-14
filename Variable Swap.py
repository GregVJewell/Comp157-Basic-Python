if __name__ == '__main__':
    number = 5
    name = "Greg"

    print("Number is %i & Name is %s" % (number, name))

    temp = name
    name = number
    number = temp

    print("\nNumber is now %s & Name is now %i" % (number, name))