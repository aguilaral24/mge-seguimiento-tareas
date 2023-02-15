import logging
#COnfigure logging
logging.basicConfig(
    filename='../logs/Tests.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


"""
import libraries
"""
import pandas as pd

def read_trainning_data():
    '''
        Read trainninig  data from csv
        
        params: NA

        outputs:
             - trainning data as data frame
    '''
    train_data = pd.DataFrame()
    
    try:
        train_data = pd.read_csv("../data/train.csv")
    except FileNotFoundError as e:
        logging.error("./data/train.csv was not found ")
        logging.debug(e)
    
    return train_data



def read_testing_data():
    '''
        Read testing  data from csv
        
        params: NA

        outputs:
             - testing data as data frame
    '''
    test_data = pd.DataFrame()

    try:
        test_data = pd.read_csv("../data/test.csv")
    except FileNotFoundError as e:
        logging.error("./data/test.csv was not found ")
        logging.debug(e)

    return test_data

def fill_missings_with_No(df,col_names):
    '''
        Fill missing data with the word No
        
        params:
            - data frame
            - array of colum names
        
        output:
            - NA
    '''

    try:
        for col in col_names:

            df[col].fillna("No", inplace=True)
    except:
        logging.error(f'Error while trying to fill missings with "No" in column: {col}')

    return df



def fill_all_missing_values(data):
    """
        Impute missings with mean and mode

        Params:
            -data: data set to impute
    """
    for col in data.columns:
        if data[col].dtype in ('float64', 'int64'):
            try:
                data[col].fillna(data[col].mean(), inplace=True)
            except Exception as e:
                logging.error('Error while imputing data')
                logging.debug(e)
        else:
            try:
                data[col].fillna(data[col].mode()[0], inplace=True)
            except Exception as e:
                logging.error('Error while imputing data')
                logging.debug(e)
    return data
