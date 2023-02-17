import logging
#COnfigure logging
logging.basicConfig(
    filename='../logs/log.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

"""
import libraries
"""

logging.info('*****Beggining of the process*****')

logging.info('Executing EDA...')
try:
    exec(open('./EDA.py').read())
except Exception as e:
  logging.exception("Exception occurred while trying to execute EDA.py")

logging.info('Executing preprocessing...')
try:
    exec(open('./preprocessing.py').read())
except Exception as e:
  logging.exception("Exception occurred while trying to execute preprocessing.py")

logging.info('Executing modeling...')
try:
    exec(open('./model.py').read())
except Exception as e:
  logging.exception("Exception occurred while trying to execute model.py")

logging.info('*****End of the process*****')