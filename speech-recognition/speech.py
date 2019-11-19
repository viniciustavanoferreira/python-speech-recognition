import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Fale qualquer coisa:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language='pt-BR')
        print('Você disse: {}'.format(text))
    except:
        print('Desculpe, não fui capaz de compreender.')