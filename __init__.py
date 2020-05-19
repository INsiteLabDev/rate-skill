from mycroft import MycroftSkill, intent_file_handler
import os

class Rate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.rate_map = {"1": "'0.5'", "2": "'0.75'", "3": "'1.0'", "4": "'1.35'", "5": "'1.7'","one": "'0.5'", "two": "'0.75'", "three" : "'1.0'", "four": "'1.35'", "five": "'1.7'"}
        self.init_path = open(os.path.abspath("mycroft/tts/audio_config.txt"), 'w')
        self.audio_settings = {"rate" : "'1.0'"}
        self.init_path.write(str(self.audio_settings))
        self.init_path.close()
        self.file_path = os.path.abspath("mycroft/tts/audio_config.txt")

##################### INTENT HANDLERS ###########################
    #handles the intent to increase the rate to fast (1.35)
    @intent_file_handler('fastRate.intent')
    def handle_fastRate(self, message):
        rateLevel = self.rate_map["4"]
        if (self.compare_rate(rateLevel)):
            self.update_audio_file(rateLevel)
            self.speak_dialog('fastRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'fast'})
   
    # handles the intent to increase the rate to fastest (1.7)
    @intent_file_handler('fastestRate.intent')
    def handle_fastestRate(self, message):
        rateLevel = self.rate_map["5"]
        if (self.compare_rate(rateLevel)):
            self.update_audio_file(rateLevel)
            self.speak_dialog('fastestRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'fastest'})
    
    # handles the intent to set the rate the requested level
    @intent_file_handler('levelRate.intent')
    def handle_levelRate(self, message):
        rateLevel = message.data.get('ratelevel')
        # checks to see if level is valid
        if rateLevel not in self.rate_map:
            self.speak_dialog("invalidResponse")
        else:
            check = self.compare_rate(self.rate_map[rateLevel])
            if check:
                self.update_audio_file(self.rate_map[rateLevel])
                self.speak_dialog('levelRate', {'rateLevel' : rateLevel})
            else:
                self.speak_dialog('atCurrentRate', {'rateLevel' : rateLevel})

    # handles the intent to set the rate back to normal (1.0)
    @intent_file_handler('normalRate.intent')
    def handle_normalRate(self, message):
        rateLevel = self.rate_map["3"]
        if(self.compare_rate(rateLevel)):
            self.update_audio_file(rateLevel)
            self.speak_dialog('normalRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'normal'})
    
    # handles the intent to decrease the rate to the slowest (1.0)
    @intent_file_handler('slowestRate.intent')
    def handle_slowestRate(self, message):
        rateLevel = self.rate_map["1"]
        if(self.compare_rate(rateLevel)):
            self.update_audio_file(rateLevel)
            self.speak_dialog('slowestRate')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'slowest'})
    
    # handles the intent to decrease the rate to slow (0.)
    @intent_file_handler('slow.intent')
    def handle_slowRate(self, message):
        rateLevel = self.rate_map["2"]
        if(self.compare_rate(rateLevel)):
            self.update_audio_file(rateLevel)
            self.speak_dialog('slow')
        else:
            self.speak_dialog('atCurrentRate', {'rateLevel': 'slow'})
            
    ###################### END OF INTENT HANDLERS ###########################


    #checks to see if the requested rate is different than the current one
    def compare_rate(self, rate) -> bool:
        audio_file = open(self.file_path, 'r')
        current_rate = self.audio_settings["rate"]
        audio_file.close()
        if current_rate != rate:
            return True
        return False
    #Updates the audio settings file to set the rate variable passed
    def update_audio_file(self, rate):
        audio_file = open(self.file_path, "w")
        self.audio_settings["rate"] = rate
        audio_file.write(str(self.audio_settings))
        audio_file.close()
     

def create_skill():
    return Rate()

