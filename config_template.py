from msgraph import GraphServiceClient
from azure.identity import DeviceCodeCredential

scopes = ["User.Read", "Calendars.ReadWrite"]

# Multi-tenant apps can use "common",
# single-tenant apps must use the tenant ID from the Azure portal
tenant_id = ""

# Values from app registration
client_id = ""

# azure.identity
credentials = DeviceCodeCredential(tenant_id=tenant_id, client_id=client_id)

graph_client = GraphServiceClient(credentials, scopes)

local_time_zone = ""  # "China Standard Time"
