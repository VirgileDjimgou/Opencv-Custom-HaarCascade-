from subprocess import PIPE, call
import urllib
   
class Speech(object):
  
    # converts text to speech
    def text_to_speech(self, text):
        try:
            # truncate text as google only allows 100 chars
            text = text[:100]
   
            # encode the text
            query = urllib.quote_plus(text)
   
            # build endpoint
            endpoint = "http://translate.google.com/translate_tts?tl=en&q=" + query
   
            # debug
            print(endpoint)
   
            # get google to translate and mplayer to play
            call(["mplayer", endpoint], shell=False, stdout=PIPE, stderr=PIPE)
        except:
            print ("Error translating text")
