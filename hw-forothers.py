print("企管1, 311057012, 黃子峻")
a = int(input('請輸入購物金額: '))

if a < 5000:
    # 打95折
    p = round(a * 95/100, 1)
    d = round(a - p, 1)
    print("折扣數為: 95 折")
    print("折扣金額為: " + str(d))
    print("實付金額為: " + str(p))

elif a < 8000:
    # 打9折
    p = round(a * 90/100, 1)
    d = round(a - p, 1)
    print("折扣數為: 9 折")
    print("折扣金額為: " + str(d))
    print("實付金額為: " + str(p))

elif a < 10000:
    # 打85折
    p = round(a * 85/100, 1)
    d = round(a - p, 1)
    print("折扣數為: 85 折")
    print("折扣金額為: " + str(d))
    print("實付金額為: " + str(p))    

elif a < 20000:
    # 打8折
    p = round(a * 80/100, 1)
    d = round(a - p, 1)
    print("折扣數為: 8 折")
    print("折扣金額為: " + str(d))
    print("實付金額為: " + str(p)) 

elif a < 30000:
    # 打75折
    p = round(a * 75/100, 1)
    d = round(a - p, 1)
    print("折扣數為: 75 折")
    print("折扣金額為: " + str(d))
    print("實付金額為: " + str(p))   

else:
    # 打7折
    p = round(a * 70/100, 1)
    d = round(a - p, 1)
    print("折扣數為: 7 折")
    print("折扣金額為: " + str(d))
    print("實付金額為: " + str(p))