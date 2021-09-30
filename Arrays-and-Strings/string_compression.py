# Implemenet a method to perform basic string compression using the counts of
# repeated characters. For example, the strin "aabcccccaaa" would become
# "a2b1c5a3". If "compressed" string would not become smaller than the original
# string, your method should return the original string. You can asssume the
# string has only uppercase and lower case letter(a-z)


def string_compression(string: str) -> str:
    last = string[0]
    count = 1
    compressed_string  = ""
    for i in string[1:]:
        if i == last:
            count += 1
        else:
            compressed_string = compressed_string + last + str(count)
            count = 1
            last = i
    compressed_string = compressed_string + last + str(count)

    if len(compressed_string) == 2 * len(string):
        return string
    return compressed_string


print(string_compression("aabcccccaaa"))
print(string_compression("abcde"))