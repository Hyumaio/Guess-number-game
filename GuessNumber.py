# Due to the method randint() including both end points which in Python is usually not what you want,
# you should always use randrange() instead of randint().
# number = random.randint(1, 100)

import random

# STARTPOINT: Set randrange start from which.
# CHANCES: Set randrange end to which.
# ENDPOINT: Set guess times, NOT include the endpoint.

STARTPOINT = 1
CHANCES = 5
ENDPOINT = 101


# OOP:
class GuessGame(object):
    def __init__(self, startpoint, endpoint, chances):
        """
        :param startpoint: Randrange start from which.
        :param endpoint: Randrange end to which.
        :param chances: The guess times you have.
        """
        self.chances = chances
        self.answer = random.randrange(startpoint, endpoint)

    def guess(self):
        # print(self.answer)  # for test

        while self.chances > 0:
            self.chances -= 1
            try:
                guess = int(input('\nType your guess here:'))
            except ValueError as e:
                print('Valid number only!!!')
                print('%s times left...' % (self.chances))
                continue

            if guess == self.answer:
                print('Bingo!!!')
                break
            elif guess > self.answer:
                print('Your guess is too large, try smaller...')
            else:
                print('Too small, try again...')

            print('%s times left...' % self.chances)

        else:
            print('Run out of times!!! the right number is %s...' % self.answer)


if __name__ == '__main__':
    # assert isinstance(STARTPOINT, int), "Type error of startpoint, int required."
    # assert isinstance(ENDPOINT, int), "Type error of endpoint, int required."
    # assert isinstance(CHANCES, int), "Type error of chances, int required."
    game = GuessGame(STARTPOINT, ENDPOINT, CHANCES)
    game.guess()




# POP:
# NUMBER = random.randrange(start=1, stop=101)
#
#
# def guess():
#     # print(number)  # for test
#     answer = NUMBER
#     chance = 0
#
#     while chance < 5:
#         try:
#             guess = int(input('\nType your guess here:'))
#             if guess == answer:
#                 print('Bingo!!!')
#                 return
#             if guess > answer:
#                 print('Your guess is too large, try smaller...')
#             elif guess < answer:
#                 print('Too small...')
#
#         except Exception as e:
#             print(e)
#
#         chance += 1
#         print('%s times left...' % (5 - chance))
#     print('Run out of times, the right number is %s...' % answer)
#
#
# if __name__ == '__main__':
#     guess()
