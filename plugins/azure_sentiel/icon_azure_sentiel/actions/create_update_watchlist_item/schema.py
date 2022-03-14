# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create or update a watchlist item."


class Input:
    APIVERSION = "api-version"
    ETAG = "etag"
    PROPERTIES = "properties"
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WATCHLISTALIAS = "watchlistAlias"
    WATCHLISTITEMID = "watchlistItemId"
    WORKSPACENAME = "workspaceName"
    

class Output:
    pass

class CreateUpdateWatchlistItemInput(insightconnect_plugin_runtime.Input):
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
    "etag": {
      "type": "string",
      "title": "Resources Etag",
      "description": "Resources etag",
      "order": 7
    },
    "properties": {
      "$ref": "#/definitions/WatchlistItemProperties",
      "title": "Watchlist Item Properties",
      "description": "The watchlist item Properties.",
      "order": 8
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
    "watchlistItemId": {
      "type": "string",
      "title": "The watchlist item id",
      "description": "The watchlist item id (GUID)",
      "order": 6
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
    "properties",
    "resourceGroupName",
    "subscriptionId",
    "watchlistAlias",
    "watchlistItemId",
    "workspaceName"
  ],
  "definitions": {
    "CreatedByType": {
      "type": "object",
      "title": "CreatedByType",
      "properties": {
        "Application": {
          "type": "string",
          "title": "Application",
          "description": "Application",
          "order": 1
        },
        "Key": {
          "type": "string",
          "title": "Key",
          "description": "Description",
          "order": 2
        },
        "ManagedIdentity": {
          "type": "string",
          "title": "Managed Indetity",
          "description": "Managed Identity",
          "order": 3
        },
        "User": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 4
        }
      }
    },
    "SystemData": {
      "type": "object",
      "title": "SystemData",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "The timestamp of resource creation (UTC).",
          "displayType": "date",
          "description": "The timestamp of resource creation (UTC).",
          "format": "date-time",
          "order": 1
        },
        "createdBy": {
          "type": "string",
          "title": "The identity that created the resource.",
          "description": "The identity that created the resource.",
          "order": 2
        },
        "createdByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "The type of identity that created the resource.",
          "description": "The type of identity that created the resource.",
          "order": 3
        },
        "lastModifiedAt": {
          "type": "string",
          "title": "The timestamp of resource last modification (UTC)",
          "displayType": "date",
          "description": "The timestamp of resource last modification (UTC)",
          "format": "date-time",
          "order": 4
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "The identity that last modified the resource.",
          "description": "The identity that last modified the resource.",
          "order": 5
        },
        "lastModifiedByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "The type of identity that last modified the resource.",
          "description": "The type of identity that last modified the resource.",
          "order": 6
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed Identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        }
      }
    },
    "UserInfo": {
      "type": "object",
      "title": "UserInfo",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the user.",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the user.",
          "order": 2
        },
        "objectId": {
          "type": "string",
          "title": "Object Identification",
          "description": "The object id of the user.",
          "order": 3
        }
      }
    },
    "WatchlistItemProperties": {
      "type": "object",
      "title": "WatchlistItemProperties",
      "properties": {
        "created": {
          "type": "string",
          "title": "The time the watchlist item was created",
          "description": "The time the watchlist item was created",
          "order": 1
        },
        "createdBy": {
          "$ref": "#/definitions/UserInfo",
          "title": "Describes a user that created the watchlist item",
          "description": "Describes a user that created the watchlist item",
          "order": 2
        },
        "entityMapping": {
          "type": "object",
          "title": "key-value pairs for a watchlist item entity mapping",
          "description": "key-value pairs for a watchlist item entity mapping",
          "order": 3
        },
        "etag": {
          "type": "string",
          "title": "Etag of the azure resource",
          "description": "Etag of the azure resource",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Azure resource Id",
          "description": "Azure resource Id",
          "order": 5
        },
        "isDeleted": {
          "type": "boolean",
          "title": "A flag that indicates if the watchlist item is deleted or not",
          "description": "A flag that indicates if the watchlist item is deleted or not",
          "order": 6
        },
        "itemsKeyValue": {
          "type": "object",
          "title": "key-value pairs for a watchlist item",
          "description": "key-value pairs for a watchlist item",
          "order": 7
        },
        "name": {
          "type": "string",
          "title": "Azure resource name",
          "description": "Azure resource name",
          "order": 8
        },
        "systemData": {
          "$ref": "#/definitions/SystemData",
          "title": "Azure Resource Manager metadata containing createdBy and modifiedBy information.",
          "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information.",
          "order": 9
        },
        "tenantId": {
          "type": "string",
          "title": "The tenantId to which the watchlist item belongs to",
          "description": "The tenantId to which the watchlist item belongs to",
          "order": 10
        },
        "type": {
          "type": "string",
          "title": "Azure resource type",
          "description": "Azure resource type",
          "order": 11
        },
        "updated": {
          "type": "string",
          "title": "The last time the watchlist item was updated",
          "description": "The last time the watchlist item was updated",
          "order": 12
        },
        "updatedBy": {
          "$ref": "#/definitions/UserInfo",
          "title": "Describes a user that updated the watchlist item",
          "description": "Describes a user that updated the watchlist item",
          "order": 13
        },
        "watchlistItemId": {
          "type": "string",
          "title": "The id (a Guid) of the watchlist item",
          "description": "The id (a Guid) of the watchlist item",
          "order": 14
        },
        "watchlistItemType": {
          "type": "string",
          "title": "The type of the watchlist item",
          "description": "The type of the watchlist item",
          "order": 15
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed Identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "The timestamp of resource creation (UTC).",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC).",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "The identity that created the resource.",
              "description": "The identity that created the resource.",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "The type of identity that created the resource.",
              "description": "The type of identity that created the resource.",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "The timestamp of resource last modification (UTC)",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "The identity that last modified the resource.",
              "description": "The identity that last modified the resource.",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "The type of identity that last modified the resource.",
              "description": "The type of identity that last modified the resource.",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indetity",
                  "description": "Managed Identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        },
        "UserInfo": {
          "type": "object",
          "title": "UserInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the user.",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the user.",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object Identification",
              "description": "The object id of the user.",
              "order": 3
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUpdateWatchlistItemOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
