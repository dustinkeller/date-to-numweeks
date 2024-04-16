import datetime
import pandas as pd
from pandas._libs.tslibs.parsing import DateParseError
import sys
from os.path import join, dirname

try:
    file_path = sys.argv[1]
    start_date = pd.to_datetime(sys.argv[2])

    data = pd.read_excel(file_path)

    data['Week Number'] = data['Timestamp'].apply(lambda date: (date - start_date).components.days // 7 + 1)

    data.to_excel(join(dirname(file_path), 'output.xlsx'))
except IndexError:
    print("Error: Please match the following argument format: /path/to/file START_DATE")
except FileNotFoundError:
    print("Error: Please make sure you enter a valid input file path.")
except DateParseError:
    print("Error: Please enter a date in the following format: MM/DD/YYYY")
