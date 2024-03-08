import os

import dump_utils as du
import config as cf
from classifier import run_classifier
import pandas as pd

import mapping_utils as mp

import data_utils as d

def preprocessing_pipeline():

    df_dump = pd.read_csv('datasets/original_dump.csv')
    print(df_dump.shape)
    df_main = pd.read_csv(cf.INPUT_DATA_PATH)
    print(df_main.shape)
    df_tags = pd.read_csv(cf.SRC_TAG_FREQ)
    mean_d, median_d = d.compute_mean_median(df_main,'downloads')
    mean_f, median_f = d.compute_mean_median(df_tags, 'count')

    filtered_df = d.filter_and_drop_infrequent(df_main, df_tags, int(median_f), int(mean_d), 'datasets/d2.csv')
    print(filtered_df.shape)
    d0 = d.group_and_count_by_tags(df_dump, 'stats/d0_stats.csv')
    d1 = d.group_and_count_by_tags(df_main, 'stats/d1_stats.csv')
    d2 = d.group_and_count_by_tags(filtered_df, 'stats/d2_stats.csv')





def collect_models_data():
    connection = du.create_server_connection(cf.HOST, cf.USER, cf.PWD, cf.DB, cf.PORT)
    #get_dataset_description(connection)
    du.get_model_data(connection)
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")


def mapping_pipeline(ptm):
    similar_ptms = mp.search_ptm_name(ptm, 'datasets/d2.csv')
    #print(similar_ptms)
    print('Most frequent tag', mp.get_most_freq_pipeline_tag(similar_ptms)[0])
    macro, sub = mp.get_most_freq_se_task(ptm, cf.SRC_PAPERS, cf.SRC_SE_TASKS, cf.SRC_MACRO)

    print('Similar PTMs', similar_ptms)
    print('Macro SE task',set(macro))
    print('Sub-tasks', sub)
    return similar_ptms, macro, sub

if __name__ == '__main__':

    #run_classifier(dataset='datasets/d2.csv',desc='card_data', cat='tags', model='CNB', results_csv_path='results/cnb_results.csv')
    mapping_pipeline('bert')
    #preprocessing_pipeline()













