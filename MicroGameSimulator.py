import numpy as np
import random


def roll_dice(dice_size):
    return random.randint(1,dice_size)


class Game:
    def __init__(self):
        self.game_history =np.zeros((1000,3))
        self.game_state = np.zeros(3)
        self.current_round = 0
        self.game_state[1] = 10


    def bettle_events(self):
        #
        roll = roll_dice(6)
        if roll <=2:
            #a visitor to your room
            roll = roll_dice(6)
            if roll ==1:
                #Your dad comes in and tells you to get another job. Take in a CV, he says. You chitter.
                self.game_history[self.current_round,0] += 1
                self.game_history[self.current_round,1] -= 1
            elif roll ==2:
                # Your mom complains you never help around the house
                self.game_history[self.current_round,0] += 1
            elif roll ==3:
                #Your girlfriend comes over. She feels like you are a better listener these days.
                self.game_history[self.current_round,0] += 1
            elif roll ==4:
                #Your boss calls. Yes, they understand you are a beetle, but they need you to cover more shifts
                self.game_history[self.current_round,1] += 1
                self.game_history[self.current_round,0] += 1
            elif roll ==5:
                #The doctor analyses you "Have you considered losing weight?", they ask
                self.game_history[self.current_round,0] += 1
                self.game_history[self.current_round,2] += 1
            else:
                # The window cleaner comes by for another look. There is prolonged eye contact.
                self.game_history[self.current_round,2] += 1
        elif roll <=5:
            # AN INSECT OF UNUSUAL SIZE...
            roll = roll_dice(6)
            if roll ==1:
                # Your rent is due, even if you are a beetle.
                self.game_history[self.current_round,1] -= 2
            elif roll ==2:
                #You dream peacefully of rooting about in the mud.
                self.game_history[self.current_round,0] += 1
            elif roll ==3:
                #You practice doing beetle things, like buzzing and clacking until you are yelled at to stop
                self.game_history[self.current_round,0] += 2
            elif roll ==4:
                #You get tipped on your back and need help to stand on your feet again
                self.game_history[self.current_round,2] += 1
            elif roll ==5:
                #You look out onto the street at all the delicious people walking below
                self.game_history[self.current_round,2] += 2
            else:
                #You record content for social media. You are downvoted by entomophobes who dont like being called that
                self.game_history[self.current_round,2] += 1
                self.game_history[self.current_round,0] += 1
        else:
            roll = roll_dice(2)
            if roll ==1:
                self.game_history[self.current_round,1] -= 1
            elif roll ==2:
                self.game_history[self.current_round,2] += 2



        if self.current_round % 3 == 0:
            self.game_history[self.current_round,1] -= 1


    def check_for_end_state(self):
        if self.game_state[0] >= 10:
            return True
        if self.game_state[1] <= 0:
            return True
        if self.game_state[2] >= 10:
            return True
        return False




    def run_round(self):
        self.bettle_events()
        self.game_state += self.game_history[self.current_round]
        self.current_round += 1
        return None

    def return_game_state(self):
        return self.game_state

    def return_game_history(self):
        return self.game_history
    def return_current_round(self):
        return self.current_round


game=Game()
number_of_runs=1000
array_of_games=np.zeros(number_of_runs,dtype=object)
print(array_of_games)
for i in range(number_of_runs):
    game=Game()
    for n in range(number_of_runs):
        if game.check_for_end_state() is False:
            game.run_round()
    game_state = game.return_game_state()
    # print("adding game state",i)
    array_of_games[i] = game
    print("round",game.current_round,"final state",game_state)


# curent_max=np.zeros(3,dtype=int)
# # print(array_of_games)
# for i in range(number_of_runs):
#     current_game = array_of_games[i]
#
#     game_state = current_game.return_game_state()
#     if game_state[0] > curent_max[0]:
#         curent_max[0] = game_state[0]
#     if game_state[1] < curent_max[1]:
#         curent_max[1] = game_state[1]
#     if game_state[2] > curent_max[2]:
#         curent_max[2] = game_state[2]
# else:
#     print("no game")
# print(curent_max)
# print("max",curent_max)
longest_run =0
for i in range(number_of_runs):
    current_game = array_of_games[i]

    game_length = current_game.return_current_round()
    if game_length > longest_run:
        longest_run = game_length
print("longest_run",longest_run)




