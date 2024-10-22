import json
import os

print("此程式用於判斷體脂健康範圍，或是查詢先前記錄的資料。") #告知程式用途
choose=input("判斷健康範圍請輸入0，查詢資料請輸入1。[0/1]：") #選擇功能
if(choose=="0"): #判斷健康範圍
    name=str(input("請輸入姓名："))
    gender=input("男生輸入0，女生輸入1。\n請輸入你的性別[0/1]：") #性別判斷，男0女1
    bodyFat=input("請輸入你的體脂率（不用加%）：")
    if(bodyFat.isdigit()==1): #體脂輸入正確，開始後續內容
        if(gender=="1"): #女生
            bodyFat=int(bodyFat)
            if(bodyFat<10):
                print("這體脂好像怪怪的?")
            elif(bodyFat>=10 and bodyFat<=13):
                print("基礎體脂")
            elif(bodyFat>=14 and bodyFat<=20):
                print("運動員體脂")
            elif(bodyFat>=21 and bodyFat<=24):
                print("健康體脂")
            elif(bodyFat>=25 and bodyFat<=31):
                print("正常體脂")
            elif(bodyFat>=32):
                print("肥胖體脂")
        elif(gender=="0"): #男生
            bodyFat=int(bodyFat)
            if(bodyFat<2):
                print("這體脂好像怪怪的?")
            elif(bodyFat>=2 and bodyFat<=5):
                print("基礎體脂")
            elif(bodyFat>=6 and bodyFat<=13):
                print("運動員體脂")
            elif(bodyFat>=14 and bodyFat<=17):
                print("健康體脂")
            elif(bodyFat>=18 and bodyFat<=24):
                print("正常體脂")
            elif(bodyFat>=25):
                print("肥胖體脂")
        
        choose=input("\n是否要將資料寫入json檔案？\n否請輸入0，是請輸入1[0/1]：")
        if(choose=="1"):
            #將資料寫入json檔案
            info={
                "name":name,
                "sex":gender,
                "bodyFat":bodyFat
            }
            # 檢查檔案是否存在
            if not os.path.exists("data.json"):
                # 如果檔案不存在，創建一個新的檔案並初始化為一個空的json陣列
                with open("data.json", "w") as infofile:
                    json.dump([], infofile)
            with open("data.json","r") as infofile:
                data=json.load(infofile)
                new_content={
                    "name":name,
                    "sex":gender,
                    "bodyFat":bodyFat
                }
            # 檢查是否已經存在具有相同 name 的資料
            found = False
            for item in data:
                if item["name"] == name:
                    item["bodyFat"] = bodyFat
                    found = True
                    break
            # 如果不存在，則新增新的資料
            if not found:
                data.append(new_content)

            with open("data.json", "w") as infofile:
                json.dump(data, infofile, indent=4)
            
            print("資料已儲存。")
        else:
            print("無儲存資料。")
    else:
        print("輸入的體脂率錯誤，程式結束。") #體脂輸入錯誤，結束程式

else:
    #查詢資料
    name=str(input("請輸入姓名："))
    # 檢查檔案是否存在
    print("--------------------") #只是想弄個分隔線
    if not os.path.exists("data.json"):
        # 如果檔案不存在，創建一個新的檔案並初始化為一個空的json陣列
        with open("data.json", "w") as infofile:
            json.dump([], infofile)
    with open("data.json","r") as infofile:
        data=json.load(infofile)
        found = False
        for item in data:
            if item["name"] == name:
                print("姓名：", item["name"])
                print("性別：", "男" if item["sex"] == "0" else "女")
                print("體脂率：", item["bodyFat"], "%")
                found = True
                break
        if not found:
            print("資料不存在。")