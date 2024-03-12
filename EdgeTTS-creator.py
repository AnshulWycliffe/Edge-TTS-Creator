import os
import pygame

# ENG
voice1_e = 'en-IN-NeerjaExpressiveNeural'
voice2_e = 'en-US-AndrewNeural'
voice3_e = 'en-US-AnaNeural'  # KIDS VOICE
voice4_e = 'en-US-SteffanNeural'
voice5_e = 'en-US-AriaNeural'
voice6_e = 'en-US-AvaNeural'
voice7_e = 'en-US-BrianNeural'
voice8_e = 'en-US-ChristopherNeural'
voice9_e = 'en-US-EmmaNeural'
voice10_e = 'en-US-EricNeural'
voice11_e = 'en-US-GuyNeural'
voice12_e = 'en-US-JennyNeural'
voice13_e = 'en-US-MichelleNeural'
voice14_e = 'en-US-RogerNeural'

# HINDI
voice1_h = 'hi-IN-MadhurNeural'
voice2_h = 'hi-IN-SwaraNeural'

# MALAYALAM
voice1_ml = 'ml-IN-SobhanaNeural'
voice2_ml = 'ml-IN-MidhunNeural'

#KANADA
voice1_kn = 'kn-IN-GaganNeural'
voice2_kn = 'kn-IN-SapnaNeural'

#TAMIL
voice1_tl = 'ta-IN-PallaviNeural'
voice2_tl = 'ta-IN-ValluvarNeural'

#BANGLA
voice1_bl = 'bn-IN-BashkarNeural'
voice2_bl = 'bn-IN-TanishaaNeural'

#GUJARATI
voice1_gu = 'gu-IN-DhwaniNeural'
voice2_gu = 'gu-IN-NiranjanNeural'

#MARATHI
voice1_mr = 'mr-IN-AarohiNeural'
voice2_mr = 'mr-IN-ManoharNeural'

#URDU
voice1_ur = 'ur-IN-SalmanNeural'
voice2_ur = 'ur-PK-UzmaNeural'

def speak(data):
    command = f'edge-tts --voice "{voice1_e}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

#speak("My name is Anshul Wycliffe, मेरा नाम अंशुल वाईक्लिफ है") # HINDI
        
#speak("My name is Anshul Wycliffe,എൻ്റെ പേര് അൻഷുൽ വൈക്ലിഫ്") # MALAYALAM
        
#speak("My name is Anshul Wycliffe,ನನ್ನ ಹೆಸರು ಅನ್ಶುಲ್ ವೈಕ್ಲಿಫ್") # KANADA
        
#speak("My name is Anshul Wycliffe,আমার নাম আনশুল উইক্লিফ") # BANGLA
        
#speak("My name is Anshul Wycliffe,મારું નામ અંશુલ વાઈક્લિફ છે") #GUJARATI
        
#speak("My name is Anshul Wycliffe,माझे नाव अंशुल वायक्लिफ आहे") #MARATHI
        
#speak("My name is Anshul Wycliffe,என் பெயர் அன்ஷுல் விக்லிஃப்") #TAMIL
        
#speak("My name is Anshul Wycliffe,میرا نام انشول وائکلف ہے۔") #URDU
        
#speak("pygame 2.5.2 (SDL 2.28.3, Python 3.12.2),Hello from the pygame community") # ENGLISH


        
