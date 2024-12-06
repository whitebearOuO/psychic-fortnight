food = ['無', '漢堡', '米漢堡']
side = ['無', '薯條', '沙拉']
drink = ['無', '可樂', '紅茶']
price = {'無': 0, '漢堡': 60, '米漢堡': 80, '薯條': 30, '沙拉': 45, '可樂': 20, '紅茶': 15}
calories = {'無': 0, '漢堡': 500, '米漢堡': 450, '薯條': 300, '沙拉': 150, '可樂': 200, '紅茶': 100}
cart = []

global BILL, TOTAL_CALORIEES
BILL = 0
TOTAL_CALORIEES = 0

# 菜單顯示
def display_menu(items):
    for i in range(len(items)):
        print(i, ":", items[i])

# 新增購物車
def add_to_cart(category, selection):
    global BILL, TOTAL_CALORIEES
    cart.append(category[selection])
    BILL += price[category[selection]]
    TOTAL_CALORIEES += calories[category[selection]]

while 1:
    # 主餐選擇
    display_menu(food)
    num = int(input('請選擇主餐:'))
    add_to_cart(food, num)
    print('當前價格:', BILL)
    print('當前熱量:', TOTAL_CALORIEES)
    print('購物車內容:', cart)
    print()

    # 副餐選擇
    display_menu(side)
    num = int(input('請選擇副餐:'))
    add_to_cart(side, num)
    print('當前價格:', BILL)
    print('當前熱量:', TOTAL_CALORIEES)
    print('購物車內容:', cart)
    print()

    # 飲料選擇
    display_menu(drink)
    num = int(input('請選擇飲料:'))
    add_to_cart(drink, num)
    print('當前價格:', BILL)
    print('當前熱量:', TOTAL_CALORIEES)
    print('購物車內容:', cart)
    print()

    # 詢問是否繼續點餐
    continue_order = input('是否繼續點餐？(y/n): ')
    if continue_order != 'y' or continue_order != 'Y':
        break

print('最終價格:', BILL)
print('最終熱量:', TOTAL_CALORIEES)
print('最終購物車內容:', cart)
print('謝謝惠顧！')