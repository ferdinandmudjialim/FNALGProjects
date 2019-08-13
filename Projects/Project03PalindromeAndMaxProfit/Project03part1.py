def reverseStr(str):
    if len(str) <= 1:
        return str
    else:
        return reverseStr(str[1:]) + str[0]

def ispalindrome(str):
    word = str.replace(" ", "").lower()
    length = len(word)
    if length <= 1:
        return True
    else:
        return ispalindrome(word[1:length-1]) and word[0] == word[length-1]


str1 = 'pots&pans'
str2 = 'racecar'
str3 = 'gohangasalamiimalasagnahog'

print(reverseStr(str1))
print(reverseStr(str2))
print(reverseStr(str3))

print(ispalindrome(str1))
print(ispalindrome(str2))
print(ispalindrome(str3))

