# -*- coding:utf-8 -*-
import sys,os,re,datetime

help_info = '''
info:
该程序支持正则表达式进行查找和替换

commands:
-h                                 获取帮助信息
-f <str> <file_name>               全文查找字符串
-r <old_str> <new_str> <file_name>     全文替换字符串
'''
def find_func(input_str,file_name):
    with open(file_name, 'r') as f:
        count = 0  # 统计行数
        for line in f.readlines():
            count += 1
            find_str = re.findall(input_str, line)
            if find_str:
                print('在第%d行中查找到了%s' % (count, find_str))

def replace_func(input_str1,input_str2,file_name):
    bak_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 以当前时间来生成文件名，防止生成的临时文件重名
    with open(file_name, 'r') as f:
        count = 0  # 统计行数
        for line in f.readlines():
            count += 1
            find_str = re.findall(input_str1, line)
            if find_str:
                print('在第%d行中替换了%s' % (count, find_str))
            with open(bak_file, 'a+') as f2:
                f2.write(re.sub(input_str1, input_str2, line))
    os.remove(file_name)
    os.rename(bak_file, file_name)

input_func = sys.argv[1]
if input_func == '-h':
    print(help_info)
elif input_func == '-f':
    input_str = sys.argv[2]
    file_name = sys.argv[3]
    find_func(input_str,file_name)
elif input_func == '-r':
    input_str1 = sys.argv[2]
    input_str2 = sys.argv[3]
    file_name = sys.argv[4]
    replace_func(input_str1,input_str2,file_name)
else:
    print('参数错误！')


