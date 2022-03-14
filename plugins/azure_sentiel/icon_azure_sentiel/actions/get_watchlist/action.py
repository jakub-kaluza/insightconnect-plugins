import insightconnect_plugin_runtime
from .schema import GetWatchlistInput, GetWatchlistOutput, Input, Output, Component
from icon_azure_sentiel.util.helpers import AzureSentinelClient
# Custom imports below


class GetWatchlist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_watchlist',
                description=Component.DESCRIPTION,
                input=GetWatchlistInput(),
                output=GetWatchlistOutput())

    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.pop("api-version")
        subscription_id = params.pop("subscriptionId")
        resource_group_name = params.pop("resourceGroupName")
        workspace_name = params.pop("workspaceName")
        watchlist_alias = params.pop(Input.WATCHLISTALIAS)

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.get_watchlist(resource_group_name, workspace_name, watchlist_alias)
        return data_dict
