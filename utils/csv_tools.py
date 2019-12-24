import pandas as pd

train = pd.read_csv('../resources/datas/kc_train.csv', names=range(1, 15))
test = pd.read_csv('../resources/datas/kc_test.csv', names=range(1, 14))

# df = pd.DataFrame

# get some columns
# df_train_2d = (train.loc[:, [9, 2]])

# remove row
# df_train_2d.drop([0], inplace=True)

# rename columns
# df_train_2d.rename(columns={9: None, 2: None}, inplace=True)

# 2d data
train.to_csv(path_or_buf='../resources/datas/train_2d.csv', columns=[9, 2], encoding='utf-8', header=False, index=False)
test.to_csv(path_or_buf='../resources/datas/test_2d.csv', columns=[8], encoding='utf-8', header=False, index=False)

# 3d data
train.to_csv(path_or_buf='../resources/datas/train_3d.csv', columns=[9, 3, 2], encoding='utf-8', header=False, index=False)
test.to_csv(path_or_buf='../resources/datas/test_3d.csv', columns=[8, 2], encoding='utf-8', header=False, index=False)
