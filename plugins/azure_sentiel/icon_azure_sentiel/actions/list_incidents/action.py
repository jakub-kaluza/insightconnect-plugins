import insightconnect_plugin_runtime
from .schema import ListIncidentsInput, ListIncidentsOutput, Input, Output, Component
# Custom imports below
from icon_azure_sentiel.util.helpers import AzureSentinelClient


class ListIncidents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_incidents',
                description=Component.DESCRIPTION,
                input=ListIncidentsInput(),
                output=ListIncidentsOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.list_incident(resource_group_name, workspace_name)
        return {Output.INCIDENTS: data_dict.get("value")}
