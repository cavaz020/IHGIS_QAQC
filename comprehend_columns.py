import pandas as pd
import numpy as np
from Base_DFs import data_only_df_cols
from Base_DFs import number_of_md_rows

# ----COMPREHENDING--COLUMNS-------------------------------------

# gets the total column name in a list of strings


def get_total_col(renamed_df_cols):
    total_list = renamed_df_cols.columns[renamed_df_cols.isnull(
    ).any()].tolist()
    total_list = [str(i) for i in total_list]
    return total_list


# gets the aggregating column names in a list of strings
def get_agg_col(renamed_df_cols):
    agg_list = renamed_df_cols.columns[~renamed_df_cols.isnull(
    ).any()].tolist()
    agg_list = [str(i) for i in agg_list]  # converting to string
    return agg_list


# gets the total column with just the numbers in a df format
def column_totals_data(renamed_df_cols, metadata_length):
    total_col_data = renamed_df_cols.loc[metadata_length +
                                         1:, renamed_df_cols.isna().any()]
    total_col_data = total_col_data.astype(int)
    return total_col_data


# gets the aggregating columns with just the numbers in a df format
def column_agg_data(renamed_df_cols, metadata_length):
    agg_col_data = renamed_df_cols.loc[metadata_length +
                                       1:, ~renamed_df_cols.isna().any()]
    agg_col_data = agg_col_data.astype(int)
    return agg_col_data

# -------------------------------------------------------------------------------------


# Finding list of indexes of total columns
total_col = get_total_col(data_only_df_cols)
# print("list of columns that have the total:", total_col)

# Finding list of indexes of columns to aggregate
agg_col = get_agg_col(data_only_df_cols)
# print("list of columns to aggregate:", agg_col)

# Copying the total column into its own separate dataframe
total_column_data = column_totals_data(data_only_df_cols, number_of_md_rows)
# print("total column:\n", total_column_data)

# Copying the collumns to be aggregated into its own separate dataframe
agg_column_data = column_agg_data(data_only_df_cols, number_of_md_rows)
# print("aggregate column:\n", agg_column_data)
