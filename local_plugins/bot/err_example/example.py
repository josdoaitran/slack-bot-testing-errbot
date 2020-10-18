from errbot import BotPlugin, botcmd, arg_botcmd

from errbot.backends.slack import SlackBackend

from local_plugins.bot.command_hint import CommandHint

class Example(BotPlugin):

    @botcmd
    def example_direct_return_name(self, msg, data):
        """
        Usage: !example direct return name <firstName> <lastName>
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

    @botcmd()
    def example_thread_return_name(self, msg, data):
        """
               Usage: !example thread return name <firstName> <lastName>
               """
        if not data:
            return 'Usage: !example thread return name <firstName> <lastName>'
        try:
            all_data = str(data)
            cmd_split = all_data.split(" ")
            firstName = cmd_split[0].strip()
            lastName = cmd_split[1].strip()
        except:
            return 'Usage: !example thread return name <firstName> <lastName>'

        self.send(msg.to, ':hammer_and_wrench: Your FulName is `' + lastName + '` ' + '`' + firstName + '`', in_reply_to=msg)

    # @botcmd()
    # def example_return_card(self, msg, data):

    # @botcmd()
    # def example_return_file(self, msg, data):

    # @botcmd()
    # def example_return_file(self, msg, data):
    #     string_text = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
    #                   '{"ID":20,"Name":"David Lee","Role":"Editor"}]'
    #
    #     print(StringUtils.prety_json(string_text))


