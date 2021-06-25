from app.text_to_speech import convert
import os

def test_convert():

    mp3_file_path = os.path.join(os.path.dirname(__file__),"..","mockaudio.mp3")

    if os.path.isfile(mp3_file_path):
        os.remove(mp3_file_path)
    
    assert os.path.isfile(mp3_file_path) == False
    
    file_path = os.path.join(os.path.dirname(__file__),"mock_data","sample_text.pdf")
    output_name = "mockaudio"
    language = "fr-FR"
    gender = "MALE"
    voice_type = "Standard"


    convert(pdf_file_path=file_path, output_name = output_name, language = language, gender = gender, voice_type = voice_type)

    assert os.path.isfile(mp3_file_path) == True