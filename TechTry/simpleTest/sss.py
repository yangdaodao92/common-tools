import glob
import os
import time
import datetime
from os.path import join, normpath
import json
import math
import getpass
import shutil

# s1 = [1, 2, 3]
# s2 = [3, 4, 5]
#
# list3 = [i for i in s1 if i not in s2]
# for i, ss in enumerate(list3):
#     print(i)
#
# o = b' Tomcat Restart Success! --------------'
# print(str(o, 'utf-8'))
#
# searchedfile = glob.glob("../replaceFiles/*")
# # files = sorted(searchedfile, key=lambda file: os.path.getctime(file))
# searchedfile.sort(key=os.path.getctime)
#
# for file in searchedfile:
#     print("{} - {}".format(file.split('\\')[-1], time.ctime(os.path.getctime(file))))
#
# print(normpath(join(__file__, '..', '..')))  # D:\OtherSource\PyCharm\Example1
#
# print(len(s1))
#
# # file1 = open(os.path.abspath('../test.txt'), 'r')
# # # file1.write(json.dumps({'aa': 11, 'bb': 22, 'a': [33, 44, 55]}, indent=4))
# # json_dict = json.loads(file1.read())
# # print(json_dict)
# # file1.close()
#
# print(os.path.exists('../dict'))
#
# a = b'1234'
# print(a.find(b'3'))
# print(a[:3])
# print(a[5:])

# ss = bytes("未发现.class文件，无需重启tomcat", encoding='utf-8')
# print(str(ss, 'utf-8'))

# ss = datetime.struct_time
#
# print(time.strftime('%Y-%m-%d_%H:%M:%S', time.struct_time))
# print(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
#
# print(math.ceil(29 / 2))
#
print(getpass.getuser())


# for i, text in enumerate(range(9)):
#     array = [''] * 9
#     array[i] = text
#     print(array)
#
# shutil.copyfile('G:\ceshi\waterdrop-common-1.0.0-20180816.095617-107.jar', 'G:\ceshi2\est.jar')

shutil.rmtree('E:\Works\ReplaceProject\\')



