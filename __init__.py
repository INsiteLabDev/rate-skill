from mycroft import MycroftSkill, intent_file_handler
import mycroft.skills.mycroft_skill.audio_config as audio


class Rate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.rate_map = {"1": "'0.5'", "2": "'0.75'", "3": "'1.0'", "4": "'1.35'", "5": "'1.7'","one": "'0.5'", "two": "'0.75'", "three" : "'1.0'", "four": "'1.35'", "five": "'1.7'"}

    @intent_file_handler('fastRate.intent')
    def handle_fastRate(self, message):
        rateLevel = self.rate_map["5"]
        if (self.compare_rate(rateLevel)):
            audio.update_rate(rateLevel)
            self.speak_dialog('fastRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'fastest'})
    
    @intent_file_handler('levelRate.intent')
    def handle_levelRate(self, message):
        rateLevel = message.data.get('ratelevel')
        #self.speak_dialog(f"this is rate {rateLevel} and rate is {self.rate_map[rateLevel]}")
        if rateLevel not in self.rate_map:
            self.speak_dialog("invalidResponse")
        else:
            check = self.compare_rate(self.rate_map[rateLevel])
            if check:
                audio.update_rate(self.rate_map[rateLevel])
                self.speak_dialog('levelRate', {'rateLevel' : rateLevel})
            else:
                self.speak_dialog('atCurrentRate', {'rateLevel' : rateLevel})

    @intent_file_handler('normalRate.intent')
    def handle_normalRate(self, message):
        rateLevel = self.rate_map["3"]
        if(self.compare_rate(rateLevel)):
            audio.update_rate(rateLevel)
            self.speak_dialog('normalRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'normal'})
    
    @intent_file_handler('slowestRate.intent')
    def handle_slowestRate(self, message):
        rateLevel = self.rate_map["1"]
        if(self.compare_rate(rateLevel)):
            audio.update_rate(rateLevel)
            self.speak_dialog('slowestRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'slowest'})
    
    @intent_file_handler('slow.intent')
    def handle_slowRate(self, message):
        rateLevel = self.rate_map["2"]
        if(self.compare_rate(rateLevel)):
            audio.update_rate(rateLevel)
            self.speak_dialog('slow')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'slow'})

    def compare_rate(self, rate) -> bool:
        current_rate = audio.get_rate()
        if current_rate != rate:
            return True
        return False
    

        

def create_skill():
    return Rate()

