import random


def generate_math_problem(nums, seed):
    random.seed(seed)
    problems = []
    for _ in range(nums):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '/':
            while eval(f"{num1} {operator} {num2}") != num1 // num2:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)

        else:
            pass
        problem = f"{num1} {operator} {num2}"
        problems.append(problem)
    return problems
