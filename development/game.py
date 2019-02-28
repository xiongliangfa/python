from random import randint

choice = ['rock', 'paper', 'scissor']

def test(player,computer):
    pass

player = False
if __name__ == "__main__":
    while player == False:
        computer = choice[randint(0, 2)]
        player = input('rock, paper, scissor?')
        test(player,computer)
        player == False