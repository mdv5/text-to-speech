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


## Usage

Run the text-to-speech script:

```py
app.py
```

PLACEHOLDER: For now the text input is hard-coded in app.py and the audio output is written to your app folder as "output.mp3". Future updates to the app will allow you to fetch the text from a local file and write it to a named output file.

