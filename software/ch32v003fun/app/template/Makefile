all: flash

# Target name for the main file
TARGET := main

# Path to the CH32V003FUN library
CH32V003FUN := ../../ch32v003fun

# Include the CH32V003FUN makefile
include $(CH32V003FUN)/ch32v003fun.mk

# Source files (.c files)
SRC := main.c  qrcode.c 

# Header files (.h files)
HDR :=  qrcode.h

# Flashing and cleaning commands
flash: cv_flash
clean: cv_clean
