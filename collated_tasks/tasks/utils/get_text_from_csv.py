import pandas as pd
import numpy as np

def get_df(file_dir):
    """Read NOTEEVENTS.csv and return a dataframe."""
    print("Reading csv file...")
    df = pd.read_csv(file_dir, dtype={'ROW_ID':np.int32, 'SUBJECT_ID': np.int32,'HADM_ID': np.float64,
                                        'CHARTDATE':str,'STORETIME':str,'CHARTTIME':str,
                                        'STORETIME': str,'CATEGORY': str,'DESCRIPTION':str,'CGID':str,'ISERROR':str,
                                            'TEXT':str}, parse_dates=['chartdate'])
    print("Reading csv file complete!")
    return df

def get_notes_single_row_id(df, row_id):
    """Select and return a single note"""
    return str(df.loc[df['row_id']==row_id]['text'].iloc[0])

def get_notes_row_id(df, row_ids):
    """Select and return a list of notes for given row_ids"""
    return df[df['row_id'].isin(row_ids)]['text'].tolist()

def get_notes_subject_id(df, subject_ids):
    """Select and return a list of notes for given subject_ids"""
    return df[df['subject_id'].isin(subject_ids)]['text'].tolist()

#if __name__ == '__main__':
#    df = get_df('../../../EHRKit_org/tutorials/data/mimic_data/NOTEEVENTS.csv')
#    #notes = get_notes_row_id('../../../EHRKit_org/tutorials/data/mimic_data/NOTEEVENTS.csv', [174, 178])   
#    notes = get_notes_subject_id(df, [22532])
#    print(notes)
