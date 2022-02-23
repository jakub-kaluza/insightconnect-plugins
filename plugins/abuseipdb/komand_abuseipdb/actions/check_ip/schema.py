# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Look up an IP address in the database"


class Input:
    ADDRESS = "address"
    DAYS = "days"
    VERBOSE = "verbose"
    

class Output:
    ABUSECONFIDENCESCORE = "abuseConfidenceScore"
    COUNTRYCODE = "countryCode"
    COUNTRYNAME = "countryName"
    DOMAIN = "domain"
    FOUND = "found"
    IPADDRESS = "ipAddress"
    IPVERSION = "ipVersion"
    ISPUBLIC = "isPublic"
    ISWHITELISTED = "isWhitelisted"
    ISP = "isp"
    LASTREPORTEDAT = "lastReportedAt"
    NUMDISTINCTUSERS = "numDistinctUsers"
    REPORTS = "reports"
    TOTALREPORTS = "totalReports"
    USAGETYPE = "usageType"
    

class CheckIpInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IPv4 or IPv6 address e.g. 198.51.100.100, ::1, must be subscribed to accept bitmask wider than 255.255.255.0 (/24)",
      "order": 1
    },
    "days": {
      "type": "string",
      "title": "Days",
      "description": "Check for IP reports in the last x days",
      "default": "30",
      "order": 2
    },
    "verbose": {
      "type": "boolean",
      "title": "Verbose",
      "description": "When set, reports will include the comment (if any) and the reporter's user ID number (0 if reported anonymously)",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "address",
    "days",
    "verbose"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckIpOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "abuseConfidenceScore": {
      "type": "integer",
      "title": "Abuse Confidence Score",
      "description": "Confidence of Abuse",
      "order": 5
    },
    "countryCode": {
      "type": "string",
      "title": "Country Code",
      "description": "Code of country IP is registered in",
      "order": 6
    },
    "countryName": {
      "type": "string",
      "title": "Country Name",
      "description": "Name of Country IP is registered in",
      "order": 10
    },
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain Name of IP",
      "order": 9
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Whether an IP address has been found, indicating it may be malicious",
      "order": 15
    },
    "ipAddress": {
      "type": "string",
      "title": "IP Address",
      "description": "Queried IP Address",
      "order": 1
    },
    "ipVersion": {
      "type": "integer",
      "title": "IP Version",
      "description": "Version of IP Address",
      "order": 3
    },
    "isPublic": {
      "type": "boolean",
      "title": "Is Public",
      "description": "Whether or not the IP Address is public",
      "order": 2
    },
    "isWhitelisted": {
      "type": "boolean",
      "title": "Is Whitelisted",
      "description": "Whether or not IP Address is whitelisted",
      "order": 4
    },
    "isp": {
      "type": "string",
      "title": "ISP",
      "description": "Internet Service Provider for IP",
      "order": 8
    },
    "lastReportedAt": {
      "type": "string",
      "title": "Last Reported At",
      "description": "Date of last report",
      "order": 13
    },
    "numDistinctUsers": {
      "type": "integer",
      "title": "Number of Distinct Users",
      "description": "Number of distinct users who reported IP",
      "order": 12
    },
    "reports": {
      "type": "array",
      "title": "Reports",
      "description": "List of reports",
      "items": {
        "$ref": "#/definitions/report"
      },
      "order": 14
    },
    "totalReports": {
      "type": "integer",
      "title": "Total Reports",
      "description": "Total number of reports of abuse",
      "order": 11
    },
    "usageType": {
      "type": "string",
      "title": "Usage Type",
      "description": "How IP is used",
      "order": 7
    }
  },
  "definitions": {
    "report": {
      "type": "object",
      "title": "report",
      "properties": {
        "categories": {
          "type": "array",
          "title": "Categories",
          "description": "List of categories",
          "items": {
            "type": "integer"
          },
          "order": 3
        },
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "Comment by reporter",
          "order": 2
        },
        "reportedAt": {
          "type": "string",
          "title": "Reported At",
          "description": "Date and time of report",
          "order": 1
        },
        "reporterCountryCode": {
          "type": "string",
          "title": "Reporter Country Code",
          "description": "Country code of the reporter",
          "order": 5
        },
        "reporterCountryName": {
          "type": "string",
          "title": "Reporter Country Name",
          "description": "Name of country reporter is from",
          "order": 6
        },
        "reporterId": {
          "type": "integer",
          "title": "Reporter ID",
          "description": "ID number of reporter",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
