import pandas as pd

world_df = pd.read_csv('data/world.csv', index_col=0)

# 도시와 나라 갯수
print(world_df['City / Urban area'].value_counts().shape)
print(world_df['Country'].value_counts().shape)

# 인구 밀도 10000명이 넘는 도시 갯수
# 인구 밀도 = 인구 수 / 땅의 면적
'''
density = world_df['Population'] / world_df['Land area (in sqKm)']
print((density>10000).value_counts())
'''

world_df['density'] = world_df['Population'] / world_df['Land area (in sqKm)']

world_df_high = world_df[world_df['density']>10000]
print(world_df_high.info())

# 인구 밀도가 가장 높은 도시
print(world_df.sort_values(by='density', ascending=False))

# 데이터 4개만 나온 도시

country = world_df['Country'].value_counts()
print(country[country==4])  # 조건문