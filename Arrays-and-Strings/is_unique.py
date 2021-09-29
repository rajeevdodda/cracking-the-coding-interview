# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data stuctures ?


def is_unique_using_hash_map(string: str):

    hash_table = set()

    for i in string:
        if i in hash_table:
            return False
        hash_table.add(i)
    return True


def is_unique_using_bits(string: str):
    checker = 0
    for i in string:
        val = ord(i) - ord("a")
        if checker & (1 << val) > 0:
            return False
        checker = checker | (1 << val)
        print(checker)
    return True


print(is_unique_using_hash_map("abca"))
print(is_unique_using_hash_map("bbc"))

print(is_unique_using_bits("abca"))
print(is_unique_using_bits("bbc"))
