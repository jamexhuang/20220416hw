# amount: 用戶輸入的總金額 int
# pay: 打折後的金額 int
# discount_amount: 折扣額 str
# actural_pay: 實付款 str


print("企管1, 311057012, 黃子峻")

try:
    amount = int(input('請輸入購物金額: '))

    if amount < 0:
        print("金額不可小於0\n程式結束")
        exit(0)

    elif amount < 5000:
        #打95折
        pay = round(amount * 95/100,1)
        discount_amount = amount - pay
        print("折扣數為: 95 折")
        print("折扣金額為: " + str(discount_amount) + "\n實付金額為: " + str(pay))

    elif amount < 8000:
        #打9折
        pay = round(amount * 90/100,1)
        discount_amount = amount - pay
        print("折扣數為: 9 折")
        print("折扣金額為: " + str(discount_amount) + "\n實付金額為: " + str(pay))

    elif amount < 10000:
        #打85折
        pay = round(amount * 85/100,1)
        discount_amount = amount - pay
        print("折扣數為: 85 折")
        print("折扣金額為: " + str(discount_amount) + "\n實付金額為: " + str(pay))

    elif amount < 20000:
        #打8折
        pay = round(amount * 80/100,1)
        discount_amount = amount - pay
        print("折扣數為: 8 折")
        print("折扣金額為: " + str(discount_amount) + "\n實付金額為: " + str(pay))

    elif amount < 30000:
        #打75折
        pay = round(amount * 75/100,1)
        discount_amount = amount - pay
        print("折扣數為: 75 折")
        print("折扣金額為: " + str(discount_amount) + "\n實付金額為: " + str(pay))

    else:
        #打7折
        pay = round(amount * 70/100,1)
        discount_amount = amount - pay
        print("折扣數為: 7 折")
        print("折扣金額為: " + str(discount_amount) + "\n實付金額為: " + str(pay))

except ValueError:
    print("只能輸入數字")