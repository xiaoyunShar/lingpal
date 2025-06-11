import pandas as pd
import json

# 读取 Excel 文件
df = pd.read_excel('fifthweek_text.xlsx')

# 将数据转换为字典列表
data = df.to_dict('records')

# 将数据保存为 JSON 文件
with open('fifthweek_text.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("转换完成！") 