from aws_cdk import ( 
    Stack,
    aws_s3 as s3,
    aws_sns as sns,
    aws_sqs as sqs,
    RemovalPolicy
)
import aws_cdk as cdk

from constructs import Construct

class MySnsTopicWithSqsdlqStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    sqsQueue00SnsSubscriptionSendFailure0087EhT = sqs.CfnQueue(self, 'SQSQueue00SNSSubscriptionSendFailure0087EhT',
          sqs_managed_sse_enabled = True,
          receive_message_wait_time_seconds = 0,
          delay_seconds = 0,
          message_retention_period = 345600,
          maximum_message_size = 262144,
          visibility_timeout = 30,
          queue_name = 'SNSSubscriptionSendFailure',
          tags = [
            {
              'value': 'receive SNS messages that are not able to be send',
              'key': 'purpose',
            },
          ],
        )
    sqsQueue00SnsSubscriptionSendFailure0087EhT.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    snsTopic00kfsolutionsemail003vA2k = sns.CfnTopic(self, 'SNSTopic00kfsolutionsemail003vA2K',
          display_name = 'SNS-kfsolutions-email',
          fifo_topic = False,
          subscription = [
            {
              'endpoint': '1robroos@gmail.com',
              'protocol': 'email',
            },
            {
              'endpoint': sqsQueue00SnsSubscriptionSendFailure0087EhT.attr_arn,
              'protocol': 'sqs',
            },
          ],
          archive_policy = {
          },
          topic_name = 'kfsolutions-email',
        )
    snsTopic00kfsolutionsemail003vA2k.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN


    s3.Bucket(
      self, 
      id="bucket123", 
      bucket_name="robroos-testbucket", # Provide a bucket name here
      removal_policy=RemovalPolicy.DESTROY 
    )

