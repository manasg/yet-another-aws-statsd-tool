from util_lib.conf_reader import ConfReader
from statsd import StatsdClient
import boto

import logging

logging.basicConfig()

config = ConfReader(aws_conf='conf/aws.conf', endpoint_conf='conf/endpoint.conf').config

print "Config Loaded : ", config

print "Sending test metric to StatsD - mg.test:2"
client = StatsdClient(config['statsd']['hostname'], config['statsd']['port'])
client.gauge('mg.test',2)

print "Testing connectivity via boto to DynamoDB to make sure credentials are fine"
access_key=config['Credentials']['aws_access_key_id']
secret_key=config['Credentials']['aws_secret_access_key']

conn = boto.connect_dynamodb(aws_access_key_id=access_key,
        aws_secret_access_key=secret_key)
conn.list_tables()


