def is_palindrome(number):
    number_str = str(number)

    return number_str == number_str[::-1]

def check_palindromes(numbers):

    numbers_list = [int(num) for num in numbers.split(", ")]

    results = [is_palindrome(num) for num in numbers_list]
    
    return results

input_numbers = input()

results = check_palindromes(input_numbers)

for result in results:
    print(result)
