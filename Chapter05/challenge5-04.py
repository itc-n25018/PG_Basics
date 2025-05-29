自分={
        "身長":"173",
        "好きな色":"青",
        "好きな食べ物":"カレーうどん"}

answer = input ("Type 身長 or 好きな色 or 好きな食べ物")
if answer in 自分:
    result = 自分[answer]
    print(result)
