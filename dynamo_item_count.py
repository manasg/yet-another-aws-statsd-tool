from util_lib.conf_reader import ConfReader
from statsd import StatsdClient
import boto

config = ConfReader(aws_conf='conf/aws.conf', endpoint_conf='conf/endpoint.conf').config

access_key=config['Credentials']['aws_access_key_id']
secret_key=config['Credentials']['aws_secret_access_key']

conn = boto.connect_dynamodb(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key)

tableName = 'prod-ActiveUsers'
table = conn.get_table(tableName)

client = StatsdClient(config['statsd']['hostname'], config['statsd']['port'])
client.gauge("dynamodb.%s.item_count" % tableName, table.item_count)
