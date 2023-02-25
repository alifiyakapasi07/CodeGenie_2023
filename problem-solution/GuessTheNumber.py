def find_original_number(final_number, operations):
  
    # Initialize the original number as the final number
    original_number = final_number
    
    for operation in operations:
        operator, value = operation.split(" ")[1:]
        value = int(value)
        if operator == "+":
            original_number += value
        elif operator == "-":
            original_number -= value
        elif operator == "*":
            original_number *= value
        elif operator == "/":
            original_number /= value
        elif operator == "^":
            original_number **= (1/value)
        elif operator == "%":
            original_number = original_number * value + (original_number // value)
    
    return int(original_number)
  
# Example usage

final_number = 2500
operations = ["X + 10", "X - 5", "X * 5", "X ^ 2"]

original_number = find_original_number(final_number, operations)
print("Original number:", original_number)
