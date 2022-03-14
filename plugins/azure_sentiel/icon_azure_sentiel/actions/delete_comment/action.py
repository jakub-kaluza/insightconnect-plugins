import insightconnect_plugin_runtime
from .schema import DeleteCommentInput, DeleteCommentOutput, Input, Output, Component
# Custom imports below
from icon_azure_sentiel.util.helpers import AzureSentinelClient


class DeleteComment(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_comment',
                description=Component.DESCRIPTION,
                input=DeleteCommentInput(),
                output=DeleteCommentOutput())

    def run(self, params={}):
        token = self.connection.auth_token

        api_version = params.get("api-version")
        subscription_id = params.get("subscriptionId")
        incident_comment_id = params.get("incidentCommentId")
        incident_id = params.get("incidentId")
        resource_group_name = params.get("resourceGroupName")
        workspace_name = params.get("workspaceName")

        client = AzureSentinelClient(token, api_version, subscription_id)
        client.delete_comment(incident_id, incident_comment_id, resource_group_name, workspace_name)
        return {Output.STATUS: "Success"}
