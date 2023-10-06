from datetime import datetime
import os


def MyFunction(Name, Location):
    """Prints a personalized greeting and the current date and time to the console.

    Args:
      Name: The name of the person to greet.
      Location: The location of the person to greet.
    """

    where_is = os.getcwd()
    print("Path: " + where_is + "\n")

    today_is = datetime.today().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Hey {Name} in {Location}! Today is {today_is}.")


# Example 1
MyFunction("Mrs. John", "New York City")

# Example 2
MyFunction("Mr. Louis", "London")

# Example 3
MyFunction("Dr. Smith", "Tokyo")
