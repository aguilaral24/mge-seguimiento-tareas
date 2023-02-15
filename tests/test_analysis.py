'''
    import libraries
'''
import sys
import pandas as pd
import pytest

# adding Folder  to the system path
sys.path.insert(1, '../code')
from functions import read_testing_data, read_trainning_data,fill_missings_with_No, fill_all_missing_values

#___________________________________________________________________________#

def test_read_trainning_data():
    '''
        Verify that trainning data set could be read and is not empty
    '''
    assert(read_trainning_data().empty==False)

#___________________________________________________________________________#

def test_read_testing_data():
    '''
        Verify that testing data set could be read and is not empty
    '''
    assert(read_testing_data().empty==False)

#___________________________________________________________________________#

@pytest.fixture(scope="module")
def df():
    return read_trainning_data()
@pytest.fixture(scope="module")
def colNames():
    return ['FireplaceQu','BsmtQual','BsmtCond','BsmtFinType1','BsmtFinType2']

def test_fill_missings_with_No(df,colNames):
    '''
        Verify all missing values for certain columns were replaced with tge word "No"
    '''
    assert(fill_missings_with_No(df,colNames)[colNames].isnull().sum().sum()==0)

#___________________________________________________________________________#

def test_fill_all_missing_values(df):

    '''
        Verify all missing values were replaced with mean or mode depending on the type of column
    '''
    assert(fill_all_missing_values(df).isnull().sum().sum()==0)

#___________________________________________________________________________#
