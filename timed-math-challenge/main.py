import random
import time

OPERATORS = ["+", "-", "*", "/"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    operator = random.choice(OPERATORS)

    if operator == "/":
        answer = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        left = answer * right
    else:
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)

        if operator == "+":
            answer = left + right
        elif operator == "-":
            answer = left - right
        else:
            answer = left * right

    expression = f"{left} {operator} {right}"
    return expression, answer


wrong = 0

input("=== Math Quiz Game ===\nPress Enter to begin...")
print("=" * 40)
print(f"Solve {TOTAL_PROBLEMS} math problems as quickly as you can!")
print("=" * 40)

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True:
        value = input(f"Question {i + 1}: {expression} = ")

        if value.strip() == str(answer):
            break

        wrong += 1
        print("Incorrect. Try again.")

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("=" * 40)
print("Quiz completed!")
print(f"Time taken: {total_time} seconds")
print(f"Incorrect attempts: {wrong}")
print("=" * 40)
print("Thanks for playing!")
