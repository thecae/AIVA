import speech_recognition as sr
import time
import pygame
from gtts import gTTS
import datetime
import calendar
import wolframalpha as wa
import warnings
import wikipedia

warnings.filterwarnings('ignore')
app_id='HIDDEN APP ID'
client=wa.Client(app_id)

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listening...')
        audio=r.listen(source)
    data=''
    try:
        data=r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError:
        print('Google Speech Recognition did not understand audio.')
    except sr.RequestError as e:
        print('Request failed; {0}'.format(e))
    return data

def respond(audio_string):
    print(audio_string)
    tts=gTTS(text=audio_string,lang='en')
    tts.save('speech.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('speech.mp3')
    pygame.mixer.music.play()

def wake_word(audio_string):
    WAKE_WORDS=['hey ava', 'okay ava']
    audio_string=audio_string.lower()
    for phrase in WAKE_WORDS:
        if phrase in audio_string:
            return True
    return False

def get_date():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    month_num=now.month
    day_num=now.day
    MONTHS=['January','February','March','April','May','June','July','August',
            'September','October','November','December']
    ORDINAL_NUMS=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                  '11th','12th','13th','14th','15th','16th','17th','18th','19th',
                  '20th','21st','22nd','23rd','24th','25th','26th','27th','28th',
                  '29th','30th','31st']
    return 'Today is '+weekday+', '+MONTHS[month_num-1]+' the '+ORDINAL_NUMS[day_num-1]+'.'

def main():
    time.sleep(2)
    listening=True
    while listening==True:
        data=''
        data=listen()
        response=''
        if wake_word(data)==True:
            if 'stop listening' in data:
                listening=False
                response+=' Listening stopped.'
            else:
                word_list=data.split()
                for x in range(len(word_list)):
                    if x+1<=len(word_list)-1 and word_list[x].lower()=='ava':
                        question=word_list[x+1:]
                        try:
                            question=' '.join(question)
                            res=client.query(question)
                            answer=next(res.results).text
                            if '=' in answer:
                                answer_list=answer.split()
                                for y in range(len(answer_list)):
                                    if y+1<=len(answer_list)-1 and answer_list[y]=='=':
                                        answer_list=answer_list[y+1:]
                                        answer=' '.join(answer_list)
                            response+=' '+answer
                        except StopIteration:
                            question=question.split()
                            question=question[2:]
                            question=' '.join(question)
                            try:
                                wiki=wikipedia.summary(question,sentences=2,auto_suggest=False,redirect=True)
                                response+=' '+wiki
                            except wikipedia.PageError:
                                calc=eval(question)
                                response+=' '+question+' is '+str(calc)
                            except wikipedia.DisambiguationError as e:
                                question=e.options[0]
                                wiki=wikipedia.summary(question,sentences=2,auto_suggest=False,redirect=True)
                                response+=' '+wiki
                            except NameError:
                                response+= ' I could not find any information about that.'
            respond(response)
            
if __name__=='__main__':
    main()