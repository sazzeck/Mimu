import typing as t

import hikari

import lightbulb

import miru


class AuthorView(miru.View):
    def __init__(
        self,
        lctx: lightbulb.Context,
        *,
        timeout: t.Optional[float] = 120,
        autodefer: bool = True,
    ) -> None:

        super().__init__(timeout=timeout, autodefer=autodefer)

        self.lctx = lctx

    async def view_check(self, ctx: miru.Context) -> bool:
        if ctx.user.id != self.lctx.author.id:
            await ctx.respond(
                hikari.Embed(
                    description="You cannot interact with the menu of this component",
                    colour=None,
                )
                .set_author("Mimu: Error!", self.lctx.author.avatar_url),
                flags=hikari.MessageFlag.EPHEMERAL,
            )

        return ctx.user.id == self.light_ctx.author.id

    async def on_timeout(self, ctx: miru.Context) -> None:
        await ctx.message.edit(
            hikari.Embed(
                description="The menu timed out",
                colour=None,
            )
            .set_author("Mimu: Timeout!", self.lctx.author.avatar_url),
            flags=hikari.MessageFlag.EPHEMERAL,
        )


class BasicButton(AuthorView):
    @miru.button(emoji="✖️", style=hikari.ButtonStyle.PRIMARY, row=1)
    async def btn_stop(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.message.delete()
        self.stop()
