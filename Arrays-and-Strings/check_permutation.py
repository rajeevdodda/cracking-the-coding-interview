# Given two strings , write a method to decide  if one is a permutation to other


def check_permutation_using_hash_map(string_1: str, string_2: str):
    hash_map = {}

    for i in string_1:
        hash_map[i] = hash_map.get(i, 0) + 1

    
    for i in string_2:
        if i in hash_map:
            hash_map[i] = hash_map[i] - 1
        else:
            return False
    
    for i in hash_map.values():
        if i != 0:
            return False

    return True

print(check_permutation_using_hash_map("abc", "cba"))
print(check_permutation_using_hash_map("abc", "cbaa"))
print(check_permutation_using_hash_map("abcj", "cba"))
