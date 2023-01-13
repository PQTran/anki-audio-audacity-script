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

def execute_macro(macro, timeout=5):
	start = time.time()
	client.write('Macro_' + macro.replace(' ', ''))

	reply = ''
	while reply == '' and time.time() - start < timeout:
		# print("looping duration: ", time.time() - start)
		time.sleep(0.5)
		reply = client.read()
		# print("Reply: ", reply)
	if time.time() - start >= timeout:
		print("Skipping..")


def copy_macro_output(filename):
	if os.path.exists(MACRO_OUTPUT_FILE):
		shutil.copyfile(MACRO_OUTPUT_FILE, TARGET_DIR + '/' + filename)

def clean_output_file():
	if os.path.exists(MACRO_OUTPUT_FILE):
		os.remove(MACRO_OUTPUT_FILE)

def main():
	for filename in os.listdir(SOURCE_DIR):
		if not filename.endswith('mp3'):
			continue
		print("Processing: ", filename)
		prepare_macro_input(filename)
		execute_macro('Anki Script')
		copy_macro_output(filename)
		clean_output_file()
	print("Script completed")

main()
