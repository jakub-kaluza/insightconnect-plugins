import insightconnect_plugin_runtime
from .schema import CreateIncidentInput, CreateIncidentOutput, Input, Output, Component

# Custom imports below
from icon_azure_sentiel.util.models import Incident
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_azure_sentiel.util.helpers import AzureSentinelClient
import json
import requests


class CreateIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_incident",
            description=Component.DESCRIPTION,
            input=CreateIncidentInput(),
            output=CreateIncidentOutput(),
        )

    def run(self, params={}):
        token = self.connection.auth_token
        api_version = params.get("api-version")
        subscription_id = params.get("subscriptionId")
        incident_id = params.get("incidentId")
        resource_group_name = params.get("resourceGroupName")
        workspace_name = params.get("workspaceName")

        title = params.get(Input.TITLE)
        severity = params.get(Input.SEVERITY)
        status = params.get(Input.STATUS)

        client = AzureSentinelClient(token, api_version, subscription_id)
        input_incident = Incident(incident_id, resource_group_name, workspace_name, title, severity, status)
        data_dict = client.create_incident(input_incident)
        return data_dict
