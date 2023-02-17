import logging
#COnfigure logging
logging.basicConfig(
    filename='../logs/eda.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

"""
import libraries
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from functions import read_trainning_data, read_trainning_data

logging.info('*****Beggining EDA*****')
logging.info('Preprocessing-Loading data...')

# Load data
train_data = pd.DataFrame()
train_data = read_trainning_data()
test_data = pd.DataFrame()
test_data = read_trainning_data()

test_data.head()
logging.info('Preprocessing-Getting shape an duplicated data')
test_ids = test_data['Id']
print("Shape:", train_data.shape)
print("Duplicated data :", train_data.duplicated().sum())


logging.info('Preprocessing-Displaying plots')
# EDA
fig, ax = plt.subplots(figsize=(25, 10))
sns.countplot(x=train_data['SaleCondition'])
sns.histplot(x=train_data['SaleType'], kde=True, ax=ax)
sns.violinplot(x=train_data['HouseStyle'], y=train_data['SalePrice'], ax=ax)
sns.scatterplot(x=train_data["Foundation"],
                y=train_data["SalePrice"], palette='deep', ax=ax)
plt.grid()

logging.info('*****End of EDA*****')
