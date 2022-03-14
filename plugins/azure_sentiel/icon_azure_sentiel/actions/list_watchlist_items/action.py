import insightconnect_plugin_runtime
from .schema import ListWatchlistItemsInput, ListWatchlistItemsOutput, Input, Output, Component
# Custom imports below
from icon_azure_sentiel.util.helpers import AzureSentinelClient


class ListWatchlistItems(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_watchlist_items',
                description=Component.DESCRIPTION,
                input=ListWatchlistItemsInput(),
                output=ListWatchlistItemsOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        watchlist_alias = params.get(Input.WATCHLISTALIAS)

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.list_watchlist_items(resource_group_name, workspace_name, watchlist_alias)
        return data_dict
