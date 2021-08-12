import pandas as pd

# -----------RAW--DF----------------------------------------


def csv_to_raw_df(file_path):
    # This function creates a raw dataframe based on the csv of interest
    raw_df = pd.read_csv(file_path)
    return raw_df

# -----------RENAMED--DF------------------------------------


def simple_rename_columns(file_path):
    renamed_df = pd.read_csv(file_path, header=None)
    return renamed_df

# ----------'Data-Only'--DF----------------------------------


def make_list_of_cols(renamed_df):
    # This function takes in the dataframe with headers from 0-N
    # and creates a list of all of the column headers in that csv
    # (basically a list of numbers from 0-N)
    list_of_col_headers = list(renamed_df)
    return list_of_col_headers


def find_n_cols_to_delete(raw_df):
    # This function takes in the RAW Dataframe (not the dataframe with headers from 0-N)
    # and is used to find the columns that should be deleted when creating the
    # dictionary of total rows and rows to be summed
    data_frame = raw_df.fillna('none')
    data_frame.set_index('x', inplace=True)
    data_frame = data_frame.drop(['start', 'none', 'end'])
    data_frame = data_frame.reset_index()
    data_frame = data_frame.loc[:, :'start']
    data_frame = data_frame.drop(['start'], axis=1)
    n_cols_to_delete = len(data_frame.columns)
    return n_cols_to_delete


def clean_data_frame_part_1(df, number_of_cols, col_header_list):
    # This function gets all the columns of metadata to delete
    N = number_of_cols
    del col_header_list[0:N]
    clean_col_df = df[col_header_list]
    return clean_col_df


def find_n_rows_to_delete(raw_df):
    # This function takes in the RAW Dataframe
    # and returns the length of the metadata
    # aka number of rows of metadata
    data_frame = raw_df.fillna('none')
    data_frame.set_index('x', inplace=True)
    data_frame = data_frame.drop(['start', 'none', 'end'])
    data_frame = data_frame.reset_index()
    metadata_dict = data_frame.set_index('x').T.to_dict()
    metadata_length = len(metadata_dict.keys())
    return metadata_length


def clean_data_frame_part_2(df, MD_length):
    # This function takes in the cleaned dataframe (from which the columns of metadata were deleted)
    # and the number of metadata rows
    # and returns a dataframe without any rows of metadata
    N = MD_length
    data_only_df = df.iloc[N+1:, :]
    return data_only_df


def clean_df_all_int(data_df):
    data_df = data_df[:].astype(int)
    return data_df

# ------------ALTERNATE--FUNCTIONS---------------------------------

# This gets the data-only df including the last row of metadata
# This is useful when comprehending columns


def clean_data_frame_part_2_cols(df, metadata_length):
    N = metadata_length
    clean_df_for_cols = df.iloc[N:, :]
    return clean_df_for_cols

# Necessary when paring the dataframe down to 'data-only' except for the last column of metadata
# This is useful when comprehending rows


def clean_data_frame_part_1_rows(renamed_df, number_of_cols, col_header_list):
    # This function takes in the dataframe with headers 0-N,
    # the list of columns to be deleted and the list holding all of the headers
    # This function creates a dataframe without the metadata
    # columns except for the last column of metadata (see line 47)
    # so that column can be used to find the 'none' values
    N = number_of_cols
    del col_header_list[0:N-1]
    clean_df_for_rows = renamed_df[col_header_list]
    return clean_df_for_rows


# ----------------RUNNING--CODE---------------------------------------------------
# Creating the RAW DF from the csv
raw_df = csv_to_raw_df(
    '/Users/cavazosarte/projects/unit-test-practice/final_code/DZ1998_7_Sheet1.csv')
# print('Raw Dataframe:\n', raw_df)

# Creating the RENAMED DF with headers 0-N
base_renamed_df = simple_rename_columns(
    '/Users/cavazosarte/projects/unit-test-practice/final_code/DZ1998_7_Sheet1.csv')
# print('Renamed Dataframe:\n', base_renamed_df)

# Example of using another CSV
# base_renamed_df = simple_rename_columns('AL2001_47_botimi.csv')
# raw_df = csv_to_raw_df('AL2001_47_botimi.csv')

# Code for making 'DATA-ONLY' DF
# Making list of columns
list_of_cols = make_list_of_cols(base_renamed_df)
# print("list of columns:", list_of_cols)

# Finding out how many columns need to be deleted from the dataframe
number_of_cols_to_delete = find_n_cols_to_delete(raw_df)
# print("number of columns to delete:", number_of_cols_to_delete)

# Deleting the columns from the dataframe to make clean dataframe
clean_df_pt_1 = clean_data_frame_part_1(
    base_renamed_df, number_of_cols_to_delete, list_of_cols)
# print("columns including metadata after deleted:\n", clean_df_pt_1)

# Cleaning the DF by deleting excess rows of metadata
number_of_md_rows = find_n_rows_to_delete(raw_df)
# print("number of metadata rows:", number_of_md_rows)

# Deleting the metadata rows from the dataframe to make clean dataframe
data_only_df = clean_data_frame_part_2(clean_df_pt_1, number_of_md_rows)
data_only_df = clean_df_all_int(data_only_df)
# print("'Data-Only' DF:\n", data_only_df)

# Alternate functions used when comprehending columns and rows respectively
# COLUMNS
data_only_df_cols = clean_data_frame_part_2_cols(
    clean_df_pt_1, number_of_md_rows)
# print('Data-only DF - Columns:\n', data_only_df_cols)

# ROWS
list_of_cols = make_list_of_cols(base_renamed_df)
data_only_df_rows_pt1 = clean_data_frame_part_1_rows(
    base_renamed_df, number_of_cols_to_delete, list_of_cols)
# print(number_of_md_rows)
data_only_df_rows = clean_data_frame_part_2(
    data_only_df_rows_pt1, number_of_md_rows)
# print('Rows:\n', data_only_df_rows)
