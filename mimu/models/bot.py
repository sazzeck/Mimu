import hikari
from hikari import events

import lightbulb

from mimu.utils import Config


class Mimu(lightbulb.BotApp):
    def __init__(self) -> None:
        ...

        super().__init__(
            token=Config.TOKEN,
            help_slash_command=True,
            intents=hikari.Intents.ALL,
        )

    @property
    def start_listeners(self) -> None:
        subscriptions = {
            events.StartingEvent: self.on_starting,
            events.StartedEvent: self.on_started,
            events.GuildAvailableEvent: self.on_guild_available,
            lightbulb.LightbulbStartedEvent: self.on_lightbulb_started,
            events.StoppingEvent: self.on_stopping,
            events.GuildJoinEvent: self.on_guild_join,
            events.GuildLeaveEvent: self.on_guild_leave,
        }
        for event, callback in subscriptions.items():
            self.event_manager.subscribe(event, callback)

    async def on_starting(self, _: events.StartingEvent):
        ...

    async def on_lightbulb_started(self, _: lightbulb.LightbulbStartedEvent):
        ...

    async def on_started(self, _: events.StartedEvent):
        ...

    async def on_stopping(self, _: events.StoppingEvent):
        ...

    async def on_guild_available(self, _: events.GuildAvailableEvent):
        ...

    async def on_guild_join(self, _: events.GuildJoinEvent):
        ...

    async def on_guild_leave(self, _: events.GuildLeaveEvent):
        ...
