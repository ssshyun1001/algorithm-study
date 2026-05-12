# Problem: Report Results
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/92334
# Level: Lv.1


# Approach:
# - Remove duplicate reports because the same user can report another user only once
# - Count how many times each user was reported
# - Find banned users whose report count is greater than or equal to k
# - Count how many banned users each user reported

def solution(id_list, report, k):

    # Initialize answer list
    answer = [0] * len(id_list)

    # Remove duplicate reports
    report = list(set(report))

    # Count reported users
    count_dict = {}

    # Store reporters for each reported user
    reporter_dict = {}

    # Process reports
    for ele in report:

        reporter, reported = ele.split()

        if reported in count_dict:
            count_dict[reported] += 1
            reporter_dict[reported].append(reporter)

        else:
            count_dict[reported] = 1
            reporter_dict[reported] = [reporter]

    # Count notification mails
    for key in count_dict:

        if count_dict[key] >= k:

            for reporter in reporter_dict[key]:
                answer[id_list.index(reporter)] += 1

    return answer