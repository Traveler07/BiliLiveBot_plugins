import time

from plugin import BotPlugin, GuardBuyMessage


class ThanksGuard(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'GUARD_BUY':
            return

        guard = GuardBuyMessage.from_command(data['data'])
        if len(f'感谢{guard.username}送出的{guard.gift_name}!') <= 20:
            await self.send_message(f'感谢{guard.username}送出的{guard.gift_name}!')

        else:
            await self.send_message(f'感谢 {guard.username}')
            time.sleep(2)
            await self.send_message(f'送出的 {guard.gift_name}')
        await self.send_message(f'老板大气!')
        time.sleep(2)
        await self.send_message(f'祝老板福如东海，寿比南山')
        time.sleep(2)
        await self.send_message(f'今年18，明年19，后年找个漂亮的女朋友')