import hikari

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
