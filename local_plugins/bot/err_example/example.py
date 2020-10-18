from errbot import BotPlugin, botcmd, arg_botcmd

from errbot.backends.slack import SlackBackend

from local_plugins.bot.command_hint import CommandHint

class Example(BotPlugin):

    @botcmd
    def example_direct_return_name(self, msg, data):
        """
        Usage:
        """
        if not data:
            return 'Usage: !example direct return <firstName> <lastName>'
        try:
            all_data = str(data)
            cmd_split = all_data.split(" ")
            firstName = cmd_split[0].strip()
            lastName = cmd_split[1].strip()
        except:
            return 'Usage: !run automation test <test_type> <test_name>'

        return ':get_well_soon: Your FulName is `' + lastName + '` ' + '`' + firstName + '`'

