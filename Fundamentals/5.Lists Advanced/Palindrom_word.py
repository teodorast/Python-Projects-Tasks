def palindrom_checker(word):
    if word==word[::-1]:
        return word


words = input().split()

palindrom_word = input()

palindrom_list = [word for word in words if palindrom_checker(word)]
number_palindromes = palindrom_list.count(palindrom_word)
print(palindrom_list)
print(f"Found palindrome {number_palindromes} times")