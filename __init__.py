from mycroft import MycroftSkill, intent_file_handler


class Rate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rate.intent')
    def handle_rate(self, message):
        self.speak_dialog('rate')


def create_skill():
    return Rate()

