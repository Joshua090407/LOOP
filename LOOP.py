x = 0
while x <= 3:
    pin = input('請輸入密碼')
    if  pin == ("12345678"):
        print('密碼正確')
        break
    elif x < 3:
        x = x + 1
        print ('密碼錯誤你還有', 4 - x ,'次機會')
    else:
        print('你沒機會了')
        break
