# Asume you have a method isSubstring which checks if on eword is a substring
# o fanother. Given two strings s1 and s2, write acode to check id s2 is a
# rotation of s2 using only one call to isSubstring(eg., "waterbottle" is a
# rotation of "erbottlewat")


def string_rotation(string_1: str, string_2: str):
    start = string_1[0]
    for i in range(len(string_2)):
        if string_2[i] == start:
            if string_1 == string_2[i:] + string_2[:i]:
                return True
    return False


print(string_rotation("waterbottle", "erbottlewat"))
print(string_rotation("waterbottle", "erbottlewae"))
