#-*- coding:utf-8 -*-

salary = int(input('Please input your salary:').strip())
product_list = [['iphone',6500],['macbook',12000],['iwatch',2200],['pythonbook',66],['bike',999]]
buy_list = []
while True:
    print('Product list'.center(30,'-'))
    for index, i in enumerate(product_list):
        print(index+1, i[0],'\t',i[1])    # index+1 将商品序号从1开始显示
    while True:
        choose = input("Please choose your want to buy or 'exit' to exit:").strip()
        if len(choose) == 0:
            continue
        else:
            break
    if choose.isdigit() and int(choose) <= len(product_list):
        choose = int(choose) - 1    # choose -1 将choose和商品列表元素相对应
        if salary >= product_list[choose][1]:
            salary = salary - product_list[choose][1]
            buy_list.append(product_list[choose])
            print('Buy Success! Your balance remaining \033[1;31m%d\033[0m!' %salary)
        else:
            print('Your balance insufficient! need \033[1;31m%d\033[0m!' %(product_list[choose][1] - salary))
    elif choose == 'exit':
        total_amount = 0
        print('Buy list'.center(30,'-'))
        for index,i in enumerate(buy_list):
            print(index+1,i[0],'\t',i[1])
            total_amount += i[1]
        print('Total_amount:\033[1;31m%d\033[0m, Your balance is \033[1;31m%d\033[0m!' %(total_amount,salary))
        break
    else:
        print('Input Error! Please input again!')