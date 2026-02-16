import os
import func_categorize
import func_api
from dotenv import load_dotenv
from pick import pick

load_dotenv()

FILE_PATH = os.getenv('FILE_PATH')
path = FILE_PATH
dir_list = os.listdir(path)

title = 'Pick a receipt:  '
file, index = pick(dir_list, title)

func_categorize.categorize(func_api.receipt.items)