import aws_cdk as core
import aws_cdk.assertions as assertions

from 3.cdk.3.cdk_stack import 3CdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 3.cdk/3.cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 3CdkStack(app, "3-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
