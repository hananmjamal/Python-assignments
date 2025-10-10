s = input("Enter a string: ")
def has_unique_chars(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True
print(has_unique_chars(s))
