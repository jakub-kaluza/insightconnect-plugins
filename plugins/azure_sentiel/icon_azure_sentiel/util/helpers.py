import requests
import json
import logging

from dataclasses import asdict
from insightconnect_plugin_runtime.exceptions import PluginException
from .endpoints import Endpoint
from .models import Incident
from typing import List, Dict, Any


logger = logging.getLogger(__name__)


class AzureSentinelClient:
    def __init__(self, auth_token: str, api_version: str, subscription_id: str):
        self.auth_token = auth_token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % auth_token,
        }
        self.api_version = api_version
        self.subscription_id = subscription_id

    def _call_api(self, method: str, url: str, headers: dict, payload: dict = None):
        try:
            data = json.dumps(payload) if payload else None
            response = requests.request(
                method,
                url,
                headers=headers,
                data=data,
            )
            response.raise_for_status()
            try:
                if method.upper() != "DELETE":
                    return response.json()
                else:
                    return response.status_code
            except json.decoder.JSONDecodeError as e:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.raw())
        except requests.exceptions.HTTPError as error:
            logger.error(response.json().get("error"))
            raise PluginException(cause="HTTP Error", assistance=str(error))
        except requests.exceptions.Timeout as timeout:
            raise PluginException(cause="Timeout error", assistance=str(timeout))
        except Exception as exception:
            raise PluginException(cause="URL Request Failed", assistance=str(exception))

    def get_comment(self, incident_id: str, incident_comment_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.GETCOMMENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            incident_comment_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def create_comment(
        self,
        incident_id: str,
        incident_comment_id: str,
        resource_group_name: str,
        workspace_name: str,
        message: str,
        etag: str = None,
    ):
        uri = Endpoint.CREATEUPDATECOMMENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            incident_comment_id,
            self.api_version,
        )
        # Without type annotation pyright is complaining
        data: Dict[str, Any] = {
            "properties": {"message": message},
        }
        if etag:
            data["etag"] = etag
        return self._call_api("PUT", final_uri, headers=self.headers, payload=data)

    def delete_comment(self, incident_id: str, incident_comment_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.DELETECOMMENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            incident_comment_id,
            self.api_version,
        )
        return self._call_api("DELETE", final_uri, self.headers)

    def list_comments(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTCOMMENTS
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def get_incident(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.GETINCIDENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def create_incident(self, input_incident: Incident):
        uri = Endpoint.CREATEINCIDENT
        final_uri = uri.format(
            self.subscription_id,
            input_incident.resource_group_name,
            input_incident.workspace_name,
            input_incident.incident_id,
            self.api_version,
        )
        # Data transformation could be refactored further...
        props = asdict(input_incident)
        for name in ["resource_group_name", "workspace_name", "incident_id"]:
            props.pop(name)
        data = {"properties": props}

        return self._call_api("PUT", final_uri, self.headers, data)

    def list_incident(self, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTINCIDENTS
        final_uri = uri.format(self.subscription_id, resource_group_name, workspace_name, self.api_version)
        return self._call_api("GET", final_uri, self.headers)

    def delete_incident(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.DELETEINCIDENT
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("DELETE", final_uri, self.headers)

    def list_bookmarks(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTBOOKMARKS
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def list_alerts(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTALERTS
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def list_entities(self, incident_id: str, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTENTITIES
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            incident_id,
            self.api_version,
        )
        return self._call_api("GET", final_uri, self.headers)

    def query_indicators(self, resource_group_name: str, workspace_name: str, **kwargs):
        uri = Endpoint.QUERYINDICATORS
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            self.api_version,
        )
        return self._call_api("POST", final_uri, self.headers, payload=kwargs)

    def create_indicator(self, resource_group_name: str, workspace_name: str, **kwargs):
        uri = Endpoint.CREATEINDICATOR
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            self.api_version,
        )
        return self._call_api("POST", final_uri, self.headers, payload=kwargs)

    def update_indicator(self, resource_group_name: str, workspace_name: str, name: str, **kwargs):
        uri = Endpoint.UPDATEINDICATOR
        final_uri = uri.format(
            self.subscription_id,
            resource_group_name,
            workspace_name,
            name,
            self.api_version
        )
        kwargs["name"] = name
        return self._call_api("PUT", final_uri, self.headers, payload=kwargs)

    def get_indicator(self, resource_group_name: str, workspace_name: str, name: str):
        uri = Endpoint.GETINDICATOR
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           name,
           self.api_version
        )
        return self._call_api("GET", final_uri, self.headers)

    def delete_indicator(self, resource_group_name: str, workspace_name: str, name: str):
        uri = Endpoint.GETINDICATOR
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           name,
           self.api_version
        )
        return self._call_api("DELETE", final_uri, self.headers)

    def append_tags(self, resource_group_name: str, workspace_name: str, name: str, **kwargs):
        uri = Endpoint.APPENDTAGS
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           name,
           self.api_version
        )
        return self._call_api("POST", final_uri, self.headers, payload=kwargs)

    def replace_tags(self, resource_group_name: str, workspace_name: str, name: str, **kwargs):
        uri = Endpoint.REPLACETAGS
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           name,
           self.api_version
        )
        return self._call_api("POST", final_uri, self.headers, payload=kwargs)

    def create_update_watchlist(self, resource_group_name: str, workspace_name: str, watchlist_alias: str, **kwargs):
        uri = Endpoint.CREATEUPDATEWATCHLIST
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           self.api_version
        )
        return self._call_api("PUT", final_uri, self.headers, payload=kwargs)

    def get_watchlist(self, resource_group_name: str, workspace_name: str, watchlist_alias: str):
        uri = Endpoint.GETWATCHLIST
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           self.api_version
        )
        return self._call_api("GET", final_uri, self.headers)

    def delete_watchlist(self, resource_group_name: str, workspace_name: str, watchlist_alias: str):
        uri = Endpoint.DELETEWATCHLIST
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           self.api_version
        )
        return self._call_api("DELETE", final_uri, self.headers)

    def list_watchlists(self, resource_group_name: str, workspace_name: str):
        uri = Endpoint.LISTWATCHLISTS
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           self.api_version
        )
        return self._call_api("GET", final_uri, self.headers)

    def create_update_watchlist_item(self, resource_group_name: str, workspace_name: str, watchlist_alias: str, watchlist_item_id: str, **kwargs):
        uri = Endpoint.CREATEUPDATEWATCHLISTITEM
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           watchlist_item_id,
           self.api_version
        )
        return self._call_api("PUT", final_uri, self.headers, payload=kwargs)

    def get_watchlist_item(self, resource_group_name: str, workspace_name: str, watchlist_alias: str, watchlist_item_id: str):
        uri = Endpoint.GETWATCHLISTITEM
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           watchlist_item_id,
           self.api_version
        )
        return self._call_api("GET", final_uri, self.headers)

    def delete_watchlist_item(self, resource_group_name: str, workspace_name: str, watchlist_alias: str, watchlist_item_id: str):
        uri = Endpoint.DELETEWATCHLISTITEM
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           watchlist_item_id,
           self.api_version
        )
        return self._call_api("DELETE", final_uri, self.headers)

    def list_watchlist_items(self, resource_group_name: str, workspace_name: str, watchlist_alias: str):
        uri = Endpoint.LISTWATCHLISTITEMS
        final_uri = uri.format(
           self.subscription_id,
           resource_group_name,
           workspace_name,
           watchlist_alias,
           self.api_version
        )
        return self._call_api("GET", final_uri, self.headers)
