def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def num_check(question, low, high):

    valid = False
    while not valid:

        print()
        error = "Please enter a number that is more than (or equal to) {} and no higher than {}".format(low, high)
        print()

        try:
            # asks user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if low <= response <= high:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)



def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("This program will calculate the factors of any given integer, "
          "along with telling you if it is a prime number or a perfect square")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    print()
    statement_generator('-','-')
    return ""

# Gets factors, returns a sorted list


def get_factors(to_factor):
    # List to hold factors

    factors_list = []

    # Square root to_factor to find 'half-way'

    limit = int(to_factor ** 0.5)

    # Find factor pairs and add to list

    for item in range(1, limit + 1):

        # Check factor is not 1 (unity)

        if to_factor == 1:
            break

        # Check if number is a factor

        result = to_factor % item

        factor_1 = int(to_factor // item)

        # Add factor to a list if it is not already in there

        if result == 0:
            factors_list.append(item)

        if factor_1 != item and result == 0:
            factors_list.append(factor_1)

    # output

    factors_list.sort()

    return (factors_list)



    
 # main routine


statement_generator("Factors Calculator","-")

# Display instructions of user who has not ued the program before
first_time = input("To display instructions, press <enter>, or press any key to continue")

if first_time == "":
    instructions()

keep_going = ""

while keep_going == "":

    comment = ""

    var_to_factor = num_check("Number?", 1, 200)

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # generate heading
    if var_to_factor == 1:
        heading = "One is special..."
    else:
        heading = "factors of {}".format(var_to_factor)

    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")

