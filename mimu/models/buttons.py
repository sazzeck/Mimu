from typing import Optional

import hikari

import lightbulb

import miru


class AuthorView(miru.View):
    def __init__(
        self,
        light_ctx: lightbulb.Context,
        *,
        timeout: Optional[float] = 120,
        autodefer: bool = True,
    ) -> None:

        super().__init__(timeout=timeout, autodefer=autodefer)

        self.light_ctx = light_ctx

    async def view_check(self, ctx: miru.Context) -> bool:
        if ctx.user.id != self.light_ctx.author.id:
            await ctx.respond(
                hikari.Embed(
                    description="You cannot interact with the menu of this component",
                    colour=None,
                )
                .set_author("Mimu: Error!", self.light_ctx.author.avatar_url),
                flags=hikari.MessageFlag.EPHEMERAL,
            )

        return ctx.user.id == self.light_ctx.author.id

    async def on_timeout(self, ctx: miru.Context) -> None:
        await ctx.message.edit(
            hikari.Embed(
                description="The menu timed out",
                colour=None,
            )
            .set_author("Mimu: Timeout!", self.light_ctx.author.avatar_url),
            flags=hikari.MessageFlag.EPHEMERAL,
        )


class BasicButton(AuthorView):
    @miru.button(lable="stop", emoji=":heavy_multiplication_x:", style=hikari.ButtonStyle.PRIMARY, row=1)
    async def btn_stop(self, ctx: miru.Context) -> None:
        await ctx.message.delete()
        self.stop()
