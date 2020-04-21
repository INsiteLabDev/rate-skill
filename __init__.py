from mycroft import MycroftSkill, intent_file_handler
import mycroft.skills.mycroft_skill.audio_config as audio


class Rate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.rate_map = {"1": "'0.5'", "2": "'0.75'", "3": "'1.0'", "4": "'1.35'", "5": "'1.7'"}

    @intent_file_handler('fastRate.intent')
    def handle_fastRate(self, message):
        audio.update_rate("'1.7'")
        self.speak_dialog('fastRate')
    
    @intent_file_handler('levelRate.intent')
    def handle_levelRate(self, message):
        rateLevel = message.data.get('rateLevel')
        #audio.update_rate("'1.7'")
        audio.update_rate(self.rate_map[rateLevel])
        self.speak_dialog('levelRate', {'rateLevel' : rateLevel})

    @intent_file_handler('normalRate.intent')
    def handle_normalRate(self, message):
        audio.update_rate("'1.0'")
        self.speak_dialog('normalRate')
    
    @intent_file_handler('slowRate.intent')
    def handle_slowRate(self, message):
        audio.update_rate("'0.7'")
        self.speak_dialog('slowRate')


def create_skill():
    return Rate()

