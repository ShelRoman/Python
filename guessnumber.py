import random


class GameInfo:

    def __init__(self):
        self.attempts = []

    def print_line(self):
        print("------------------------------------")

    def add_attempt(self, user_choice):
        self.attempts.append(user_choice)

    def print_current_stats(self, game_range):
        self.print_line()
        if self.attempts:
            print("Number of attempts: " + str(len(self.attempts)))
            print("Last attempt: " + str(self.attempts[-1]))
        print("Range is: min- " + str(game_range[0]) + " max- " + str(game_range[1]))
        self.print_line()

    def print_greeting(self):
        print("Hello, User, I've chosen the number, can you guess it?")
        print("Type in " + str(Game.QUIT_NUMBER) + " to stop game immediately!")

    def print_attempt_meassage(self):
        print("Your choice: ")

    def print_out_of_range_message(self):
        print("Number is not in the range, try another one")

    def print_tip(self, user_choice, goal_number):
        if user_choice > goal_number:
            print("The chosen number is lesser than yours")
        else:
            print("The chosen number is bigger than yours")

    def print_NaN_message(self):
        print("Input is NaN, be more attentive")

    def print_endgame_stats(self, is_goal_achieved):
        self.print_line()
        if is_goal_achieved:
            print("You've won. Congratulations!!!")
            print("Attempts made - " + str(len(self.attempts)))
            print("List of user's attempts:")
            for attempt in self.attempts:
                print("Attempt #" + str((self.attempts.index(attempt) + 1)) + " - " + str(attempt))
        else:
            print("Goodbye")
        self.print_line()


class GameController:

    def get_user_choice(self):
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            return Game.WRONG_INPUT


class Game:
    QUIT_NUMBER = 666
    WRONG_INPUT = -666

    def end_game(self):
        self.run_while = False

    def __init__(self):
        self.rand_max = 100
        self.rand_min = 0
        self.run_while = True
        self.is_goal_achieved = False
        self.game_range = [self.rand_min, self.rand_max]
        self.goal_num = random.randint(self.rand_min, self.rand_max)
        self.g_info = GameInfo()
        self.controller = GameController()

    def is_wrong_input(self, user_choice):
        return user_choice == self.WRONG_INPUT

    def process_choice(self, user_choice):
        if self.is_wrong_input(user_choice):
            self.g_info.print_NaN_message()
            return
        if self.is_quit_num(user_choice):
            self.end_game()
        elif self.is_not_in_range(user_choice):
            self.g_info.print_out_of_range_message()
        else:
            self.g_info.add_attempt(user_choice)
            if user_choice == self.goal_num:
                self.is_goal_achieved = True
                self.end_game()
            else:
                self.g_info.print_tip(user_choice, self.goal_num)
                self.change_range(user_choice)

    def start_game(self):
        self.g_info.print_greeting()
        while self.run_while:
            self.g_info.print_current_stats(self.game_range)
            self.g_info.print_attempt_meassage()
            self.process_choice(self.controller.get_user_choice())
        self.g_info.print_endgame_stats(self.is_goal_achieved)

    def is_quit_num(self, user_choice):
        return user_choice == self.QUIT_NUMBER

    def is_not_in_range(self, user_choice):
        return user_choice < self.game_range[0] or user_choice > self.game_range[1]

    def change_range(self, user_choice):
        if user_choice < self.goal_num:
            self.game_range[0] = user_choice
        else:
            self.game_range[1] = user_choice


class MainGame:
    new_game = Game()
    new_game.start_game()
