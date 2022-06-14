# importing speech recognition package from google api
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS  # google text to speech
import os  # to save/open files
from translate import Translator
## A tuple containing all the language and
dic = ['afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu']
# Capture Voice
# takes command through microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("listening.....")
        print('say:translate (the word or sentence) to (language)')
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("The User said" +query)
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query

def test():

            result = takecommand()
            result=result.lower()
            lstA =[]
            for i in result.split():
                lstA.append(i) #creating list that contains the command
            print(result)
            x = any(item in lstA for item in dic)

            for i in lstA:
                    if i=='translate':
                        lstA.remove(i)

                    elif i=='to':
                        lstA.remove(i)


                    text = ''
            global to_lang
            to_lang=lstA[-1] #getting the desination language
            to_lang = dic[dic.index(to_lang) + 1]
            translator = Translator(to_lang=to_lang)
            lstA.pop()
            for x in lstA:
                      text+=' '+x

            # Translating from src to dest
            text_to_translate= translator.translate(text)
            return text_to_translate

## calling test function
test=test()

speak = gTTS(text=test, lang=to_lang, slow=False)

                        # Using save() method to save the translated
                        # speech in capture_voice.mp3
speak.save("captured_voice.mp3")
playsound("F:\python\captured_voice.mp3")
print(test)
