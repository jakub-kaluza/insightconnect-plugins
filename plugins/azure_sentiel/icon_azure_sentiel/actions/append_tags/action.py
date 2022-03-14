import insightconnect_plugin_runtime
from .schema import AppendTagsInput, AppendTagsOutput, Input, Output, Component
from icon_azure_sentiel.util.helpers import AzureSentinelClient
# Custom imports below


class AppendTags(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='append_tags',
                description=Component.DESCRIPTION,
                input=AppendTagsInput(),
                output=AppendTagsOutput())

    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.pop("api-version")
        subscription_id = params.pop("subscriptionId")
        resource_group_name = params.pop("resourceGroupName")
        workspace_name = params.pop("workspaceName")
        name = params.pop("name")

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.append_tags(resource_group_name, workspace_name, name, **params)
        return data_dict
