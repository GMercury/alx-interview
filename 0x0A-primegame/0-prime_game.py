#!/usr/bin/python3
"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds of playing the Prime Game.
"""


def isWinner(x, nums):
    """
    Determines the winner after a certain number of rounds
    of playing the Prime Game

    The Prime Game is a list of consecutive ints starting from 1 up to and
    including n. Players take turns picking prime numbers, which removes
    that number and all multiples of that number from the set. The player that
    has no more prime numbers to choose loses the game.

    Maria and Ben are playing the game, and Maria always goes first.
    Given the number of rounds, n, determine who the winner is.

    parameters:
        x [int]:
            the number of rounds
        nums [list of ints]:
            list of all ns for each round
    returns:
        the name of the player that won the most rounds,
        if both players play optimally,
        or None, if the winner cannot be determined
    """
    if not nums or x < 1:  # if nums is empty or x is less than 1
        return None
    n = max(nums)  # get the max value in nums list
    sieve = [True for _ in range(max(n + 1, 2))]  # create a sieve of True val.
    for i in range(2, int(pow(n, 0.5)) + 1):  # loop through the sieve
        if not sieve[i]:  # if the value is False (not prime)
            continue
        for j in range(i*i, n + 1, i):  # loop through the sieve
            sieve[j] = False  # set the value to False (not prime)

    sieve[0] = sieve[1] = False  # set 0 and 1 to False (not prime)
    count = 0  # initialize count to 0 (Maria's score)
    for i in range(len(sieve)):  # loop through the sieve and count the primes
        if sieve[i]:  # if the value is True (prime)
            count += 1
        sieve[i] = count  # set the value to the count of primes

    player1 = 0
    for n in nums:  # loop through the nums list and count Maria's wins
        player1 += sieve[n] % 2 == 1  # if Maria's score is odd, she wins
    if player1 * 2 == len(nums):  # if Maria wins half the rounds
        return None
    if player1 * 2 > len(nums):  # if Maria wins more than half the rounds
        return "Maria"  # Maria wins
    return "Ben"  # Ben wins
