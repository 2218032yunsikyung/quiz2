#환율
exchange_rate = {"달러":1320,"엔":950,"위안":182}

#철수가 가지고 있는 돈
money = [13, 200, 13]

#환전
total = (exchange_rate["달러"]*money[0]+exchange_rate["엔"]*money[1]+exchange_rate["위안"]*money[2])

#철수가 가지고 있는 원화의 가치
print("철수가 가지고 있는 돈의 원화 가치는 ",total,"입니다.")
