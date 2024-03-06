import asyncio
from msgraph.generated.users.item.events.events_request_builder import (
    EventsRequestBuilder,
)
from msgraph.generated.models.event import Event
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.date_time_time_zone import DateTimeTimeZone
from msgraph.generated.models.location import Location

from config import graph_client, local_time_zone
from cf_api import get_cf_contests
from cf_api import contest


async def new_event(c: contest):
    request_body = Event(
        subject=c.name,
        body=ItemBody(
            content_type="html",
            content=c.url,
        ),
        start=DateTimeTimeZone(
            date_time=c.get_start_time(),
            time_zone=local_time_zone,
        ),
        end=DateTimeTimeZone(
            date_time=c.get_end_time(),
            time_zone=local_time_zone,
        ),
        location=Location(
            display_name=c.url,
        ),
        allow_new_time_proposals=True,
    )

    request_configuration = (
        EventsRequestBuilder.EventsRequestBuilderPostRequestConfiguration()
    )
    request_configuration.headers.add("Prefer", f'outlook.timezone="{local_time_zone}"')

    return await graph_client.me.events.post(
        request_body, request_configuration=request_configuration
    )


tasks = []
for i in get_cf_contests():
    tasks.append(asyncio.ensure_future(new_event(i)))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

