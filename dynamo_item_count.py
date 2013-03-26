from util_lib.conf_reader import ConfReader
from statsd import StatsdClient
import boto

config = ConfReader(aws_conf='conf/aws.conf', endpoint_conf='conf/endpoint.conf').config

access_key=config['Credentials']['aws_access_key_id']
secret_key=config['Credentials']['aws_secret_access_key']

conn = boto.connect_dynamodb(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key)

#table_names = ['table1','table2']
table_names = conn.list_tables()

for name in table_names:
    table = conn.get_table(name)
    client = StatsdClient(config['statsd']['hostname'], config['statsd']['port'])
    client.gauge("dynamodb.%s.item_count" % name, table.item_count)

