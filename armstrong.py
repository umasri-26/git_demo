#write a python programming for armstrong number
def is_armstrong_number(num):
    """Function to check if a number is an Armstrong number."""
    num_str = str(num)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == num
# Example usage
if __name__ == "__main__":
    number = 153
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")


