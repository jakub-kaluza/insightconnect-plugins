import insightconnect_plugin_runtime
from icon_azure_sentiel.util.helpers import AzureSentinelClient
from .schema import ListBookmarksInput, ListBookmarksOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class ListBookmarks(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_bookmarks',
                description=Component.DESCRIPTION,
                input=ListBookmarksInput(),
                output=ListBookmarksOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        # TODO: if data_dict.get("nextLink"): ## handle that
        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.list_bookmarks(incident_id, resource_group_name, workspace_name)
        return {Output.BOOKMARKS: data_dict.get("value")}
