import insightconnect_plugin_runtime

from icon_azure_sentiel.util.helpers import AzureSentinelClient
from .schema import QueryIndicatorsInput, QueryIndicatorsOutput, Input, Output, Component
# Custom imports below

class QueryIndicators(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_indicators',
                description=Component.DESCRIPTION,
                input=QueryIndicatorsInput(),
                output=QueryIndicatorsOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.pop(Input.APIVERSION)
        subscription_id = params.pop(Input.SUBSCRIPTIONID)
        resource_group_name = params.pop(Input.RESOURCEGROUPNAME)
        workspace_name = params.pop(Input.WORKSPACENAME)

        #TODO: probably should clean null fields from the params dict
        client = AzureSentinelClient(token, api_version, subscription_id)
        result = client.query_indicators(resource_group_name, workspace_name, **params)
        return {Output.INDICATORS: result.get("value")}
