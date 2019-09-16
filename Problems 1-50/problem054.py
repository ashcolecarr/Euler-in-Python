# Project Euler Problem 54

import time
from collections import Counter

startTime = time.clock()

FILENAME = "poker.txt"

class Hand:
    NONE, ONE_PAIR, TWO_PAIRS, THREE_OF_A_KIND, STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH, ROYAL_FLUSH = range(10)   

def convertCardValue(cardValue):
    if cardValue == 'T':
        return 10
    elif cardValue == 'J':
        return 11
    elif cardValue == 'Q':
        return 12
    elif cardValue == 'K':
        return 13
    elif cardValue == 'A':
        return 14
    else:
        return int(cardValue)

def determineHand(hand):
    cardValues = [convertCardValue(x[0]) for x in hand]
    cardSuits = [x[1] for x in hand]

    cardValues.sort()
    sameValues = len(set(cardValues))
    # If every card is of the same suit, it is some kind of flush.
    if len(set(cardSuits)) == 1:
        # Are the values consecutive?
        if sameValues == 5 and cardValues[4] - cardValues[0] == 4:
            # Royal Flush
            if cardValues[0] == 10 and cardValues[4] == 14:
                return Hand.ROYAL_FLUSH
            # Straight Flush
            else:
                return Hand.STRAIGHT_FLUSH
        # Flush
        else:
            return Hand.FLUSH
    
    # Check if values are consecutive, but not of the same suit, i.e. a Straight.
    if sameValues == 5 and cardValues[4] - cardValues[0] == 4:
        return Hand.STRAIGHT

    valuesCount = Counter(cardValues)
    if sameValues == 2:
        # If there are 4 of the same value, then it's Four of a Kind.
        if 4 in valuesCount.values():
            return Hand.FOUR_OF_A_KIND
        # Otherwise, it must be a Full House.
        else:
            return Hand.FULL_HOUSE
    elif sameValues == 3:
        # If there are 3 of the same value, then it's Three of a Kind.
        if 3 in valuesCount.values():
            return Hand.THREE_OF_A_KIND
        # Otherwise, it must be Two Pairs.
        else:
            return Hand.TWO_PAIRS
    elif sameValues == 4:
        # Only One Pair
        return Hand.ONE_PAIR

    # No winning hand.
    return Hand.NONE

def player1HasHighCard(player1Hand, player2Hand):
    player1CardValues = [convertCardValue(x[0]) for x in player1Hand]
    player2CardValues = [convertCardValue(x[0]) for x in player2Hand]

    return max(player1CardValues) > max(player2CardValues)

def player1HasGreaterValuedHand(player1Cards, player2Cards, playerHand):
    player1CardValues = [convertCardValue(x[0]) for x in player1Cards]
    player2CardValues = [convertCardValue(x[0]) for x in player2Cards]
    player1CardValues.sort()
    player2CardValues.sort()
    player1CountedValues = Counter(player1CardValues)
    player2CountedValues = Counter(player2CardValues)
    
    if playerHand == Hand.STRAIGHT_FLUSH or playerHand == Hand.FLUSH or playerHand == Hand.STRAIGHT or playerHand == Hand.NONE:
        return player1HasHighCard(player1Cards, player2Cards)
    elif playerHand == Hand.TWO_PAIRS or playerHand == Hand.ONE_PAIR:
        player1PairValues = [x for x in player1CountedValues.keys() if player1CountedValues[x] > 1]
        player2PairValues = [x for x in player2CountedValues.keys() if player2CountedValues[x] > 1]
        if max(player1PairValues) == max(player2PairValues) and min(player1PairValues) == min(player2PairValues):
            return player1HasHighCard(player1Cards, player2Cards)
        else:
            return max(player1PairValues) > max(player2PairValues)
    else:
        if player1CountedValues[0] == player2CountedValues[0]:
            return player1HasHighCard(player1Cards, player2Cards)
        else:
            return player1CountedValues[0] > player2CountedValues[0]

def isPlayer1Winner(playerHands):
    splitHands = playerHands.split(' ')
    player1Hand = determineHand(splitHands[0:5])
    player2Hand = determineHand(splitHands[5:10])

    if player1Hand > player2Hand:
        return True
    elif player1Hand < player2Hand:
        return False
    # If both players have the same hand, check which hand has the greater value or check the high card if the hands are equal in value.
    else:
        return player1HasGreaterValuedHand(splitHands[0:5], splitHands[5:10], player1Hand)

player1WinCount = 0
with open(FILENAME, 'r') as handsFile:
    data = handsFile.readlines()

    for hands in data:
        if isPlayer1Winner(hands[0:-1:]):
            player1WinCount += 1

print("Player 1 wins {0} poker hands.".format(player1WinCount))

print("Program execution took {0} seconds.".format(time.clock() - startTime))
