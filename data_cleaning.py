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
