print("請輸入西元年")
year=int(input())
if(year%400==0 or year%4==0 and year%100!=0):
    print("閏年")
else:
    print("平年")
#西元年被4整除且不被100整除，或被400整除者即為閏年