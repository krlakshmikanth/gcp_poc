from google.cloud import bigquery
client = bigquery.Client()
project="bigquery-poc-297703"
dataset_id="bigQuery"
table_id="Order"
def table1_details(client):
    dataset_ref = client.dataset(dataset_id, project=project)
    table_ref = dataset_ref.table(table_id)
    table = client.get_table(table_ref)  # API Request
    print(table.schema)
table1_details(client)

