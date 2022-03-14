import insightconnect_plugin_runtime
from icon_azure_sentiel.util.helpers import AzureSentinelClient
from .schema import DeleteIndicatorInput, DeleteIndicatorOutput, Input, Output, Component


class DeleteIndicator(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_indicator',
                description=Component.DESCRIPTION,
                input=DeleteIndicatorInput(),
                output=DeleteIndicatorOutput())

    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.get("api-version")
        subscription_id = params.get("subscriptionId")
        resource_group_name = params.get("resourceGroupName")
        workspace_name = params.get("workspaceName")
        name = params.get("name")

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.delete_indicator(resource_group_name, workspace_name, name)
        return data_dict
