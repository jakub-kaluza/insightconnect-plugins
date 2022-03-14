import insightconnect_plugin_runtime
from .schema import ListEntitiesInput, ListEntitiesOutput, Input, Output, Component
# Custom imports below
from icon_azure_sentiel.util.helpers import AzureSentinelClient

class ListEntities(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_entities',
                description=Component.DESCRIPTION,
                input=ListEntitiesInput(),
                output=ListEntitiesOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.list_entities(incident_id, resource_group_name, workspace_name)
        # TODO: if data_dict.get("nextLink"): ## handle that
        return {Output.ENTITIES: data_dict.get("value")}

