import insightconnect_plugin_runtime
from icon_azure_sentiel.util.helpers import AzureSentinelClient
from .schema import CreateIndicatorInput, CreateIndicatorOutput, Input, Output, Component
# Custom imports below


class CreateIndicator(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_indicator',
                description=Component.DESCRIPTION,
                input=CreateIndicatorInput(),
                output=CreateIndicatorOutput())

    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.pop("api-version")
        subscription_id = params.pop("subscriptionId")
        resource_group_name = params.pop("resourceGroupName")
        workspace_name = params.pop("workspaceName")

        client = AzureSentinelClient(token, api_version, subscription_id)
        result = client.create_indicator(resource_group_name, workspace_name, **params)
        return result
