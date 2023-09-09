#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Print the person's name in the format
    "My name is <first name> <last name>".

    :param first_name: The first name of the person.
    :param last_name: The last name of the person (optional).
    :raises TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(
            first_name, str) or not isinstance(
                    last_name, str):
        raise TypeError(
                "first_name must be a string or last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")


if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
