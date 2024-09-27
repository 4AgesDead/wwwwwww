import json, random


with open('quests.json', 'r', encoding='utf-8') as file:
    list_quest = json.loads(file.read())



class Quests():
    def __init__(self, quest, diff, answer):
        self.quest = quest
        self.diff = diff
        self.answer = answer
        self.quested = False
        self.user_answer = None
        self.scores = self.get_points()

    def get_points(self):
        return self.diff * 10

    def is_correct(self):
        if self.user_answer == self.answer:
            return True
        else:
            return False


class Works():
    def __init__(self):
        self.list_quest = []
        self.random_numb = None
        self.make_list()
        self.poits = 0
        self.right=0

    def make_list(self):
        for quest in list_quest:
            self.list_quest.append([Quests(quest['quest'], quest['dif'], quest['answer']), False])

    def build_question(self):
        if self.list_quest[self.random_numb][1] == False:
            print(self.list_quest[self.random_numb][0].quest, )
            print('diff', self.list_quest[self.random_numb][0].diff)
            self.list_quest[self.random_numb][0].user_answer = input("ur answer ")
        else:
            self.work()

    def build_feedback(self):
        if self.list_quest[self.random_numb][0].is_correct():
            print('Боже, а ты хорош, получено',  self.list_quest[self.random_numb][0].scores, ' баллов')
            self.poits += self.list_quest[self.random_numb][0].scores
            self.right += 1
        else:
            print('АХАХАХАХАХХА ЛОХ, верный ответ', self.list_quest[self.random_numb][0].answer)
        self.list_quest[self.random_numb][1] = True

    def is_correct(self):
        if self.list_quest[self.random_numb][0].user_answer == self.list_quest[self.random_numb][0].answer:
            return True
        else:
            return False

    def work(self):
        while True:
            self.random_numb = random.randint(0, len(list_quest)-1)
            self.build_question()
            self.build_feedback()
            if self.check_end():
                self.build_end()
                break

    def check_end(self):
        count_false = 0
        for quest in self.list_quest:
            if quest[1] == False:
                count_false+=1
        if count_false == 0:
            return True

    def build_end(self):
        print('Вот и все!')
        print('Отвечено ', self.right,' вопроса из ', len(list_quest))
        print('Набрано баллов: ', self.poits)


Works().work()
'''
for i in range(len(list_quest)-1):
    a = random.randint(0,len(list_quest)-1)
    quest = Quests(list_quest[a]['quest'], list_quest[a]['dif'], list_quest[a]['answer'])
    quest.build_question()
    quest.user_answer = input("ur answer ")
    quest.build_feedback()'''
