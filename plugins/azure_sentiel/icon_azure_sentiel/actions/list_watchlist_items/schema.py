# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List watchlist items."


class Input:
    APIVERSION = "api-version"
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WATCHLISTALIAS = "watchlistAlias"
    WORKSPACENAME = "workspaceName"
    

class Output:
    pass

class ListWatchlistItemsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api-version": {
      "type": "string",
      "title": "API version",
      "description": "The API version to use for this operation.",
      "order": 4
    },
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription. The name is case insensitive.",
      "order": 1
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$",
      "order": 2
    },
    "watchlistAlias": {
      "type": "string",
      "title": "Watchlist Alias",
      "description": "The watchlist alias",
      "order": 5
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 3
    }
  },
  "required": [
    "api-version",
    "resourceGroupName",
    "subscriptionId",
    "watchlistAlias",
    "workspaceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListWatchlistItemsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
