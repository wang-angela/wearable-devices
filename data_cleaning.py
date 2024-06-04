from IPython.display import display
import pandas as pd


# Removes participants who withdrew consent
def withdrew_consent(target_df, consent_df):
    # Filter participants to only include those who did withdraw consent
    consent_df = consent_df[consent_df['Consent'] == False]

    # Loop through target DataFrame and remove participants who withdrew consent
    for val in consent_df['ID']:
        # Some IDs are not included in the data
        # This catches 'not found' errors and properly handles them
        try:
            target_df.drop(val, axis=1, inplace=True)
        except KeyError:
            print('Participant ' + str(val) + ' has not logged data')

    return target_df


# Drops participants based on how many days of data have been collected
def threshold_drop(target_df, threshold):
    # Fill in NaN with zeros first then retrieve number of nonzero values in each column
    sum_series = target_df.fillna(0).astype(bool).sum(axis=0)
    # Keep participants who don't meet the threshold
    filtered_series = sum_series[sum_series < threshold]

    # Loop through and remove each participant that doesn't meet the threshold
    for i, val in filtered_series.items():
        # Find participant and drop
        target_df.drop(i, axis=1, inplace=True)

    return target_df

