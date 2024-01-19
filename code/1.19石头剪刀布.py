import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["石头", "剪刀", "布"]

    def get_user_choice(self):
        while True:
            choice = input("请选择：剪刀，石头，布：")
            if choice.lower() in self.choices:
                return choice.lower()
            else:
                print("无效选择，请重新选择。")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "平局！"
        elif (user_choice == "rock" and computer_choice == "scissors") or (
                user_choice == "scissors" and computer_choice == "paper") or (
                user_choice == "paper" and computer_choice == "rock"):
            return "牛啊牛啊！"
        else:
            return "拉了拉了！"

    def play(self):
        game_over = False
        while not game_over:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print("电脑选择：", computer_choice)
            print(self.determine(user_choice, computer_choice))

            play_again = input("再来一轮？(y/n) ")
            if play_again.lower() != "y":
                game_over = True


# 实例化游戏对象，并启动游戏
game = RockPaperScissors()
game.play()
