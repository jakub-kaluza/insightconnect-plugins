import insightconnect_plugin_runtime
from .schema import CreateCommentInput, CreateCommentOutput, Input, Output, Component
# Custom imports below
from logging import getLogger
from icon_azure_sentiel.util.helpers import AzureSentinelClient

logger = getLogger(__name__)


class CreateComment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_comment',
                description=Component.DESCRIPTION,
                input=CreateCommentInput(),
                output=CreateCommentOutput())

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get(Input.APIVERSION)
        subscription_id = params.get(Input.SUBSCRIPTIONID)
        incident_comment_id = params.get(Input.INCIDENTCOMMENTID)
        incident_id = params.get(Input.INCIDENTID)
        resource_group_name = params.get(Input.RESOURCEGROUPNAME)
        workspace_name = params.get(Input.WORKSPACENAME)
        message = params.get(Input.PROPERTIESMESSAGE)
        client = AzureSentinelClient(token, api_version, subscription_id)

        data_dict = client.create_comment(incident_id, incident_comment_id, resource_group_name, workspace_name, message)

        result = {
            Output.CREATEDTIMEUTC: str(data_dict.get("properties").get("createdTimeUtc")),
            Output.ETAG: data_dict.get("etag"),
            Output.ID: data_dict.get("id"),
            Output.LASTMODIFIEDTIMEUTC: str(data_dict.get("properties").get("lastModifiedTimeUtc")),
            Output.MESSAGE: data_dict.get("properties").get("message"),
            Output.NAME: data_dict.get("name"),
            Output.TYPE: data_dict.get("type"),
        }

        author = data_dict.get("properties").get("author")
        if author:
            author = replace_none(author)
            result["author"] = author
        return result

def replace_none(test_dict: dict) -> dict: 
    new_dict = {}
    for key in test_dict: 
        if test_dict[key] is None: 
            new_dict[key] = "" 
        else:
            new_dict[key] = test_dict[key]
    return new_dict
