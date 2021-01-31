import BMRS_helper as bmrs



df = bmrs.extract_data('FORDAYDEM', '2020-01-27', '2020-01-28')
print(df)

# df = bmrs.extract_data2('FORDAYDEM', '2020-01-27', '2020-01-28')
# print(df.head())

# df1 = bmrs.generation('2020-01-27', '2020-01-28')
# print(df1.head())

# df1 = bmrs.loss_of_load('2020-01-27', '2020-01-28')

# print(df1.head())
# print(df1.tail())


# df1 = bmrs.frequency('2020-01-27', '2020-01-28')
# print(df1.head())
# print(df1.describe())

# df1 = bmrs.initial_demand_transmission('2020-01-27', '2020-01-28')
# print(df1.head())
# print(df1.describe())

# if __name__ == "__main__":
#     print('a')

