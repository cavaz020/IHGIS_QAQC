import pandas as pd
from Base_DFs import raw_df
from Base_DFs import base_renamed_df
from Base_DFs import number_of_cols_to_delete

# ------------------GLOBAL--MD--DICTIONARY-----------------------------------------------
# gets the title from the metadata


def meta_title(df):
    title = df[df.values == "title"]
    title = title['start']
    title = title.to_string(index=False)
    return title


# gets the source from the metadata
def meta_source(df):
    source = df[df.values == 'source']
    source = source['start']
    source = source.to_string(index=False)
    return source


# gets the geog dictionary from the metadata
def meta_geog_dict(df):
    geog_dict = df[df.values == 'geog dict']
    geog_dict = geog_dict['start']
    geog_dict = geog_dict.to_string(index=False)
    return geog_dict


# gets the mako version from the metadata
def meta_mako_ver(df):
    mako_ver = df[df.values == 'mako version']
    mako_ver = mako_ver['start']
    mako_ver = mako_ver.to_string(index=False)
    return mako_ver


# gets the table number from the metadata
def meta_table_num(df):
    table_num = df[df.values == 'table number']
    table_num = table_num['start']
    table_num = table_num.to_string(index=False)
    return table_num


# gets the geographic extent from the metadata
def meta_geo_extent(df):
    geo_extent = df[df.values == 'geographic extent']
    geo_extent = geo_extent['start']
    geo_extent = geo_extent.to_string(index=False)
    return geo_extent


# creates a dictionary of all the global metadata and puts them in a list
def dictionary_global(title, source, geog_dict, mako_ver, table_num, geo_extent):
    global_dict = {}
    global_dict['title'] = title
    global_dict['source'] = source
    global_dict['geog dict'] = geog_dict
    global_dict['mako version'] = mako_ver
    global_dict['table number'] = table_num
    global_dict['geographic extent'] = geo_extent
    return global_dict

# ------------------COLUMN--DEPENDENT--DICTIONARY-------------------------------------


def make_metadata_dict(renamed_df):
    # This function creates a dictionary holding the metadata (and the first row of the data.. should we delete this?)
    df = renamed_df.iloc[1:, :]
    df = df.loc[:(df == 'start').any(1).idxmax()]
    # This makes the dataframe into a dictionary where each row is a dictionary
    md_dict = df.to_dict(orient='records')
    return md_dict


def make_data_year_dict(md_dict):
    # This function creates a dictionary just holding the info for each column in the 'data year' row
    data_year_dict = {}
    for i in md_dict:
        for k, v in list(i.items()):
            if v == 'data year':
                data_year_dict = i
    # This deletes the key: value '0': 'data year'
    del data_year_dict[0]
    return data_year_dict


def make_universe_dict(md_dict):
    # This function creates a dictionary just holding the info for each column in the 'universe' row
    universe_dict = {}
    for i in md_dict:
        for k, v in list(i.items()):
            if v == 'universe':
                universe_dict = i
    del universe_dict[0]  # This deletes the key: value '0': 'universe'
    return universe_dict


def make_agg_method_dict(md_dict):
    # This function creates a dictionary just holding the info for each column in the 'aggregation method' row
    agg_method_dict = {}
    for i in md_dict:
        for k, v in list(i.items()):
            if v == 'aggregation method':
                agg_method_dict = i
    # This deletes the key: value '0': 'aggregation method'
    del agg_method_dict[0]
    return agg_method_dict


def make_column_dependent_dict(data_yr_dict, universe_dict, agg_method_dict):
    # Creating a dictionary of the three column dependent dictionaries
    col_dependent_dict = {}
    col_dependent_dict['data year'] = data_yr_dict
    col_dependent_dict['universe'] = universe_dict
    col_dependent_dict['aggregation method'] = agg_method_dict
    return col_dependent_dict

# ------------------TRANSLATION--DICTIONARY---------------------------------------


def make_translation_dictionary(renamed_col_df, n_cols_to_delete):
    # This function creates a dictionary holding the metadata (and the first row of the data.. should we delete this?)

    df = renamed_col_df.iloc[1:, :]
    df = df.loc[:(df == 'start').any(1).idxmax()]
    df = df.fillna('Total')

    df.drop(df.tail(1).index, inplace=True)

    list_of_h_geog_row = renamed_col_df[renamed_col_df[0]
                                        == 'h:geog'].index.values
    N = int(list_of_h_geog_row)
    df = df.iloc[N:, n_cols_to_delete:]

    translation_dictionary = df.to_dict(orient='records')
    return translation_dictionary

# ---------------------------RUNNING----CODE-------------------------------------------------


# CODE FOR MAKING GLOBAL MD DICTIONARY
title = meta_title(raw_df)
# print("Title:", title)
source = meta_source(raw_df)
# print("Source:", source)
geog_dict = meta_geog_dict(raw_df)
# print("Geog Dict:", geog_dict)
mako_ver = meta_mako_ver(raw_df)
# print("Mako Version:", mako_ver)
table_num = meta_table_num(raw_df)
# print("Table Number:", table_num)
geo_extent = meta_geo_extent(raw_df)
# print("Geography Extent:", geo_extent)
dict_global = dictionary_global(
    title, source, geog_dict, mako_ver, table_num, geo_extent)
print(dict_global)


# CODE FOR MAKING COLUMN DEPENDENT DICTIONARY
# Calling the function to create a basic list of dictionaries of each row of the metadata
md_dict = make_metadata_dict(base_renamed_df)

# Pulling out the data year dictionary from the list of metadata dictionaries
d_y_dict = make_data_year_dict(md_dict)
# print('Data Year Info:', d_y_dict)

# Pulling out the universe dictionary from the list of metadata dictionaries
u_dict = make_universe_dict(md_dict)
# print('Universe Info:', u_dict)

# Pulling out the aggregation method dictionary from the list of metadata dictionaries
# This will be used for aggregation method info later
agg_dict = make_agg_method_dict(md_dict)
# print('Aggregation Info:', agg_dict)

# Making the column dependent dictionary
col_dependent_dict = make_column_dependent_dict(d_y_dict, u_dict, agg_dict)
# print(col_dependent_dict)

# CODE FOR MAKING TRANSLATION DICTIONARY
translation_dict = make_translation_dictionary(
    base_renamed_df, number_of_cols_to_delete)
# print(translation_dict)
