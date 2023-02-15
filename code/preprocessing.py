import logging
#Configure logging
logging.basicConfig(
    filename='../logs/T_03-preprocessing.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

"""
import libraries
"""
import pandas as pd
import seaborn as sns
from functions import read_trainning_data, read_trainning_data,fill_missings_with_No,fill_all_missing_values

# Preprocessing
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

logging.info('*****Beggining of preprocessing*****')

# Load data
train_data = pd.DataFrame()
train_data = read_trainning_data()
test_data = pd.DataFrame()
test_data = read_trainning_data()

logging.info('Preprocessing-Filling missing data. with "No"...')
# Fill missing data
colNames=['FireplaceQu','BsmtQual','BsmtCond','BsmtFinType1','BsmtFinType2']
fill_missings_with_No(train_data,colNames)


logging.info({'Preprocessing-Imputing missing values with mean and mode...'})
fill_all_missing_values(train_data)
fill_all_missing_values(test_data)

logging.info('Preprocessing-Dropping unwanted data...')
# drop unwanted data
drop_col = ['Id', 'Alley', 'PoolQC', 'MiscFeature', 'Fence', 'MoSold',
            'YrSold', 'MSSubClass', 'GarageType', 'GarageArea', 'GarageYrBlt',
            'GarageFinish', 'YearRemodAdd', 'LandSlope', 'BsmtUnfSF',
            'BsmtExposure', '2ndFlrSF', 'LowQualFinSF', 'Condition1',
            'Condition2', 'Heating', 'Exterior1st', 'Exterior2nd',
            'HouseStyle', 'LotShape', 'LandContour', 'LotConfig',
            'Functional', 'BsmtFinSF1', 'BsmtFinSF2', 'FireplaceQu',
            'WoodDeckSF', 'GarageQual', 'GarageCond', 'OverallCond']
try:
    train_data.drop(drop_col, axis=1, inplace=True)
except Exception as e:
                logging.error('Error while dropping data in train_data')
                logging.debug(e)
try:
    test_data.drop(drop_col, axis=1, inplace=True)
except Exception as e:
                logging.error('Error while dropping data in test_data')
                logging.debug(e)

logging.info('Preprocessing-Transforming data...')
# Preprocessing
ordinal_col = ['GarageQual', 'GarageCond', 'BsmtQual', 'BsmtCond',
               'ExterQual', 'ExterCond', 'KitchenQual', 'FireplaceQu',
               'PavedDrive', 'Functional', 'Electrical', 'Heating',
               'BsmtFinType1', 'BsmtFinType2', 'Utilities']


def transform_data(categoriesv, col):
    '''
        Categorize a column of data set

        params:
            categories: list of categories
            col: column to be transformed
    '''
    #o_encoder = OrdinalEncoder(categoresv)
    o_encoder = OrdinalEncoder()
    train_data[col] = o_encoder.fit_transform(train_data[[col]])
    test_data[col] = o_encoder.transform(test_data[[col]])


categories = [['No', 'Po', 'Fa', 'TA', 'Gd', 'Ex']]
col=''
try:
    col='BsmtQual'
    transform_data(categories,col)

    col='BsmtCond'
    transform_data(categories, col)

    categories = [['Po', 'Fa', 'TA', 'Gd', 'Ex']]
    col='ExterQual'
    transform_data(categories, col)

    col='ExterCond'
    transform_data(categories, col)

    col='KitchenQual'
    transform_data(categories, col)

    categories = [['N', 'P', 'Y']]
    col='PavedDrive'
    transform_data(categories, col)

    categories = [['Mix', 'FuseP', 'FuseF', 'FuseA', 'SBrkr']]
    col='Electrical'
    transform_data(categories, col)

    categories = [['No', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ']]
    col='BsmtFinType1'
    transform_data(categories, col)

    categories = [['No', 'Unf', 'LwQ', 'Rec', 'BLQ', 'ALQ', 'GLQ']]
    col='BsmtFinType2'
    transform_data(categories, col)

    categories = [['ELO', 'NoSeWa', 'NoSewr', 'AllPub']]
    col='Utilities'
    transform_data(categories, col)

    categories = [['C (all)', 'RH', 'RM', 'RL', 'FV']]
    col='MSZoning'
    transform_data(categories, col)

    categories = [['Slab', 'BrkTil', 'Stone', 'CBlock', 'Wood', 'PConc']]
    col='Foundation'
    transform_data(categories, col)

    categories = [['MeadowV', 'IDOTRR', 'BrDale', 'Edwards',
                'BrkSide', 'OldTown', 'NAmes', 'Sawyer',
                'Mitchel', 'NPkVill', 'SWISU', 'Blueste',
                'SawyerW', 'NWAmes', 'Gilbert', 'Blmngtn',
                'ClearCr', 'Crawfor', 'CollgCr', 'Veenker',
                'Timber', 'Somerst', 'NoRidge', 'StoneBr',
                'NridgHt']]
    col='Neighborhood'
    transform_data(categories, col)

    categories = [['None', 'BrkCmn', 'BrkFace', 'Stone']]
    col='MasVnrType'
    transform_data(categories, col)

    categories = [['AdjLand', 'Abnorml', 'Alloca', 'Family',
                'Normal', 'Partial']]
    col='SaleCondition'
    transform_data(categories, col)

    categories = [['Gambrel', 'Gable', 'Hip', 'Mansard', 'Flat', 'Shed']]
    col='RoofStyle'
    transform_data(categories, col)

    categories = [['ClyTile', 'CompShg', 'Roll', 'Metal',
                'Tar&Grv', 'Membran', 'WdShake', 'WdShngl']]
    col='RoofMatl'
    transform_data(categories, col)
except Exception as e:
                logging.error(f'Error while transforming data,col {col} ')
                logging.debug(e)

Level_col = ['Street', 'BldgType', 'SaleType', 'CentralAir']

encoder = LabelEncoder()


def encode_catagorical_columns(train, test):
    '''
        Encode categorical columns

        params:
            train: trainning set
            test: testing set
    '''
    for col in Level_col:
        train[col] = encoder.fit_transform(train[col])
        test[col] = encoder.transform(test[col])

logging.info('Preprocessing-Encoding categorical columns...')

try:
    encode_catagorical_columns(train_data, test_data)
except Exception as e:
                logging.error(f'Error while encoding categorical columns')
                logging.debug(e)


logging.info('Preprocessing-Applying variable engineering...')
# TRaining data
train_data['BsmtRating'] = train_data['BsmtCond'] * train_data['BsmtQual']
train_data['ExterRating'] = train_data['ExterCond'] * train_data['ExterQual']
train_data['BsmtFinTypeRating'] = train_data['BsmtFinType1'] *\
                                  train_data['BsmtFinType2']

train_data['BsmtBath'] = train_data['BsmtFullBath'] +\
                         train_data['BsmtHalfBath']
train_data['Bath'] = train_data['FullBath'] + train_data['HalfBath']
train_data['PorchArea'] = train_data['OpenPorchSF'] +\
                          train_data['EnclosedPorch'] +\
                          train_data['3SsnPorch'] + train_data['ScreenPorch']

test_data['BsmtRating'] = test_data['BsmtCond'] * test_data['BsmtQual']
test_data['ExterRating'] = test_data['ExterCond'] * test_data['ExterQual']
test_data['BsmtFinTypeRating'] = test_data['BsmtFinType1'] *\
                                 test_data['BsmtFinType2']

test_data['BsmtBath'] = test_data['BsmtFullBath'] + test_data['BsmtHalfBath']
test_data['Bath'] = test_data['FullBath'] + test_data['HalfBath']
test_data['PorchArea'] = test_data['OpenPorchSF'] +\
                         test_data['EnclosedPorch'] +\
                         test_data['3SsnPorch'] + test_data['ScreenPorch']

drop_col = ['OverallQual',
            'ExterCond', 'ExterQual',
            'BsmtCond', 'BsmtQual',
            'BsmtFinType1', 'BsmtFinType2',
            'HeatingQC',
            'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch',
            'BsmtFullBath', 'BsmtHalfBath',
            'FullBath', 'HalfBath']

train_data.drop(drop_col, axis=1, inplace=True)
test_data.drop(drop_col, axis=1, inplace=True)

print(train_data.shape)

logging.info('Writting cleaned data...')
train_data.to_csv("../data/cleaned_train.csv", index=False)
test_data.to_csv("../data/cleaned_test.csv", index=False)

logging.info('*****End of preprocessing*****')