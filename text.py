from fnmatch import fnmatch
from datetime import datetime
from plugin import BotPlugin, DanmakuMessage


class TimeChecker(BotPlugin):
    async def on_command_received(self, cmd, data):
        if cmd != 'DANMU_MSG':
            return
        danmu = DanmakuMessage.from_command(data['info'])
        if danmu.uid != 2089560435:
            return
        if fnmatch(danmu.msg, '07!'):
            now = datetime.now()
            show = now.strftime('%Y{y}%m{m}%d{d} %H:%M:%S').format(y='年', m='月', d='日')
            await self.send_message(f'{show}')
