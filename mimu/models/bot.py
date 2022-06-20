import logging
import typing as t

from aiohttp import ClientSession

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import hikari
from hikari import events

import lightbulb

from mimu.utils import Config

import msgpack

import sake


class Mimu(lightbulb.BotApp):
    def __init__(self) -> None:
        self.log = logging.getLogger("mimu")
        self.scheduler = AsyncIOScheduler()
        self.session = ClientSession()

        super().__init__(
            token=Config.TOKEN,
            help_slash_command=True,
            intents=hikari.Intents.ALL,
        )

        self.redis_cache = sake.RedisCache(
            app=self,
            address=Config.REDIS_ADDRESS,
            event_manager=self.event_manager,
            event_managed=True,
            dumps=msgpack.dumps,
            loads=msgpack.loads,
        )

        self.start_listeners
        self._list_guilds: t.List[hikari.Snowflake] = []

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

    async def on_lightbulb_started(self, _: lightbulb.LightbulbStartedEvent):
        self.log.info(f"Connected to {len(self._list_guilds)} guilds")

    async def on_starting(self, _: events.StartingEvent):
        self.scheduler.start()
        self.session
        await self.redis_cache.open()

    async def on_started(self, _: events.StartedEvent):
        ...

    async def on_stopping(self, _: events.StoppingEvent):
        self.scheduler.shutdown()
        await self.session.close()

    async def on_guild_available(self, event: events.GuildAvailableEvent):
        self._list_guilds.append(event.guild_id)

    async def on_guild_join(self, event: events.GuildJoinEvent):
        self._list_guilds.append(event.guild_id)
        self.log.info(f"Bot joined a new guild: {event.guild.name} (id: {event.guild_id})")

    async def on_guild_leave(self, event: events.GuildLeaveEvent):
        self._list_guilds.remove(event.guild_id)
        self.log.info(f"Bot left a guild: {event.old_guild.name} (id: {event.guild_id})")
