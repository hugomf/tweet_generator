import boto3

# > SQSWrapper is a class that wraps the boto3 SQS client and provides a simple interface for sending
# and receiving messages
class SQSWrapper:
    
    def __init__(self,queueName=None,):
        """
        The function takes in a queue name and returns the queue url
        
        :param queueName: The name of the queue you want to connect to
        """
        self.sqs = boto3.client("sqs")
        self.queue_url = self.sqs.get_queue_url(QueueName=queueName)["QueueUrl"]

    def send_message(self, message):
        """
        It sends a message to the queue
        
        :param message: The message you want to send to the queue
        :return: The response from the send_message method.
        """
        return self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message
        )
    
    def pop_message(self):
        """
        It gets a message from the queue, deletes it from the queue, and returns the message
        :return: The word that is being returned is the word that is being sent to the queue.
        """
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )

        if "Messages" in response:
            message = response["Messages"][0]
            receipt_handle = message["ReceiptHandle"]
            word = message["Body"]
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            return word
        else:
            return None

    def receive_message(self):
        """
        It receives a message from the queue, and returns the message body
        :return: The word that is being returned is the word that is being searched for.
        """
        self.response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )

        if "Messages" in self.response:
            message = self.response["Messages"][0]
            word = message["Body"]
            return word
        else:
            return None

    def remove_message(self):
        """
        It removes the message from the queue
        """
        if "Messages" in self.response:
            message = self.response["Messages"][0]
            receipt_handle = message["ReceiptHandle"]
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )