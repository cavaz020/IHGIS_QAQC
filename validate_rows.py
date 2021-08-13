import pandas as pd
from Base_DFs import data_only_df
from comprehend_rows import rows_to_sum, total_rows


# THIS FILE AND THESE FUNCTIONS ARE USEFUL FOR DATAFRAME WITH ONLY ONE TOTAL ROW (SIMPLE CSV)
def create_df_total_rows(data_only_data_frame, rows_to_sum):
    # This function takes in the "data-only" df and the rows to sum and creates a separate df
    # with only the total rows
    total_rows_df = data_only_data_frame.drop(labels=rows_to_sum)
    total_rows_df = total_rows_df.transpose()
    return total_rows_df


def create_df_rows_to_be_aggregated(data_only_data_frame, total_rows):
    # This function takes in the "data-only" df and the rows to sum and creates a separate df
    # with only the rows to be aggregated summed
    rows_to_be_aggregated_df = data_only_data_frame.drop(labels=total_rows)
    return rows_to_be_aggregated_df


def create_rows_to_agg_dict(create_sum_df):
    # This function creates a dictionary of the sum of the rows to be aggregated
    create_sum_df = create_sum_df.sum(axis=0)
    created_sum_dict = create_sum_df.to_dict()
    return created_sum_dict


def create_created_sum_df(created_sum_dict):
    # This function creates a dataframe with the summed row with the column header '0'
    created_sum_df = pd.DataFrame.from_dict(created_sum_dict, orient='index')
    return created_sum_df


# -------------------FUNCTION--TO--VALIDATE--DATA----------------------------

def validate_rows(total_rows_df, total_row_list, created_sum_df):
    # This function takes in the dataframe of the total row and
    # the dataframe of the summed rows to be aggregated
    # This function returns a list of the columns where the value between the aggregated column
    # and the total column are incorrect
    # If there are no incorrect columns, a message indicating this will be returned
    total_rows_df['aggregated'] = created_sum_df
    for num in total_row_list:
        total_index = num
    total_rows_df = total_rows_df.rename(columns={total_index: 'Total'})
    index = total_rows_df.index
    condition = total_rows_df['aggregated'] != total_rows_df['Total']
    incorrect_indices = index[condition]
    incorrect_indices_list = incorrect_indices.tolist()
    if len(incorrect_indices_list) == 0:
        incorrect_indices_list.append(
            '!!There are no unequal columns. This table adds up correctly in the total row!!')
    return incorrect_indices_list


# -------------------------------------------------------------------------------
# Calling functions to create variables to be used when validating row sums
# Dataframe with only the total row - transposed to make the row into a column
total_rows_df = create_df_total_rows(data_only_df, rows_to_sum)
# print('Only Total Row DF:\n', total_rows_df)

# Dataframe with only the rows that should be aggregated
rows_to_agg_df = create_df_rows_to_be_aggregated(data_only_df, total_rows)
# print('Only Rows to Sum:\n', rows_to_agg_df)

# Dictionary with the sum of the rows that should be aggregated
created_total_dict = create_rows_to_agg_dict(rows_to_agg_df)
# print('Summed Rows Dict:, created_total_dict)

# Dataframe with only one row (transposed to a column) that is
# the sum of the rows to be aggregated
created_total_df = create_created_sum_df(created_total_dict)
# print('Summed Rows DF:\n', created_total_df)

# Calling the function to validate the row values
# Prints out a list of the columns where the totals don't match the aggregated values
unequal_col_list = validate_rows(
    total_rows_df, total_rows, created_total_df)
# print('Unequal Columns:', unequal_col_list)
