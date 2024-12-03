import random
import datetime

# Generate a random timestamp and some sample Python code
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
code_samples = [
    "print('Hello, World!')",
    "for i in range(5): print(i)",
    "import math\nprint(math.sqrt(16))",
]

chosen_code = random.choice(code_samples)

# Save the crafted code to a file
with open("crafted_code.py", "w") as file:
    file.write(f"# Generated on {timestamp}\n\n{chosen_code}\n")
