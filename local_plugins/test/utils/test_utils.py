from local_plugins.utils.string_utils import StringUtils


class TestUtils:

    def test_prety_json(self):
        string_text = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

        print (StringUtils.prety_json(string_text))
