from confluent_kafka import Producer


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(),
                                                    msg.partition()))


producer_conf = {'bootstrap.servers': 'mybroker1,mybroker2'}

producer = Producer(producer_conf)
data = "hello"

# Trigger any available delivery report callbacks from previous produce() calls
producer.poll(0)

# Asynchronously produce a message, the delivery report callback
# will be triggered from poll() above, or flush() below, when the message has
# been successfully delivered or failed permanently.
producer.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
producer.flush()
