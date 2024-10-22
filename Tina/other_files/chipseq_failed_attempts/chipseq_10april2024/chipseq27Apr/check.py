import pandas as pd

# 尝试读取文件
try:
    df = pd.read_csv('count_table_updated.txt', sep='\t')
    print(df.head())  # 打印前五行数据来查看
except Exception as e:
    print("Error reading the file:", e)

