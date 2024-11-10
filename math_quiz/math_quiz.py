import random
"""
Math Quiz Game

This program launches an interactive math quiz where the user must solve randomly generated math problems.
The problems are created using random integers and include addition, subtraction or multiplication.
"""


def random_integer(min_val, max_val):
    """
    Return a random integer within the specified range.
    """
    return random.randint(min_val, max_val)


def random_operator():
    """
    Return a random operator as a string.
    """
    return random.choice(['+', '-', '*'])


def generate_problem(integer1, integer2, operator):
    """
    Generate a mathematical problem using two integers and an operator,
    and return both the problem as a string and the correct solution as an integer.
    """
    problem = f"{integer1} {operator} {integer2}"
    if operator == '+':
        answer = integer1 + integer2
    elif operator == '-':
        answer = integer1 - integer2
    else:
        answer = integer1 * integer2

    return problem, answer


def math_quiz():
    """
    Start a math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        integer1 = random_integer(1, 10)
        integer2 = random_integer(1, 5)
        operator = random_operator()

        problem, answer = generate_problem(integer1, integer2, operator)
        print(f"\nQuestion: {problem}")

        while True:
            try:
                user_answer = int(input("Your answer: "))
                if user_answer == answer:
                    print("Correct! You earned a point.")
                    score += 1
                else:
                    print(f"Wrong answer. The correct answer is {answer}.")
                break
            except ValueError:
                print(f"Invalid input. Please enter a number!")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
