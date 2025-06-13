numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("数字を入力してください(qで終了).")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("正解")
    else:
        print("不正解!")
