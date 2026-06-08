# Problem: Find the Mode
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/120812
# Level: Lv.0


# Approach 1:  Raises an error when there are multiple modes.
# - Use the statistics.mode() function to find the most frequent value.
# - Return the mode directly.
def solution(array):
    from statistics import mode
    answer = mode(array)

    return answer

# Approach 2: Use a Dictionary
# - Count the frequency of each number using a dictionary.
# - Find the maximum frequency.
# - Count how many numbers have the maximum frequency.
# - Return the number if the mode is unique.
# - Return -1 if multiple modes exist.
def solution(array):
    count_dict = {num:array.count(num) for num in set(array)}
    frequency_max = max(count_dict.values())
    count_max = list(count_dict.values()).count(frequency_max)

    if count_max != 1:
        answer = -1

    else:
        for key, value in count_dict.items():
            if value == frequency_max:
                answer = key

    return answer