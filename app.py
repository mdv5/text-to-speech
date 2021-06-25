from google.cloud import texttospeech
import os
from dotenv import load_dotenv
import PyPDF2

load_dotenv()

def convert(pdf_file_path, output_name, language = 'en-US',gender = "MALE",voice_type = "Standard"):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # have the user input the file path
    
    if file_path.endswith(".pdf"):
        pdfFileObject = open(file_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        pageObject = pdfReader.getPage(0)
        extracted_text = (pageObject.extractText())
        pdfFileObject.close()

    else: 
        f = open(file_path, "r")
        extracted_text = f.read()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text= extracted_text)

        # validate user input for language
    if language not in ['en-US', 'fr-FR', 'es-US']:
        print("Oops wrong language")
        return None

    # validate user input for gender
    if gender not in ['MALE','FEMALE','NEUTRAL']:
        print("Oops wrong gender")
        return None

    if voice_type not in ['Standard','Wavenet']:
        print("Oops wrong voicetype")
        return None
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code=language, 
        name=language+"-"+voice_type+"-A",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.

    print("Nice,", output_name, "should now be in your text-to-speech folder.")

    with open(output_name+".mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "', output_name, '.mp3"')


# have the user input the file path
file_path = input ("Input your file path of a PDF or TXT file: ")

#prompt user to enter a desired language
language = input("Please choose a language code, one of 'en-US', 'fr-FR', or 'es-US': ")


# validate user input for gender
gender = input("Please choose a gender for the voice, one of 'MALE', 'FEMALE', or 'NEUTRAL': ")

voice_type = input("Please choose a voice type, one of 'Standard', or 'Wavenet': ")

# The response's audio_content is binary.

output_name = input("What would you like to name your mp3 file? Type it here:  ")

convert(pdf_file_path=file_path, output_name = output_name, language = language, gender = gender, voice_type = voice_type)