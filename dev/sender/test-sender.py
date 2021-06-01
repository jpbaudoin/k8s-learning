from kubemq.queue.message_queue import MessageQueue

from kubemq.queue.message import Message

import time
import sys

if __name__ == "__main__":
    while True:
        channel = "queues.single"
        queue = MessageQueue(channel, "python-sdk-cookbook-queues-single-client", "kubemq-cluster-grpc.kubemq.svc.cluster.local:50000")
        message = Message()
        message.metadata = 'metadata'
        message.body = "some-simple-queue-message".encode('UTF-8')
        message.attributes = None
        try:
            sent = queue.send_queue_message(message)
            if sent.error:
                print('message enqueue error, error:' + sent.error)
            # else:
            #     print('Send to Queue  at: %d' % (
            #         sent.sent_at
            #     ))
        except Exception as err:
            print('message enqueue error, error:%s' % (
                err
            ))
        
        sys.stdout.flush()
        time.sleep(3)