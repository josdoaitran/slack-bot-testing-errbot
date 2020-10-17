from errbot import BotPlugin, botcmd, arg_botcmd

from errbot.backends.slack import SlackBackend

from local_plugins.bot.command_hint import CommandHint

class Loan(BotPlugin):

    @botcmd
    def run(self, msg, args):
        """
        Usage: List out command for support by: !loan
        """
        return 'You meant:  \n' \
               + CommandHint.run_hint() + \
               'You can use this command to input correct syntax: !help \n' \
               'or contact @Doai Tran'

    @botcmd
    def run_automation_test(self, msg, data):
        """
        Usage: Kick off automation test: !run automation test <test_name_in_CI
        """
        if not data:
            return 'Usage: !run automation test <test_type> <test_name>'
        try:
            all_data = str(data)
            cmd_split = all_data.split(" ")
            test_type = cmd_split[0].strip()
            test_name = cmd_split[1].strip()
        except:
            return 'Usage: !run automation test <test_type> <test_name>'

        self.send(msg.to, ':hammer_and_wrench: I will execute testing `' + test_type + '` `' + test_name + '`',
                  in_reply_to=msg)
        # Call to TeamCity / JMeter to kick off automation with parameter: test_type and test_name
        #
        # ###### Return result # ######
        self.send(msg.to, 'Done. We kick off test successfully')