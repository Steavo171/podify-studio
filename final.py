from gtts import gTTS
import pyttsx3

def text_to_audio_gtts(text, language='en', output_file='output.mp3'):
    
    tts = gTTS(text=text, lang=language)
    

    tts.save(output_file)
    
    print(f"Text converted to speech and saved as '{output_file}'")

def text_to_audio_pyttsx3(text, language='en', output_file='output.mp3'):


    engine = pyttsx3.init()


    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level


    engine.setProperty('language', language)

    engine.save_to_file(text, output_file)


    engine.runAndWait()

    print(f"Text converted to speech and saved as '{output_file}'")

def read_text_from_file(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    print("Welcome to Text-to-Speech Converter!")
    print("Choose the library you want to use:")
    print("1. gTTS (Google Text-to-Speech)")
    print("2. pyttsx3")

    choice = input("Enter your choice (1 or 2): ")

    text = ""
    if choice in ['1', '2']:
        text_source = input("Enter '1' to enter text manually or '2' to read from a file: ")
        if text_source == '1':
            text = input("Enter the text to convert to speech: ")
        elif text_source == '2':
            file_path = input("Enter the path to the text file: ")
            text = read_text_from_file(file_path)
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    language = input("Enter the language code (e.g., 'en' for English): ")
    output_file = input("Enter the output file name: ")

    if choice == '1':
        text_to_audio_gtts(text, language, output_file)
    elif choice == '2':
        text_to_audio_pyttsx3(text, language, output_file)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
