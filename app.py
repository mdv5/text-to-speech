from google.cloud import texttospeech
import os
from dotenv import load_dotenv
import PyPDF2

load_dotenv()

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# have the user input the file path
file_path = input ("Input your file path of a PDF or TXT file: ")

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

#prompt user to enter a desired language
language = input("Please choose a language code, one of 'en-US', 'fr-FR', or 'es-US': ")
# validate user input for language
if (language == "en-US") or (language == "fr-FR") or (language == "es-US"):
    True
else:
    print("OOPS, invalid language. Please try again.")
    exit()
# validate user input for gender
gender = input("Please choose a gender for the voice, one of 'MALE', 'FEMALE', or 'NEUTRAL': ")
if (gender == "MALE") or (gender == "FEMALE") or (gender == "NEUTRAL"):
    True
else:
    print("OOPS, invalid gender. Please try again.")
    exit()

voice_type = input("Please choose a voice type, one of 'Standard', or 'Wavenet': ")
if (voice_type == "Standard") or (voice_type == "Wavenet"):
    True
else:
    print("OOPS, invalid voice type. Please try again.")
    exit()

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

output_name = input("What would you like to name your mp3 file? Type it here:  ")
print("Nice,", output_name, "should now be in your text-to-speech folder.")

with open(output_name+".mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "', output_name, '.mp3"')
