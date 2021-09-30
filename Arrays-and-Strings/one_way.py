# there are three types of edits that can be performed on strings; insert a
# character remove a character, or replace a character. Given two strings, write
# a function to check if tehy are one edit(or zero edits) away


def check_one_way(string_1: str, string_2: str) -> bool:
    if len(string_1) == len(string_2):
        # if len is equal check for no of changes
        count = 0
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                count += 1
                if count == 2:
                    return False
        return True
    elif abs(len(string_1) - len(string_2)) > 1:
        return False

    else:
        i, j = 0, 0     
        count = 0
        while i < len(string_1) and j < len(string_2):
            if string_1[i] != string_2[j]:
                i += 1
                count += 1
            else:
                i += 1
                j += 1
            if count > 1:
                return False
        return True


print(check_one_way("pale", "ple"))
print(check_one_way("pales", "palet"))
print(check_one_way("pale", "bale"))
print(check_one_way("pale", "bake"))
