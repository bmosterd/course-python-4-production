def even_nr():
    num = 0
    while True:
        yield num
        num += 2

# even_gen = even_nr()

# total_count = 0
# for _ in range(5):
#     total_count += next(even_gen)
# print(total_count)
import os
import constants
from global_utils import blockPrint, enablePrint
from pprint import pprint
path = '/workspace/course-python-4-production/data/tst/2015.csv'
os.chdir('/workspace/course-python-4-production/w1')
from utils import DataReader
from main import get_sales_information
os.chdir('/workspace/course-python-4-production/')


col_names = [constants.OutDataColNames.STOCK_CODE, constants.OutDataColNames.DESCRIPTION,
                 constants.OutDataColNames.UNIT_PRICE, constants.OutDataColNames.QUANTITY,
                 constants.OutDataColNames.TOTAL_PRICE, constants.OutDataColNames.COUNTRY,
                 constants.OutDataColNames.INVOICE_NO, constants.OutDataColNames.DATE]
data_reader = DataReader(fp=path, sep=',', col_names=col_names)

# # CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))
# import os

# print(os.getcwd())
# from w1.main import get_sales_information
# from w1.utils import DataReader
# import constants
# from global_utils import blockPrint, enablePrint
# from pprint import pprint
# CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
# data_folder_path = os.path.join(CURRENT_FOLDER, '..', constants.DATA_FOLDER_NAME, 'tst')