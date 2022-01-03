# anki-audio-audacity-script

## Summary
This script is used to batch crop the last audio section of mp3 files. My motivation was to convert my workbook audio into flashcards.

## Pre-requisites
* Python3 [link](https://www.python.org/downloads/)
* Audacity [link](https://www.audacityteam.org/)

## Setup
* Clone this repo
* Enable mod-script-pipe [link](https://manual.audacityteam.org/man/scripting.html#Getting_Started)
* Update script variables for `SOURCE_DIR`, `TARGET_DIR`, `MACRO_INPUT_FILE`, `MACRO_OUTPUT_FILE`
* Import Audacity macro: `Anki Script.txt`

## Running
* Execute `python scripts/anki-media.py`
* All cropped audio can be found at `TARGET_DIR`
