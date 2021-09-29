# Given a string, write a function to check if is permutation of a palindrome

def check_palindrome_permutation(string: str) -> bool:

    hash_table = {}

    for i in string:
        hash_table[i] = hash_table.get(i, 0) + 1

    
    count = 0

    for i in hash_table.values():
        if i % 2 == 1:
            count += 1
            if count > 1:
                return False
    return True

print(check_palindrome_permutation("abcccba"))
print(check_palindrome_permutation("abcccbaa"))
print(check_palindrome_permutation("abcccbaaa"))