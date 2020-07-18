# It has been Told to me that
# python functions can be passed as arguments
# to other functions,
# to those so called 'Higher Order Functions'.

# How can it be? I don't believe this. I think it's utter bullshit.
# But although i have literelly zero belief, i still wanna check this shit out.

# Let me declare a function:

def addition(x, y):
    return x+y


def multiplication(x, y):
    return x*y


def subtraction(x, y):
    return x-y


def division(x, y):
    return x/y


def bigger(func1, func2, x, y):
    result1 = func1(x, y)
    result2 = func2(x, y)
    if result1 > result2:
        return func1
    elif result1 < result2:
        return func2
    else:
        return("It's a tie")


x = 2
y = 5
winner = bigger(addition, multiplication, x, y)
if not (winner == "It's a tie"):
    print(winner(x, y))
else:
    print(winner)


# Hey look It's Fucking Works
