from util_lib.conf_reader import ConfReader
from statsd import StatsdClient
import boto.sqs

config = ConfReader(aws_conf='conf/aws.conf', endpoint_conf='conf/endpoint.conf').config

access_key=config['Credentials']['aws_access_key_id']
secret_key=config['Credentials']['aws_secret_access_key']

region = config['Sqs']['region']
prefix = ""

if 'prefix' in config['Sqs'] : 
    prefix = config['Sqs']['prefix'] 

conn = boto.sqs.connect_to_region(region, 
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key)

queues = conn.get_all_queues(prefix=prefix)

client = StatsdClient(config['statsd']['hostname'], config['statsd']['port'])

for queue in queues:
    client.gauge("sqs.%s.item_count" % queue.name, queue.count())

