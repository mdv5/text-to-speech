# text-to-speech
Simple Python app that calls the Google Text to Speech API

Open a terminal and go to a directory on your computer where you want to store the project

``` sh
mkdir text-to-speech
```
``` sh
cd text-to-speech
```
Clone the project from github
```sh
git clone https://github.com/mdv5/text-to-speech.git
```
Create credentials to be used with the app
PLACEHOLDER TO CREATE AN API KEY and store the JSON file that contains it
For now quick-start guidance is available in Google's documentation: https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries

***Mac/Linux***
Set up a virtual environment and install the google-cloud-texttospeech #Section to be replaced with CONDA and requirements.txt file
```sh
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-cloud-texttospeech
```

Set the environment variable #Section to be replaced with dotenv package so environment variable can be stored and accessed locally
```sh
export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

Example
```sh
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
```

***Windows***
Set up a virtual environment and install the google-cloud-texttospeech #Section to be replaced with CONDA and requirements.txt file

```pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-cloud-texttospeech
```

Set the environment variable #Section to be replaced with dotenv package so environment variable can be stored and accessed locally

```sh
$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```

Example
```sh
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"
```
