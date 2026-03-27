# Task 1
def create_user(name, age, role):
    return {"name": name.title(), "age": age, "role": role}

users = []

def add_user(name, age, role):
    user = create_user(name, age, role)
    users.append(user)
    return user


def print_users():
    for u in users:
        print(u)

# Task 2
def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

# Task 3
def system_config(**settings):
    for k, v in settings.items():
        print(f"{k}: {v}")

# Task 4
def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Task 5
def square_generator(n):
    for i in range(n):
        yield i * i

# Task 6
def divide_safe():
    try:
        numerator = input("Enter numerator: ")
        denominator = input("Enter denominator: ")
        num = float(numerator)
        den = float(denominator)
        result = num / den
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except ValueError:
        print("Error: Invalid input")
    finally:
        print("Program Completed")

# Task 7
def file_handling_demo():
    users_to_write = [
        create_user("alice", 28, "developer"),
        create_user("bob", 35, "manager")
    ]
    f = open("team_data.txt", "w")
    try:
        for u in users_to_write:
            f.write(f"{u['name']},{u['age']},{u['role']}\n")
    finally:
        f.close()

    with open("team_data.txt", "r") as r:
        content = r.read()
    print(content)
    print("File closed:", r.closed)

if __name__ == "__main__":
    add_user("john doe", 30, "admin")
    add_user("jane smith", 25, "user")
    print_users()

    total, avg = calculate_total(10, 20, 30)
    print("Total:", total, "Average:", avg)

    system_config(mode="debug", version="1.0")

    try:
        print("Factorial 5:", factorial(5))
        print("Factorial 0:", factorial(0))
    except ValueError as e:
        print(e)

    list_squares = [i * i for i in range(5)]
    gen_squares = square_generator(5)
    print("List type:", type(list_squares), "Generator type:", type(gen_squares))
    print("Generator values:", list(gen_squares))

    file_handling_demo()
