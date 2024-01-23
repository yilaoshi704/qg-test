import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["石头", "剪刀", "布"]

    def get_user_choice(self):
        while True:
            choice = input("请选择：剪刀，石头，布：")
            if choice in self.choices:
                return choice
            else:
                print("无效选择，请重新选择。")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "平局！"
        elif (user_choice == "石头" and computer_choice == "剪刀") or (
                user_choice == "剪刀" and computer_choice == "布") or (
                user_choice == "布" and computer_choice == "石头"):
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

            while True:
                play_again = input("再来一轮？(y/n) ")
                if play_again == "y":
                    break
                elif play_again.lower() == "n":
                    game_over = True
                    break
                else:
                    print("输入有误！！")

game = RockPaperScissors()
game.play()
