import os

import dump_utils as du
import config as cf
from classifier import run_classifier
import pandas as pd
import yaml
import mapping_utils as mp

import data_utils as d

def preprocessing_pipeline():

    df_dump = pd.read_csv('datasets/out_file_missing.csv')
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
    d2 = d.group_and_count_by_tags(filtered_df, 'stats/d2_new_stats.csv')





def collect_models_data():
    connection = du.create_server_connection(cf.HOST, cf.USER, cf.PWD, cf.DB, cf.PORT)
    #get_dataset_description(connection)
    du.get_model_data(connection)
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")


def mapping_pipeline():
    ptm = 'bert'
    similar_ptms = mp.search_ptm_name(ptm, 'datasets/d2.csv')
    print(similar_ptms)
    print(mp.get_most_freq_pipeline_tag(similar_ptms))

    macro, sub = mp.get_most_freq_se_task(ptm, cf.SRC_PAPERS, cf.SRC_SE_TASKS, cf.SRC_MACRO)
    print(set(macro))
    print(len(set(macro)))
    print(sub)
if __name__ == '__main__':
    #run_classifier(dataset='datasets/d2.csv',desc='card_data', cat='tags', model='CNB', results_csv_path='results/d2_cnb_all.csv')


    #mp.search_pdf_content('se_kb','pre-trained')

    mapping_pipeline()


    #print(len(similar_ptms))

    # df = pd.read_csv('yaml_only.csv')
    # print(df.shape)
    #collect_models_data()
    #preprocessing_pipeline()
    #preprocessing_pipeline()
    #yaml_pipeline()
    #df = pd.read_csv('d1.csv')
    #df = pd.read_csv('stats/stats_tags_all.csv')
    #print(df.shape)







