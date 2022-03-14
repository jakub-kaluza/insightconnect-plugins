class Endpoint():
    GETCOMMENT = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/comments/{}?api-version={}"

    CREATEUPDATECOMMENT = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/comments/{}?api-version={}"
    
    DELETECOMMENT = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/comments/{}?api-version={}"
    
    LISTCOMMENTS ="https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/comments?api-version={}"

    GETINCIDENT = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}?api-version={}"

    CREATEINCIDENT = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}?api-version={}"

    LISTINCIDENTS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents?api-version={}"

    DELETEINCIDENT = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}?api-version={}"
    LISTALERTS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/alerts?api-version={}"
    LISTBOOKMARKS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/bookmarks?api-version={}"
    LISTENTITIES = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/incidents/{}/entities?api-version={}"
    QUERYINDICATORS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/queryIndicators?api-version={}"
    CREATEINDICATOR = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/createIndicator?api-version={}"
    UPDATEINDICATOR = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{}?api-version={}"
    GETINDICATOR = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{}?api-version={}"
    DELETEINDICATOR = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{}?api-version={}"
    APPENDTAGS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{}/appendTags?api-version={}"
    REPLACETAGS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/threatIntelligence/main/indicators/{}/replaceTags?api-version={}"
    CREATEUPDATEWATCHLIST = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}?api-version={}"
    GETWATCHLIST = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}?api-version={}"
    DELETEWATCHLIST = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}?api-version={}"
    LISTWATCHLISTS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists?api-version={}"
    CREATEUPDATEWATCHLISTITEM = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}/watchlistItems/{}?api-version={}"
    GETWATCHLISTITEM = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}/watchlistItems/{}?api-version={}"
    DELETEWATCHLISTITEM = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}/watchlistItems/{}?api-version={}"
    LISTWATCHLISTITEMS = "https://management.azure.com/subscriptions/{}/resourceGroups/{}/providers/Microsoft.OperationalInsights/workspaces/{}/providers/Microsoft.SecurityInsights/watchlists/{}/watchlistItems?api-version={}"
