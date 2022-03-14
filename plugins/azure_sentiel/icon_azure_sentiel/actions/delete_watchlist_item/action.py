import insightconnect_plugin_runtime
from .schema import DeleteWatchlistItemInput, DeleteWatchlistItemOutput, Input, Output, Component
from icon_azure_sentiel.util.helpers import AzureSentinelClient
# Custom imports below


class DeleteWatchlistItem(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_watchlist_item',
                description=Component.DESCRIPTION,
                input=DeleteWatchlistItemInput(),
                output=DeleteWatchlistItemOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.pop("api-version")
        subscription_id = params.pop("subscriptionId")
        resource_group_name = params.pop("resourceGroupName")
        workspace_name = params.pop("workspaceName")
        watchlist_alias = params.pop(Input.WATCHLISTALIAS)
        watchlist_item_id = params.pop(Input.WATCHLISTITEMID)
        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.delete_watchlist_item(resource_group_name, workspace_name, watchlist_alias, watchlist_item_id)
        return data_dict
