import random

user1 = input("请输入玩家1姓名：")
user2 = input("请输入玩家2姓名：")

dict_user1 = {}
dict_user2 = {}
user1_wins = 0
user2_wins = 0

while True:

    list_user1 = []
    list_user2 = []

    user1_card1 = input(f"请玩家 {user1}猜一个数：")
    user2_card1 = input(f"请玩家 {user2}猜一个数：")
    list_user1.append(int(user1_card1))
    list_user2.append(int(user2_card1))

    for i in range(2):
        list_user1.append(random.randint(1,9))
        list_user2.append(random.randint(1,9))

    print(f"{user1}的牌为：{list_user1} = {sum(list_user1)}")
    print(f"{user2}的牌为：{list_user2} = {sum(list_user2)}")

    if abs(21 - sum(list_user1)) < abs(21 - sum(list_user2)):
        user1_wins += 1
        print(f"{user1}赢")
    elif abs(21 - sum(list_user1)) > abs(21 - sum(list_user2)):
        user2_wins += 1
        print(f"{user2}赢")

    dict_user1[user1] = user1_wins
    dict_user2[user2] = user2_wins

    print(dict_user1)
    print(dict_user2)

    if input("是否继续（q退出，任意键继续）") == 'q':
        break
