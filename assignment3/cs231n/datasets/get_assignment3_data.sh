#!/bin/bash

# Following scripts assume wget for Windows (http://gnuwin32.sourceforge.net/packages/wget.htm)
# installed as 'C:\Program Files (x86)\GnuWin32\bin\wget.exe'
# Ran from Git Bash
./get_coco_captioning.sh
./get_squeezenet_tf.sh
./get_imagenet_val.sh

