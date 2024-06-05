from bank import Account

jc_personal = Account('Jean-Christophe Clouet', 200.70)

jc_profesional = Account('Jean-Christophe Clouet', 20.42)
jc_profesional.withdraw(4.20, 'babycarrots-wrap-schokomilk')
print(jc_profesional.balance)


jc_personal.withdraw(50, 'amazon card')
jc_personal.withdraw(10, 'lunch')


# test = Account('Bob', 150)
# print(test.balance)
# test.deposit(20, 'grandma gift')
# print(test.balance)
# test.withdraw(50, 'video games')
# print(test.balance)
# test.create_balance()