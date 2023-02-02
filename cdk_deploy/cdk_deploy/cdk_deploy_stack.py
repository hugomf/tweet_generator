from constructs import Construct
from aws_cdk import (
    Duration,
    CfnOutput,
    aws_sqs as sqs,
    Stack,
)

from env_config import (
    QUEUE_NAME,
    OPENAI_API_KEY
) 

class CdkDeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create an SQS queue
        queue = sqs.Queue(
            self, "PhraseProducerQueue",
            queue_name="phrase-producer-queue",
            visibility_timeout=Duration.seconds(300)
        )
        
        # Output the URL of the queue
        CfnOutput(
            self, "PhraseProducerQueueUrl",
            value=queue.queue_url
        )

