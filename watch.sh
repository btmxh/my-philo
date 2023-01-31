#!/bin/bash

while inotifywait -e modify *.md; do
	python generator.py
done
