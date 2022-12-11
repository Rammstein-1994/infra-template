import aws_cdk as core
import aws_cdk.assertions as assertions

from infra_template.infra_template_stack import InfraTemplateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra_template/infra_template_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InfraTemplateStack(app, "infra-template")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
