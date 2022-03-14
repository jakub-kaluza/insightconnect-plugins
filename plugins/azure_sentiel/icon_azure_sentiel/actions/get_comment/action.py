import insightconnect_plugin_runtime

from icon_azure_sentiel.util.helpers import AzureSentinelClient
from .schema import GetCommentInput, GetCommentOutput, Output, Component

# Custom imports below
from logging import getLogger

logger = getLogger(__name__)


class GetComment(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_comment", description=Component.DESCRIPTION, input=GetCommentInput(), output=GetCommentOutput()
        )

    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.get("api-version")
        subscription_id = params.get("subscriptionId")
        incident_comment_id = params.get("incidentCommentId")
        incident_id = params.get("incidentId")
        resource_group_name = params.get("resourceGroupName")
        workspace_name = params.get("workspaceName")

        client = AzureSentinelClient(token, api_version, subscription_id)
        data_dict = client.get_comment(incident_id, incident_comment_id, resource_group_name, workspace_name)

        result = {
            Output.CREATEDTIMEUTC: str(data_dict.get("properties").get("createdTimeUtc")),
            Output.ETAG: data_dict.get("etag"),
            Output.ID: data_dict.get("id"),
            Output.LASTMODIFIEDTIMEUTC: str(data_dict.get("properties").get("lastModifiedTimeUtc")),
            Output.MESSAGE: data_dict.get("properties").get("message"),
            Output.NAME: data_dict.get("name"),
            Output.TYPE: data_dict.get("type"),
            Output.AUTHOR: data_dict.get("author", {})
        }
        return result
