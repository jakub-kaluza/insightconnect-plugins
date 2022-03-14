import insightconnect_plugin_runtime
from .schema import ListWatchlistsInput, ListWatchlistsOutput, Input, Output, Component
from icon_azure_sentiel.util.helpers import AzureSentinelClient
# Custom imports below


class ListWatchlists(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_watchlists',
                description=Component.DESCRIPTION,
                input=ListWatchlistsInput(),
                output=ListWatchlistsOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.list_watchlists(resource_group_name, workspace_name)
        return data_dict.get("value")
