# Problem: Running Race
# Platform: Programmers
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/178871
# Level: Lv.1


# Approach 1: time out
# - When a player's name is called, the player overtakes the player directly ahead.
# - Find the current position of the called player.
# - Remove the player from the current position.
# - Insert the player one position ahead.


def solution(players, callings):
    for calling in callings:

        index_name = players.index(calling)

        players.pop(index_name)
        players.insert(index_name - 1, calling)

    return players

# Approach 2 :
# - Store each player's current rank in a dictionary.
# - When a player's name is called, find the player's current rank.
# - Find the player directly ahead.
# - Swap the two players in the players list.
# - Update both players' ranks in the dictionary.

def solution(players, callings):

    rank_dict = {player: idx for idx, player in enumerate(players)}

    for calling in callings:

        current_rank = rank_dict[calling]
        front_player = players[current_rank - 1]

        players[current_rank - 1], players[current_rank] = (players[current_rank], players[current_rank - 1])

        rank_dict[calling] -= 1
        rank_dict[front_player] += 1

    return players