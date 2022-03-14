# Description

Azure Sentiel is Azures automated security

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_version|string|2016-04-30-preview|True|The version of the API to use. The current version is 2016-04-30-preview|None|None|
|client_id|string|None|True|The application ID that the application registration portal assigned to your app|None|None|
|client_secret|credential_asymmetric_key|None|True|The application secret that you generated for your app in the app registration portal|None|None|
|host|string|https://example.com|True|Azure REST API Server|None|None|
|tenant_id|string|None|True|This is active directory ID|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Replace Tags

This action is used to replace tags to a threat intelligence indicator..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field.|None|None|
|properties|ThreatIntelligenceIndicatorProperties|None|True|Object containing all the necessary properties to conclude a query. Only property that affects the API is threatIntelligenceTags.|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### list watchlist items

This action is used to list watchlist items..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Delete a watchlist item

This action is used to delete a watchlist item..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|watchlistItemId|string|None|True|The watchlist item id (GUID)|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Get a watchlist item

This action is used to get a watchlist item..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|watchlistItemId|string|None|True|The watchlist item id (GUID)|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### List a watchlist

This action is used to list a watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Create or update a watchlist item

This action is used to create or update a watchlist item..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|etag|string|None|False|Resources etag|None|None|
|properties|WatchlistItemProperties|None|True|The watchlist item Properties.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|watchlistItemId|string|None|True|The watchlist item id (GUID)|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### delete a watchlist

This action is used to delete a watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### get a watchlist

This action is used to get a watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Create or update a watchlist

This action is used to create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|properties|WatchlistProperties|None|True|all the properties included in the body of the query.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|watchlistAlias|string|None|True|The watchlist alias|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Append Tags

This action is used to append tags to a threat intelligence indicator..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field.|None|None|
|threatIntelligenceTags|[]string|None|False|List of tags to be appended.|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Get Threat Intelligence Indicator

This action is used to get existing threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field.|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Delete Threat Intelligence Indicator

This action is used to delete existing threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Threat intelligence indicator name field.|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Create Threat Intelligence Indicator

This action is used to create new threat intelligence indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|etag|string|None|False|Etag of the azure resource|None|None|
|properties|ThreatIntelligenceIndicatorProperties|None|True|Object containing all the necessary properties to conclude a query.|None|None|

Example input:

```
```

##### Output

_This action does not contain any outputs._

#### Query Threat Indicators

This action is used to query threat intelligence indicators as per filtering criteria..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|ids|[]string|None|False|Ids of threat intelligence indicators|None|None|
|includeDisabled|boolean|None|False|Parameter to include/exclude disabled indicators.|None|None|
|keywords|[]string|None|False|Keywords for searching threat intelligence indicators|None|None|
|maxConfidence|integer|None|False|Maximum confidence.|None|75|
|maxValidUntil|string|None|False|End time for ValidUntil filter.|None|None|
|minConfidence|integer|None|False|Minimum confidence.|None|0|
|minValidUntil|string|None|False|Start time for ValidUntil filter.|None|None|
|pageSize|integer|None|False|Page Size.|None|None|
|patternTypes|integer|None|False|Pattern Types.|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skip Token.|None|None|
|sortBy|[]ThreatIntelligenceSortingCriteria|None|False|Columns to sort by and sorting order|None|None|
|sources|[]string|None|False|Sources of threat intelligence indicators.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|threatTypes|[]string|None|False|Threat Types of Threat Inteligence Indicators.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
{
  "maxConfidence": 75,
  "minConfidence": 0
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicators|[]object|False|output threat intelligence indicators.|

Example output:

```
```

#### List entities

This action is used to get all incidents entities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]object|False|All the entities assigned to the given incident.|

Example output:

```
```

#### List Bookmarks

This action is used to get all incidents bookmarks.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|bookmarks|[]object|False|All the bookmarks assigned to the given incident.|

Example output:

```
```

#### List Comments

This action is used to get all incidents alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]object|False|All the alerts assigned to the given incident.|

Example output:

```
```

#### Get Incident

This action is used to get all incidents from a given workspace and resource group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident|object|False|The queried incident|

Example output:

```
```

#### Get Comments

This action gets all the comments for a given incident..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|filter|string|None|False|Filters the results, based on a Boolean condition. Optional.|None|None|
|orderBy|string|None|False|sorts the results|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|skipToken|string|None|False|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|top|integer|None|False|Return only n first results.|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Incidents|[]object|False|list of incidents objects|

Example output:

```
```

#### Get Comment

This action gets a comment for a given incident..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|incidentCommentId|string|None|True|Incident Comment ID|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|author|person|False||
|createdTimeUtc|date|False||
|etag|string|False||
|id|string|False||
|lastModifiedTimeUtc|date|False||
|message|string|False||
|name|string|False||
|type|string|False||

Example output:

```
```

#### Delete Comment

This action deletes a comment for a given incident..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|incidentCommentId|string|None|True|Incident Comment ID|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status of the requested operation e.g. success, error, etc|

Example output:

```
```

#### Create Comment

This action creates or updates a comment for a given incident..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api-version|string|None|True|The API version to use for this operation.|None|None|
|etag|string|None|False|etag of the azure resource|None|None|
|incidentId|string|None|True|Incident ID|None|None|
|resourceGroupName|string|None|True|The name of the resource group within the user's subscription. The name is case insensitive.|None|None|
|severity|string|None|True|Incidents severity|['High', 'Informational', 'Low', 'Medium']|None|
|status|string|None|True|Incidents status|['Active', 'Closed', 'New']|None|
|subscriptionId|string|None|True|Azure subscription ID Regex pattern: ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$|None|None|
|title|string|None|True|The Incidents title|None|None|
|workspaceName|string|None|True|The name of the workspace|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alertProductNames|[]string|False||
|alertsCount|integer|False||
|assignedTo|string|False||
|bookmarksCount|integer|False||
|classification|string|False||
|classificationComment|string|False||
|classificationReason|string|False||
|commentsCount|integer|False||
|createdTimeUtc|date|False||
|description|string|False||
|email|string|False||
|etag|string|False||
|firstActivityTimeUt|date|False||
|id|string|False||
|incidentNumber|integer|False||
|incidentUrl|string|False||
|labels|[]string|False||
|lastActivityTimeUtc|date|False||
|lastModifiedTimeUtc|date|False||
|name|string|False||
|ownersObjectId|string|False||
|relatedAnalyticRuleIds|[]string|False||
|severity|string|False||
|status|string|False||
|tactics|[]string|False||
|title|string|False||
|type|string|False||
|userPrincipalName|string|False||

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Azure Sentiel Plugin](LINK TO PRODUCT/VENDOR WEBSITE)

