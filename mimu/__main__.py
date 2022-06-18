import os

from mimu.core.bot import Mimu


def main():
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot = Mimu()
    bot.run(asyncio_debug=True)


if __name__ == "__main__":
    main()
