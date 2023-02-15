import logging
#COnfigure logging
logging.basicConfig(
    filename='../logs/T_03-model.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

"""
import libraries
"""
import pandas as pd
import seaborn as sns

# Model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

logging.info('*****Beggining of Modeling*****')
logging.info('MOdel-Loading cleaned data...')

# Load data
train_data = pd.DataFrame()
test_data = pd.DataFrame()

try:
    train_data = pd.read_csv("../data/cleaned_train.csv")
except FileNotFoundError as e:
  logging.error("../data/cleaned_train.csv was not found ")
  logging.debug(e)

try:
    test_data = pd.read_csv("../data/test.csv")
except FileNotFoundError as e:
  logging.error("../data/test.csv was not found ")
  logging.debug(e)
test_ids = test_data['Id']


try:
    test_data = pd.read_csv("../data/cleaned_test.csv")
except FileNotFoundError as e:
  logging.error("../data/cleaned_test.csv was not found ")
  logging.debug(e)


# Model
y = train_data['SalePrice']
X = train_data.drop(['SalePrice'], axis=1)

candidate_max_leaf_nodes = [250]
# model = LinearRegression()

logging.info('Model-Building model')
try:
    for node in candidate_max_leaf_nodes:
        model = RandomForestRegressor(max_leaf_nodes=node,)
        model.fit(X, y)
        score = cross_val_score(model, X, y, cv=10)
        print(score.mean())
except Exception as e:
        logging.error('Error: Random Forest Regressor could not be built')
        logging.debug(e)


# Output
price = model.predict(test_data)
submission = pd.DataFrame({
    "Id": test_ids,
    "SalePrice": price
})

logging.info('MOdel-Writring predictions to csv...')
submission.to_csv("../data/submission.csv", index=False)
submission.sample(10)

logging.info('*****End of preprocessing*****')