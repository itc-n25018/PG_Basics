answer = input("好きな食べ物はなんですか？")
with open("food.txt", "w") as f:
    f.write(answer)
