# functions


# add func
# input: 2 variables x and y
# return: the addition of the two variables
def add(x, y):
    addition = float(x) + float(y)
    return addition


# multiply func
# input: 2 variables x and y
# output: teh multiplication of x and y
def mult(x, y):
    return float(x) * float(y)


# divide function
# input: 2 variables x and y
# output: the division of x and y
def div(x, y):
    return float(x) / float(y)


# subtract function
# input: 2 variables x and y
# calls add with x and the negative of y
def subs(x, y):
    return add(x, mult(y, -1))


def main():
    # code for the calculator
    q = 'y'

    # while loop to keep going until the user wants to stop
    while q == 'y':
        print('enter 2 numbers to do math on!! ')

        a = input('Enter the first number: ')
        b = input('Enter the second number: ')

        words = {'a': add(float(a), float(b)), 'x': mult(float(a), float(b)),
                 'd': div(float(a), float(b)), 's': subs(float(a), float(b))}

        func = str(input('what function to run? a: add, x: mult, d: divide, s: subtract \n'))

        # while loop to make sure the input one of a, s, d, x only
        # if it is then break else keep looping until the correct var is entered
        # if the correct input is already entered then print the answer
        while func not in ('a', 'd', 's', 'x'):
            func = str(input('please enter from these options: a: add, x: mult, d: divide, s: subtract \n'))

        print(words[func])

        # end of the while loop to make sure the user doesn't want to quit
        q = input('Do you want to keep going? (y or n) ')


if __name__ == "__main__":
    main()
