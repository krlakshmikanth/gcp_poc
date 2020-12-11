from google.cloud import bigquery
client = bigquery.Client("bigquery-poc-297703")
table_id = "bigquery-poc-297703.bigQuery.historical_table$20201206"
table = client.get_table(table_id)
row_to_insert = [(2, u'{"name": "Arunagiri,", "age": 55}',1575072000)]
errors = client.insert_rows(table,row_to_insert)
if errors==[]:
    print("Row added successfully")
