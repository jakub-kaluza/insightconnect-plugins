import insightconnect_plugin_runtime
from icon_azure_sentiel.util.helpers import AzureSentinelClient
from .schema import UpdateIndicatorInput, UpdateIndicatorOutput, Input, Output, Component
# Custom imports below


class UpdateIndicator(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_indicator',
                description=Component.DESCRIPTION,
                input=UpdateIndicatorInput(),
                output=UpdateIndicatorOutput())
    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.pop("api-version")
        subscription_id = params.pop("subscriptionId")
        resource_group_name = params.pop("resourceGroupName")
        workspace_name = params.pop("workspaceName")
        name = params.pop("name")

        client = AzureSentinelClient(token, api_version, subscription_id)
        result = client.update_indicator(resource_group_name, workspace_name, name, **params)
        return result
