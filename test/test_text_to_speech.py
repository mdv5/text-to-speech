from app.text_to_speech import convert
import os

def test_convert():

    file_path = os.path.join(os.path.dirname(__file__),"mock_data","sample_text.pdf")
    output_name = "mockaudio"
    language = "fr-FR"
    gender = "MALE"
    voice_type = "Standard"


    convert(pdf_file_path=file_path, output_name = output_name, language = language, gender = gender, voice_type = voice_type)