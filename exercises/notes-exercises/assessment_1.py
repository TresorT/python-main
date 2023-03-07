player_one_cards = [10, 6, 8, 9, 7, 12, 7]
player_two_cards = [7, 6, 9, 5, 2, 8, 11]
turn = 0
player_one_score = 0
player_two_score = 0

print('**********Card Busters**********')

for i in range(7):
    turn += 1
    if player_one_cards[i] > player_two_cards[i]:
        print('Round number', str(turn) + ':', 'Player 1 wins the round, with', player_one_cards[i], ' beating ',
              player_two_cards[i])
        player_one_score += 1
    elif player_one_cards[i] < player_two_cards[i]:
        print('Round number', str(turn) + ':', 'Player 2 wins the round, with', player_two_cards[i], ' beating ',
              player_one_cards[i])
        player_two_score += 1
    else:
        print('Round number', str(turn) + ':', 'This round has ended in a draw')

print()
if player_one_score > player_two_score:
    print('Player 1 wins the game, by', player_one_score, 'wins to', player_two_score)
elif player_one_score < player_two_score:
    print('Player 2 wins the game, by', player_two_score, 'wins to', player_one_score)
else:
    print("It's a tie! Both Player 1 and Player 2 won ", player_one_score, " rounds each.")
