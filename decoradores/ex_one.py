def pre_post_decorator(show_user):
    def wrapper(name, age):
        print(f"Pre function logic prints: {name} and {age}")
        show_user(name, age)
        print("Post function logic")
    return wrapper

@pre_post_decorator
def show_user(name, age):
    print(f"User name is {name} and age is {age}")

show_user("Jose", 35)