from plugin import BotPlugin


class WelcomeUser(BotPlugin):
    async def on_command_received(self, cmd, data):
        if cmd != 'INTERACT_WORD':
            return
        name = data['data']['uname']
        await self.send_message(f'欢迎 {name} 回家')