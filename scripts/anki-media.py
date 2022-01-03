#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import shutil
import pipeclient

SOURCE_DIR = '/Users/ptran/Music/anki-source'
TARGET_DIR = '/Users/ptran/Music/anki-output'
MACRO_INPUT_FILE = '/Users/ptran/Music/macro-input/anki.mp3'
MACRO_OUTPUT_FILE = '/Users/ptran/Music/macro-output/anki.mp3'

client = pipeclient.PipeClient()

def prepare_macro_input(filename):
        shutil.copyfile(SOURCE_DIR + '/' + filename, MACRO_INPUT_FILE)

def execute_macro(macro, timeout=1):
        start = time.time()
        client.write('Macro_' + macro.replace(' ', ''))

        reply = ''
        while reply == '' or time.time() - start > timeout:
                time.sleep(0.1)
                reply = client.read()

def copy_macro_output(filename):
        shutil.copyfile(MACRO_OUTPUT_FILE, TARGET_DIR + '/' + filename)

def main():
        for filename in os.listdir(SOURCE_DIR):
                if not filename.endswith('mp3'):
                        continue
                print("Processing: ", filename)
                prepare_macro_input(filename)
                execute_macro('Anki Script')
                copy_macro_output(filename)
        print("Script completed")

main()
