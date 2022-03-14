from dataclasses import dataclass, field
import datetime 
from typing import Any, List
from enum import Enum

class IncidentLabelType(Enum):
    SYSTEM = "System"
    USER = "User"

class IncidentSeverity(Enum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"
    INFORMATIONAL = "Informational"

class OwnerType(Enum):
    GROUP = "Group"
    UNKNOWN = "Unknown"
    USER = "User"

@dataclass
class Team:
    description: str 
    name: str
    primaryChannelUrl: str
    teamCreationTimeUtc: datetime.datetime	
    teamId: str

@dataclass
class Label:
    label: str
    label_type: IncidentLabelType

@dataclass
class IncidentOwnerInfo:
    assigned_to: str
    email: str
    object_id: str
    owner_type: OwnerType 

@dataclass
class Incident:
    incident_id: str
    resource_group_name: str
    workspace_name: str
    title: str
    severity: IncidentSeverity
    status: str
    etag: str=""
    classification: str=""
    classification_comment: str=""
    classification_reason: str=""
    description: str=""
    first_activity_time_utc: datetime.datetime=None
    labels: List[Label] = field(default_factory=list)
    last_activity_time_utc: datetime.datetime=None
    provider_incident_id: str=""
    provider_name: str=""
    team_information: Team=None
    incident_owner_info: IncidentOwnerInfo=None
