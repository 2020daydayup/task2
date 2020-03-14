while True:

    exchange_rate = 7.0036
    rate = 0.9144
    print("欢迎使用单位转换器".center(30, '-'))
    select = input("请选择转换类型\n温度：t\n汇率：e\n长度：len\n")

    if select == 't':
        value = input("请输入数据\n1摄氏度：1c\n1华氏度：1f\n")
        num = int(value[:-1])
        if 'c' in value:
            result = round(num * (9 / 5) + 32, 4)
            print(f"{value} = {str(result)}华氏度(°F)")
        else:
            result = round((num - 32) * (5 / 9), 4)
            print(f"{value} = {str(result)}摄氏度(°C)")

    if select == 'e':
        value = input("请输入数据\n1人民币：￥1\n1美元：$1\n")
        num = int(value[1:])
        if '￥' in value:
            result = round(num / exchange_rate, 4)
            print(f"{value} = ${str(result)}")
        else:
            result = round(num * exchange_rate, 4)
            print(f"{value} = ￥{str(result)}")

    if select == 'len':
        value = input("请输入数据\n1米：1m\n1码：1y\n")
        num = int(value[:-1])
        if 'm' in value:
            result = round(num / rate, 4)
            print(f"{value} = {str(result)}码(y)")
        else:
            result = round(num * rate, 4)
            print(f"{value} = {str(result)}码(yd)")
    
    if input("是否继续（q退出，任意键继续）") == 'q':
        break