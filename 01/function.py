'''
함수
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance > money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금을 실패하였습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    comission = 100 # 수수료
    return comission, balance - money - comission        

balance = 0
balance = deposit(balance, 1000)

# balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
comission, balance = withdraw_night(balance , 500)

print(balance)