import os

from mimu.models.bot import Mimu


def main():
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot = Mimu()

    bot.run()


if __name__ == "__main__":
    main()
