class Calculator:
    def __init__(self):
        pass

    def add_numbers(self, a, b):
        result = a + b
        return result

# Example usage:
calculator_instance = Calculator()
num1 = 5
num2 = 10
sum_result = calculator_instance.add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is: {sum_result}")
