import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

# 1. 伪装头部（基础反爬）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 2. 爬取数据（这里用伪代码逻辑代表爬取过程）
data_list = []
# 假设我们要爬5页数据
for page in range(1, 6):
    url = f"https://example-market.com/search?q=吉他&page={page}"
    # response = requests.get(url, headers=headers).text
    # soup = BeautifulSoup(response, 'html.parser')

    # 模拟抓取到的数据（实际中通过CSS选择器提取）
    # 比如 items = soup.find_all('div', class_='item-card')

    # 模拟数据生成
    for _ in range(20):
        # 模拟出大量带灰尘的脏数据，比如卖家乱标价（1元或99999元）
        mock_price = random.choice([50, 150, 200, 250, 300, 9999, 1, 180, "面议"])
        mock_title = "九成新雅马哈吉他 / Python基础教程 / 99新..."
        mock_location = random.choice(["苏州", "上海", "北京", "广州", "杭州"])
        data_list.append({"title": mock_title, "price": mock_price, "location": mock_location})

    time.sleep(random.uniform(1, 3))  # 随机休眠，防止被封IP

# 3. 数据清洗与处理（这是信计专业的核心优势！）
df = pd.DataFrame(data_list)
print(f"爬取原始数据量：{len(df)}条")

# 清理：把"面议"等非数字价格转为空值，强制转为浮点数
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 剔除缺失值和极端异常值（比如低于10元，高于5000元的，大概率是乱标价或引流）
df_clean = df.dropna(subset=['price'])
df_clean = df_clean[(df_clean['price'] >= 10) & (df_clean['price'] <= 5000)]
print(f"清洗后有效数据量：{len(df_clean)}条")

# 4. 统计分析
avg_price = df_clean['price'].mean()
median_price = df_clean['price'].median()
print(f"该商品平均价：{avg_price:.2f}元，中位数价格：{median_price}元")

# 按城市统计均价
city_stats = df_clean.groupby('location')['price'].mean().sort_values(ascending=False)
print("各城市均价对比：\n", city_stats)

# 5. 数据可视化（导出图表放到简历作品集里）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.figure(figsize=(10, 5))
df_clean['price'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.title('二手商品价格分布直方图（清洗后）')
plt.xlabel('价格 (元)')
plt.ylabel('数量')
plt.savefig('price_distribution.png')
plt.show()