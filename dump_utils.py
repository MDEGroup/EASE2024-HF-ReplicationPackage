
import mysql.connector
from mysql.connector import Error
import data_utils as du


def create_server_connection(host_name, user_name, user_password, db_name, port_number):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=port_number
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection



def get_dataset_description(conn):
    dict_datasets = {}
    cur = conn.cursor()
    cur.execute("SELECT id, description FROM dataset,repository where dataset.dataset_id=repository.id;")
    data = cur.fetchall()
    dict_datasets.update({data[0]: data[1]})
    return dict_datasets

def get_model_data(conn):
    list_results = []
    cur = conn.cursor()
    cur.execute("SELECT model_id,card_data,pipeline_tag,likes,downloads FROM model,repository where model.model_id = repository.id;")

    data = cur.fetchall()
    for d in data:
        cleaned_tuple = [str(elem).strip().replace(',','') for elem in d]
        list_results.append(cleaned_tuple)


    #list_results.append(cur.fetchall())
    headers = ['model_name', 'card_data', 'tags', 'likes', 'downloads']

    du.write_tuples_to_csv('datasets/original_dump.csv', list_results, headers)

    return list_results