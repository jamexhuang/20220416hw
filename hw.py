#amount: 用戶輸入的總金額 Int
#discount: 折扣金額 Str
#pay: 實付款

print("企管1, 311057012, 黃子峻")
amount = int(input('請輸入購物金額:'))

if amount < 5000:
    pay = int(amount * 95/100)
    discount = str(amount - pay)
    print("折扣數為: 95 折")
    print("折扣金額為:" + discount)
    print(pay)
    print(discount)
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
print()
