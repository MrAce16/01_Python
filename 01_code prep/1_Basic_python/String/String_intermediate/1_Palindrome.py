# str1 = input("Enter the string : ")
# if str1 == str1[::-1]:
#     print("Print string is palindrome")

# else:
#     print("enter string is not palindrome")


def palindrome(str1):
    for i in str1:
        print(i)

        # print("Print palindrome")

        # if str1[i] == str1[::-1]:
        #     print("Print palindrome")
        # else:
        #     print("Not an Palindrome")


phrases = [
    "racecar", "level", "deified", "radar", "civic",
    "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?",
    "No 'x' in Nixon.", "Eva, can I see bees in a cave?", "Madam, in Eden, I'm Adam.",
    "RaceCar", "LeVEl", "DeiFied", "RaDar", "CiVic",
    "A Santa at NASA", "Able was I, ere I saw Elba!",
    "Madam, in Eden, I'm Adam.", "Mr. Owl ate my metal worm.", "Step on no pets."
]
str1 = palindrome(str(phrases))


def check_palidrome(str):
    rev = ""
    for ch in str[::-1]:
        rev = rev+ch
    if str == rev:
        print("plaindrome")
    else:
        print("not plaindrome")


phrases = [
    "racecar", "level", "deified", "radar", "civic",
    "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?",
    "No 'x' in Nixon.", "Eva, can I see bees in a cave?", "Madam, in Eden, I'm Adam.",
    "RaceCar", "LeVEl", "DeiFied", "RaDar", "CiVic",
    "A Santa at NASA", "Able was I, ere I saw Elba!",
    "Madam, in Eden, I'm Adam.", "Mr. Owl ate my metal worm.", "Step on no pets."
]


for ch in phrases:
    check_palidrome(ch.lower().split())
