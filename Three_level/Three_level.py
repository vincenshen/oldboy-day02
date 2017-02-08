#-*- coding:utf-8 -*-

china ={
    '四川':{
        '达州':['大竹','渠县','宣汉'],
        '德阳':['中江','罗江','强江'],
        '绵阳':['三台','平武','盐亭']
        },
    '广东':{
        '东莞':['南城','厚街','黄江'],
        '广州':['珠海','白云','越秀'],
        '珠海':['香洲','斗门','金湾']
        },
    '山东':{
        '青岛':['黄岛','崂山','城阳'],
        '济南':['历城','章丘','长青'],
        '烟台':['龙口','莱山','蓬莱']
        }
    }

def print_fun(p_name,p_list):
    print('%s'.center(30, '-') %p_name)
    for index, i in enumerate(p_list):
        print('%s.' %(index+1), i)

def choose_fun(location,choose_list):
    while True:
        if location == 'Province':choose = input("Please input number for choose list, or 'q' to quit:").strip()
        if location == 'City':choose = input("Please input number for choose list, or 'b' to back or 'q' to quit:").strip()
        if location == 'Country':choose = input("Please input 'b' to back or 'q' to quit:").strip()
        if choose.isdigit():
            choose =  int(choose)
            if choose > 0 and choose <= len(choose_list):return choose_list[choose - 1]
            else:print("Input Error! Please input again!")
        elif choose == 'b':
            return 'b'
        elif choose == 'q':
            exit()
        else:
            print('Input Error! Please input again!')

province_list = list(china.keys())  # 取字典第一层省份的值
while True:
    print_fun('Province',province_list)
    choose = choose_fun('Province',province_list)
    if choose == 'b':continue
    province_name = choose
    city_list = list(china[choose].keys())  # 取字典第二层城市的值
    while True:
        print_fun('City',city_list)
        choose = choose_fun('City',city_list)
        if choose == 'b':break
        country_list = china[province_name][choose]  # 取字典第三层区县的值
        while True:
            print_fun('Country',country_list)
            choose = choose_fun('Country',country_list)
            if choose == 'b':
                break
            else:
                print('Input Error! Please input again!')


