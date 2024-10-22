height=float(input("請輸入你的身高："))
weight=float(input("請輸入你的體重："))
bmi= round(weight/((height/100)**2),1) #輸出到小數第一位
if(bmi<18.5):
    print("體重過輕，bmi是：",bmi)
elif(bmi>=24):
    print("體重過重，bmi是：",bmi)
else:
    print("體重正常，bmi是：",bmi)