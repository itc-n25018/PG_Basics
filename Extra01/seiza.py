def get_zodiac(month, day):
    if   (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "みずがめ座"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "うお座"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "おひつじ座"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "おうし座"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "ふたご座"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "かに座"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "しし座"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "おとめ座"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "てんびん座"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "さそり座"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "いて座"
    else:
        return "やぎ座"

def main():
    print("誕生日を入力してください")
    try:
        month = int(input("月: "))
        day = int(input("日: "))
        
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            print("正しい日付を入力してください")
            return

        zodiac = get_zodiac(month, day)
        print(f"あなたの星座は{zodiac}です")
    except ValueError:
        print("数字を入力してください。")

# 実行
main()

