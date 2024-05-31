from IPython.display import display
import pandas as pd

def read_data(filename):
    # Prepare to parse Excel sheets into DataFrame
    xls = pd.ExcelFile('./data/' + filename)

    # Reading total sleep record sheet into DataFrame
    totalsleep_df = pd.read_excel(xls, 'TotalSleepRecords')

if __name__ == '__main__':
    read_data('SP24_rawSleepUpdated.xlsx')

