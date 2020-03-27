# -*- coding: utf-8 -*-

from kafka.consumer import KafkaConsumer

if __name__ == '__main__':
    BOOTSTRAP_SERVERS = 'kafka-sub.gcxx.com:80'
    # BOOTSTRAP_SERVERS = 'otter13:9093'
    TOPIC = 'gxb'
    consumer = KafkaConsumer(TOPIC, bootstrap_servers=BOOTSTRAP_SERVERS, security_protocol='SASL_PLAINTEXT',
                             sasl_mechanism='PLAIN', sasl_plain_username='client2',
                             sasl_plain_password='AZxdr56YHNmko0', api_version=(0, 10), group_id='gxb')

    # Consumption log
    for msg in consumer:
        print(msg)
