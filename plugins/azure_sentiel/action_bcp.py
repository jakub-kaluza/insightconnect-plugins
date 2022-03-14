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
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        self.logger.info(params)

        return {Output.INDICATORS:[]}
