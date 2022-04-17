# amount: 用戶輸入的總金額 int
# pay: 打折後的金額 int
# discount_amount: 折扣額 str
# actural_pay: 實付款 str

print("企管1, 311057012, 黃子峻")
try:
    amount = int(input('請輸入購物金額: '))

    if amount < 0:
        print("金額不可小於0\n程式結束")
        exit()
    elif amount < 5000:

        pay = float(amount * 95/100)
        actural_pay = str(pay)
        discount_amount = str(amount - pay)
        print("折扣數為: 95 折")
        print("折扣金額為: " + discount_amount + "\n實付金額為: " + actural_pay)

    elif amount < 8000:
        print(amount * 90/100)
    elif amount < 10000:
        print(amount * 80/100)
    elif amount < 20000:
        print(amount * 80/100)
    elif amount < 30000:
        print(amount * 80/100)
    else:
        print(amount * 70/100)

except ValueError:
    print("只能輸入數字")