from IPython.display import display
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import data_cleaning as dc


def read_data(filename, sheetname, drop):
    # Prepare to parse Excel sheets into DataFrame
    xls = pd.ExcelFile('./data/' + filename)
    # Read data into DataFrame from appropriate sheet
    df = pd.read_excel(xls, sheetname)

    if drop is True:
        # Drop column 0 because it reads in the labels
        df.drop(df.columns[0], axis=1, inplace=True)

    display(df)

    return df


def create_heatmap(df, filename):
    # Alter figsize to be larger
    fig, ax = plt.subplots(figsize=(10, 10))
    # Draw a heatmap with the numeric values in each cell
    sns.heatmap(df, fmt="d", linewidths=.5, ax=ax)
    # Save heatmap
    plt.savefig("./images/" + filename, dpi=600)

    plt.show()


if __name__ == '__main__':
    # Reading in files
    total_sleep_df = read_data('SP24_rawSleepUpdated.xlsx', 'TotalSleepRecords', True)
    consent_info_df = read_data('SP24_consentInfo.xlsx', 'Sheet1', False)

    # Cleaning Data
    total_sleep_df = dc.withdrew_consent(total_sleep_df, consent_info_df)

