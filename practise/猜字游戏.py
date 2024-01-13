# 猜单词游戏
#
import random

lives = 3  # 3次机会

answers = ['s', 't', 'r', 'a', 'n', 'g', 'e']
answer = random.choice(answers)  # 谜底,随机
print(answer)

heart_symbol = u'\u2764'

is_correct = False
correct_set = set()  # 已猜中的不能重复猜


def answer_correct(guessed_word, correct_answer):
    if guessed_word == correct_answer:
        is_correct = True
        return is_correct


def count_set(set1:set):
    return len(set1)

while lives>0:
    print('剩余猜测次数: '+heart_symbol * lives)
    guess = str(input('猜测包含字母: ').strip().lower())
    res = answer_correct(guess, answer)
    if correct_set.__contains__(guess):
        print('这个已经猜中过了,请重新猜\n')
    elif res :
        print('猜对了,请继续猜测其他字母\n')
        lives -= 1
        correct_set.add(guess)
        answer = random.choice(answers)  # 更换谜底
    else :
        print('\u26A1\u2708 猜错了,请重新猜\n')
        lives -= 1

    if lives == 0:
        print('游戏结束,共猜中 ' + str(len(correct_set)) + ' 次')

