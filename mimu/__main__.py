import os

from mimu.models.bot import Mimu
from mimu.utils import Config

import sake


def main():
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot = Mimu()

    bot.redis_chache = sake.RedisCache(
        app=bot,
        address=Config.REDIS_ADDRESS,
        event_manager=bot.event_manager,
        event_managed=True,
    )

    bot.run()


if __name__ == "__main__":
    main()
