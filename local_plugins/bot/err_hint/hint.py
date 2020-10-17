from errbot import BotPlugin, botcmd

from local_plugins.bot.command_hint import CommandHint

class Hint(BotPlugin):
    @botcmd
    def hint(self, msg, args):
        """
        I will help you. usage: !hint or !help
        """
        body = ':one: !run: // run as prefix \n' \
               + CommandHint.run_hint() + \
               ':white_check_mark: Or please contact @Doai Tran to get more supports.'

        self.send_card(title='Hello guys, I am a Testing Bot! To procedure correct what you want. '
                             'Please review syntax in commands below: ',
                       color='blue',
                       image='https://avatars.slack-edge.com/2020-04-29/1099567160276_d702e8e21c070e5e99f6_192.png',
                       link='https://www.linkedin.com/in/doai-tran-nguyen-van-b125b051/',
                       in_reply_to=msg,
                       body=body)
