import boto3

class SQSWrapper:
    
    def __init__(self,queueName=None,):
        self.sqs = boto3.client("sqs")
        self.queue_url = self.sqs.get_queue_url(QueueName=queueName)["QueueUrl"]

    def send(self, message):
        return self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message
        )
    
    # Define a function to receive messages from the SQS queue
    def pop_message(self):
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


 # Define a function to receive messages from the SQS queue
    def receive_message(self):
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
        if "Messages" in self.response:
            message = self.response["Messages"][0]
            receipt_handle = message["ReceiptHandle"]
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )