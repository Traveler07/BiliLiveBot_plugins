import time
from datetime import datetime

from plugin import BotPlugin


class WelcomeUp(BotPlugin):
    async def on_command_received(self, cmd, data):
        if cmd != 'LIVE':
            return
        time.sleep(5)
        now = datetime.now().hour
        if now >= 19:
            await self.send_message(f'晚上好呀崽崽')
            time.sleep(2)
            await self.send_message(f'又是秃头的的一夜呢')
        else:
            await self.send_message(f'午好呀，崽崽')