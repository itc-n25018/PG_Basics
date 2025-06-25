import random

def janken():
    janken_list = ["グー", "チョキ", "パー"]
    random_number = random.randint(0, 2)
    computer = janken_list[random_number]

    print("グー、チョキ、パーを選んでください")
    player = input("あなたの手：")

    print(f"コンピュータ：{computer}")
    print(f"あなた：{player}")

    # 勝敗判定
    if player == computer:
        print("あいこです")
    elif (
        (player == "グー" and computer == "チョキ") or
        (player == "チョキ" and computer == "パー") or
        (player == "パー" and computer == "グー")
    ):
        print("あなたの勝ち！")
    else:
        print("あなたの負け…")

# 関数を実行
janken()

