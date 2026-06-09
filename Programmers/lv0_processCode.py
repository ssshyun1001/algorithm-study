# Problem: Process Code
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/181932
# Level: Lv.0


# Approach 1:
# - Iterate through the code with both index and character.
# - Toggle the mode whenever the character is '1'.
# - In mode 0, append the character only if its index is even.
# - In mode 1, append the character only if its index is odd.
# - Return "EMPTY" if the result string is empty.
# - Otherwise, return the result string.

def solution(code):
    mode = 0
    ret = ""

    for idx, letter in enumerate(code):
        if letter == "1":
            mode = 1 - mode
            continue

        if mode == 0:
            if idx % 2 == 0:
                ret += letter
        else:
            if idx % 2 == 1:
                ret += letter

    if ret =="":
        return "EMPTY"

    return ret