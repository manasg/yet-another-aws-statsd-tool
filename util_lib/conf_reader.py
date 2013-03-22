import ConfigParser

class ConfReader:
    def __init__(self, aws_conf = '../conf/aws.conf', endpoint_conf = '../conf/endpoint.conf'):
        config = ConfigParser.ConfigParser()
        config.readfp(open(aws_conf))
        config.readfp(open(endpoint_conf))

        self.config = dict(config._sections)
        self.config['statsd']['port'] = int(self.config['statsd']['port'])

if __name__ == "__main__":
    conf = ConfReader()
    print conf.config
