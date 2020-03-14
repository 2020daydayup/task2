import re

list_memo = []
count = 1
while True:

    dict_memo = {}
    print("欢迎使用51备忘录".center(30,'-'))
    data = input("请输入信息（例：3.14，学python基础，3个小时）:\n")

    date,thing,remark = re.split(r',|，',data)
    dict_memo["id"] = count
    dict_memo["日期"] = date
    dict_memo["事情"] = thing
    dict_memo["备注"] = remark

    list_memo.append(dict_memo)
    for i in list_memo:
        print(f"\033[32;0m{i['日期']},\033[1;32;40m{i['事情']},\033[1;31m{i['备注']}")

    count += 1
    if input("\033[0m是否继续（q退出，任意键继续）") == 'q':
        break