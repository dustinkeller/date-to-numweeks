# Date -> Number of Weeks
Python script that will find out what week number a timestamped entry in an Excel sheet is in, given a specified start date.

# Usage
Open the terminal and run the following to install all dependencies:

```
pip install -r /path/to/requirements.txt
```

Then, run the following:
```
python3 /path/to/date_to_numweeks.py /path/to/your_excel.xlsx START_DATE
```
Make sure your start date is in MM/DD/YYYY format.

This script will produce an `output.xlsx` file in the same directory as the input Excel file.

# Dependencies
* [pandas](https://pandas.pydata.org)
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)