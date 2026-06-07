# Problem: Rank Search
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/72412
# Level: Lv.2

# Approach 1 : time out
# - Split applicants into three groups based on language: java, cpp, and python.
# - Split each language group again based on job type.
# - Split each subgroup again based on career level.
# - Split each subgroup again based on food preference.
# - For each query, select the matching group.
# - Count applicants whose score is greater than or equal to the required score.

def solution(info, query):
    applicant_dict = {}

    # Split applicants by each condition
    for applicant in info:
        language, job, career, food, score = applicant.split()
        score = int(score)

        key = (language, job, career, food)

        if key not in applicant_dict:
            applicant_dict[key] = []

        applicant_dict[key].append(score)

    answer = []

    # Process each query
    for q in query:
        q = q.replace(" and ", " ")
        language, job, career, food, score = q.split()
        score = int(score)

        count = 0

        # Check all divided groups
        for key in applicant_dict:
            key_language, key_job, key_career, key_food = key

            if language != "-" and language != key_language:
                continue

            if job != "-" and job != key_job:
                continue

            if career != "-" and career != key_career:
                continue

            if food != "-" and food != key_food:
                continue

            for applicant_score in applicant_dict[key]:
                if applicant_score >= score:
                    count += 1

        answer.append(count)

    return answer

# Approach 2: time out
# - Assign a unique prime number to each attribute value.
# - Convert each applicant's information into a unique key by multiplying the corresponding prime numbers.
# - Store applicants in a dictionary using the product of primes as the key.
# - Save the applicant's score in the dictionary value.
# - For each query, convert the specified conditions into a prime-product key.
# - Ignore '-' conditions when generating the query key.
# - Check whether an applicant key is divisible by the query key.
# - If applicant_key % query_key == 0, the applicant satisfies all specified conditions.
# - Count applicants whose score is greater than or equal to the target score.


def solution(info, query):

    prime_dict = {
        "java": 2,
        "cpp": 3,
        "python": 5,
        "backend": 7,
        "frontend": 11,
        "junior": 13,
        "senior": 17,
        "chicken": 19,
        "pizza": 23
    }

    applicant_dict = {}

    # Store applicants
    for applicant in info:

        language, job, career, food, score = applicant.split()

        key = (
            prime_dict[language]
            * prime_dict[job]
            * prime_dict[career]
            * prime_dict[food]
        )

        if key not in applicant_dict:
            applicant_dict[key] = []

        applicant_dict[key].append(int(score))

    answer = []

    # Process queries
    for q in query:

        q = q.replace(" and ", " ")
        language, job, career, food, target_score = q.split()

        query_key = 1

        if language != "-":
            query_key *= prime_dict[language]

        if job != "-":
            query_key *= prime_dict[job]

        if career != "-":
            query_key *= prime_dict[career]

        if food != "-":
            query_key *= prime_dict[food]

        count = 0

        for applicant_key, scores in applicant_dict.items():

            if applicant_key % query_key == 0:

                for score in scores:

                    if score >= int(target_score):
                        count += 1

        answer.append(count)

    return answer

# Approach 3 (Accepted)
# - Generate all possible condition combinations for each applicant, including '-'.
# - Store the applicant's score for every generated condition key.
# - Use a dictionary where the key is a condition combination and the value is a list of scores.
# - Sort all score lists in the dictionary.
# - Convert each query into the corresponding condition key.
# - Use binary search to count scores greater than or equal to the target score.

from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    applicant_dict = {}

    # Store applicant scores for all possible condition keys
    for applicant in info:
        data = applicant.split()
        conditions = data[:-1]
        score = int(data[-1])

        for i in range(5):
            for comb in combinations(range(4), i):
                temp = conditions[:]

                for idx in comb:
                    temp[idx] = "-"

                key = "".join(temp)

                if key not in applicant_dict:
                    applicant_dict[key] = []

                applicant_dict[key].append(score)

    # Sort scores for binary search
    for key in applicant_dict:
        applicant_dict[key].sort()

    answer = []

    # Process queries
    for q in query:
        q = q.replace(" and ", " ")
        data = q.split()

        conditions = data[:-1]
        target_score = int(data[-1])

        key = "".join(conditions)

        if key not in applicant_dict:
            answer.append(0)
            continue

        scores = applicant_dict[key]

        index = bisect_left(scores, target_score)

        answer.append(len(scores) - index)

    return answer