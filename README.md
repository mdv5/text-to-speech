# text-to-speech
Simple Python app that calls the Google Text to Speech API

## Prerequisites

  + Anaconda 3.7+
  + Python 3.8+
  + Pip
  + Python-dotenv

## Installation

Fork this z`[remote repository] (https://github.com/mdv5/text-to-speech.git) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd text-to-speech
```

Use Anaconda to create and activate a new virtual environment, perhaps called "text-to-speech":

```sh
conda create -n text-to-speech python=3.8
conda activate text-to-speech
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify the following environment variables:

GOOGLE_APPLICATION_CREDENTIALS="ENTER FILE PATH OF GOOGLE CREDENTIALS JSON HERE"

You can obtain a Google Credentials JSON by following the steps outlined in Google's Text-to-Speech Quickstart reference material (https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries).


## Usage

Run the text-to-speech script:

```py
app/text_to_speech.py
```

Once the app is launched, you will be prompted to input the path of the file to be converted into an audio mp3 file. The app can accept either PDF for TXT files as an input. Importantly, remember to include the file name to be converted including its .pdf or .txt extension at the end of the file path (e.g., YourDrive:\YourDirectory\YourFileName.pdf).

After providing the above information, you will also be prompted to select a language code, voice gender, and voice type. Finally, you will be asked to provide a name for the mp3 file the app creates. This mp3 file will be saved in the text-to-speech folder. 
