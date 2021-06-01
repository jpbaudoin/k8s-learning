from kubemq.queue.message_queue import MessageQueue

from kubemq.queue.message import Message

import time
import sys

if __name__ == "__main__":
    while True:
        channel = "queues.single"
        queue = MessageQueue(channel, "python-sdk-cookbook-queues-single-client-receiver", "kubemq-cluster-grpc.kubemq.svc.cluster.local:50000", 2, 1)
        try:
            res = queue.receive_queue_messages()
            if res.error:
                print(
                    "'Received:'%s'" % (
                        res.error
                    )
                )
            # else:
            #     for message in res.messages:
            #         print(
            #             "'Received :%s ,Body: sending:'%s'" % (
            #                 message.MessageID,
            #                 message.Body
            #             )
            #         )
        except Exception as err:
            print(
                "'error sending:'%s'" % (
                    err
                )
            )
        
        sys.stdout.flush()
        time.sleep(1)