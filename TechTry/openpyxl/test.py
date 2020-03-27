# 读取、创建、生成、追加
# 计算、数组
#

from openpyxl import Workbook, load_workbook
import numpy as np

wb = load_workbook('D:\OtherSource\PyCharm\CommonTools\TechTry\openpyxl\对接会信息导出.xlsx')
ws = wb.active

# ## 读取数据
# data = [[1] * 3 for i in range(2)]
# for i in range(0,2):
#     for j in range(0,1):
#         data[i][j] = i + j
#
zeros = np.zeros((3,4), dtype=int)
zeros_list = zeros.tolist()

for i in range(0, np.size(zeros, 0)):
    ws.append(zeros_list[i])

## 保存数据
wb.save('D:\OtherSource\PyCharm\CommonTools\TechTry\openpyxl\对接会信息导出.xlsx')

