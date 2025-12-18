def is_number_validation(function):
    def wrapper(*args):
        if not isinstance(*args, (int, float)):
            raise TypeError("The parameter is not a number")
        return function(*args)
    return wrapper

@is_number_validation
def show_numbers(number_one, number_two):
    print(f"The numbers are: {number_one} and {number_two}")

show_numbers(1, 2)