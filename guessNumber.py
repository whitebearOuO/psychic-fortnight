import random
import json
import os

# 生成答案0到100隨機一個數字
answer = random.randint(0, 100)

# 將答案記入data.json 檔案
with open("data.json", "w") as infofile:
    json.dump({"answer": answer}, infofile)

print("來猜數字，數字範圍是1~100。")

while 1: #猜對再break
    userInput = int(input("請輸入一個數字："))

    #讀取data.json
    with open("data.json", "r") as infofile:
        data = json.load(infofile)

    # 檢查userInput是否存在
    if "userInput" in data: #存在就加在尾巴
        data["userInput"].append(userInput)
    else: #不存在就直接新增
        data["userInput"] = [userInput]

    # 將更新後的資料寫回到 data.json 檔案
    with open("data.json", "w") as infofile:
        json.dump(data, infofile)

    if userInput == answer:
        print("恭喜你猜對ㄌ！")
        print("--------------------")
        break
    elif userInput > answer:
        print("再猜小一點看看。\n")
    else:
        print("再猜大一點看看。\n")