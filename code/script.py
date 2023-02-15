import logging
#COnfigure logging
logging.basicConfig(
    filename='../logs/T_03.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

"""
import libraries
"""

logging.info('*****Beggining of the process*****')

logging.info('Executing EDA...')
try:
    execfile('./EDA.py')
except Exception as e:
  logging.exception("Exception occurred while trying to execute EDA.py")

logging.info('Executing preprocessing...')
try:
    execfile('./preprocessing.py')
except Exception as e:
  logging.exception("Exception occurred while trying to execute preprocessing.py")

logging.info('Executing modeling...')
try:
    execfile('./model.py')
except Exception as e:
  logging.exception("Exception occurred while trying to execute model.py")

logging.info('*****End of the process*****')