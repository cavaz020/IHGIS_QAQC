import pandas as pd
from Base_DFs import data_only_df_rows

# THE FOLLOWING CODE FINDS THE ROWS HOLDING SUM VALUES (TOTAL ROWS)


def find_first_col(data_only_dataframe_rows):
    # This function finds what the first column header is within the row version of the data-only dataframe
    list_of_col_headers = list(data_only_dataframe_rows)
    first_col_index = list_of_col_headers[0]
    return first_col_index


def find_indices_of_total_rows(data_only_dataframe_rows, first_col_index):
    # This function takes in the doubly cleaned dataframe and the header of the first column in that dataframe
    # This function returns the index of the rows that hold totals
    # These indices are in a list
    cleaned_df_filled = data_only_dataframe_rows.fillna('none')
    # This is a dataframe
    total_rows = cleaned_df_filled.loc[cleaned_df_filled[first_col_index] == 'none']
    total_rows_dict = total_rows.to_dict('split')
    total_rows_index_list = total_rows_dict['index']
    return total_rows_index_list


def find_rows_to_sum(data_only_dataframe_rows, first_col_index):
    # This function takes in the doubly cleaned dataframe and the header of the first column in that dataframe
    # This function returns the index of the rows that should be aggregated to get the value in the total row
    # These indices are in a list
    cleaned_df_filled = data_only_dataframe_rows.fillna('none')
    # This is a dataframe
    rows_to_sum = cleaned_df_filled.loc[cleaned_df_filled[first_col_index] != 'none']
    rows_to_sum_dict = rows_to_sum.to_dict('split')
    rows_to_sum_index = rows_to_sum_dict['index']
    return rows_to_sum_index


def make_row_dict(rows_to_sum_index, total_rows_index):
    # This function takes in the two lists - the list of the indices of rows to be aggregated
    # and the list of the indices of rows holding the totals
    # This function creates a dictionary of dictionaries
    row_dict = {}
    row_dict['rows to sum'] = rows_to_sum_index
    row_dict['total rows'] = total_rows_index
    return row_dict

# TEST WHETHER TO USE THE SIMPLE FUNCTIONS OR MORE COMPLICATED FUNCTIONS


def number_of_total_rows(total_rows_index):
    # This function takes in the list of the indices of total-rows and counts them
    # This is just used to determine the complexity of the CSV
    total_rows_count = len(total_rows_index)
    return total_rows_count


def fork_in_the_code(number_of_total_rows):
    # This function takes in the number of total rows in the CSV and prints out a message
    # It will eaither say the CSV is complicated (more than 1 total row)
    # Or it will say the CSV is simple (only 1 total row)
    message_list = []
    if number_of_total_rows > 1:
        message_list.append(
            '!!Complicated CSV!! There are multiple total rows')
    else:
        message_list.append(
            'Simple CSV ~ Proceed with functions for one total row')
    return message_list


# ---------------------------------------
# Finding the index of the column that starts the data-only dataframe for rows
first_col_index = find_first_col(data_only_df_rows)

# Finding the total rows within the data-only dataframe for rows
total_rows = find_indices_of_total_rows(data_only_df_rows, first_col_index)
# print('List of Total Row Indices:', total_rows)

# Counting the number of total rows in the dataframe for indicating the complexity of the CSV
tot_row_count = number_of_total_rows(total_rows)
# print('Number of Total rows:', tot_row_count)

# Finding the rows that will be aggregated within the data-only dataframe for rows
rows_to_sum = find_rows_to_sum(data_only_df_rows, first_col_index)
# print('List of rows to be aggregated:', rows_to_sum)

# Making the dictionary to hold the rows that will be aggregated and the rows that hold the totals
row_dict = make_row_dict(rows_to_sum, total_rows)
# print('Row Dictionary:\n', row_dict)

# FORK IN THE CODE - tells whether the CSV is simple or more complicated (aka multiple total rows)
what_to_do_next = fork_in_the_code(tot_row_count)
# print(what_to_do_next)
