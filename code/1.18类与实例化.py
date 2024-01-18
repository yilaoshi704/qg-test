true_answers = []


class Student:

    def __init__(self, name, major, stu_class, answers, score):
        self.name = name
        self.major = major
        self.stu_class = stu_class
        self.answers = str(answers)
        self.score = 0

    def compute(self, true_answers):
        self.score = 0  # 重置分数为0
        for true_answer, now_answer in zip(true_answers, self.answers):  # 使用zip函数进行迭代
            if int(true_answer) == int(now_answer):  # 将答案转换为整数类型进行比较
                self.score += 1
        print(self.score)

while True:
    true_answers.append(input("Enter the correct answers\n"))
    if input("Enter 'q' to quit\n") == 'q':
        print("Quit")
        break
    else:
        continue

while True:
    a = Student(
        input("Enter name\n"),
        input("Enter major\n"),
        input("Enter class\n"),
        input("Enter answers\n"),
        0
    )
    a.compute(true_answers)
    if input("Enter 'q' to quit\n") == 'q':
        print("Quit")
        break
    else:
        continue
