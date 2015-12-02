##########------------------------------------------------------##########
##########              Project-specific Details                ##########
##########    Check these every time you start a new project    ##########
##########------------------------------------------------------##########

MCU   = atmega328p
F_CPU = 8000000
BAUD = 19200
## Also try BAUD = 19200 or 38400 if you're feeling lucky.

## This is where your main() routine lives
MAIN = sensors_module.c

## If you've split your program into multiple .c / .h files,
## include the additional source (in same directory) here
LOCAL_SOURCE = dht11.c

## Here you can link to one more directory (and multiple .c files)
EXTRA_SOURCE_DIR =
EXTRA_SOURCE_FILES =

##########------------------------------------------------------##########
##########                 Programmer Defaults                  ##########
##########          Set up once, then forget about it           ##########
##########        (Can override.  See bottom of file.)          ##########
##########------------------------------------------------------##########

PROGRAMMER_TYPE = usbasp
# extra arguments to avrdude: baud rate, chip type, -F flag, etc.
PROGRAMMER_ARGS = -F -V -c $(PROGRAMMER_TYPE) -P /dev/ttyACM0 -b $(BAUD)

##########------------------------------------------------------##########
##########                   Makefile Magic!                    ##########
##########         Summary:                                     ##########
##########             We want a .hex file                      ##########
##########        Compile source files into .elf                ##########
##########        Convert .elf file into .hex                   ##########
##########        You shouldn't need to edit below.             ##########
##########------------------------------------------------------##########

## Defined programs / locations
CC = avr-gcc
OBJCOPY = avr-objcopy
OBJDUMP = avr-objdump
AVRSIZE = avr-size
AVRDUDE = avrdude

## Compilation options, type man avr-gcc if you're curious.
CFLAGS = -mmcu=$(MCU) -DF_CPU=$(F_CPU)UL -DBAUD=$(BAUD) -Os -I.
CFLAGS += -funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums
CFLAGS += -Wall -Wstrict-prototypes
CFLAGS += -g -ggdb
CFLAGS += -ffunction-sections -fdata-sections -Wl,--gc-sections -Wl,--relax
CFLAGS += -std=gnu99
## CFLAGS += -Wl,-u,vfprintf -lprintf_flt -lm  ## for floating-point printf
## CFLAGS += -Wl,-u,vfprintf -lprintf_min      ## for smaller printf

LDFLAGS = -lavrutil

## Lump target and extra source files together
TARGET = $(strip $(basename $(MAIN)))
SRC = $(TARGET).c
EXTRA_SOURCE = $(addprefix $(EXTRA_SOURCE_DIR), $(EXTRA_SOURCE_FILES))
SRC += $(EXTRA_SOURCE)
SRC += $(LOCAL_SOURCE)

## List of all header files
HEADERS = $(SRC:.c=.h)

## For every .c file, compile an .o object file
OBJ = $(SRC:.c=.o)

## Generic Makefile targets.  (Only .hex file is necessary)
all: $(TARGET).hex

%.hex: %.elf
	$(OBJCOPY) -R .eeprom -O ihex $< $@

%.elf: $(SRC)
	$(CC) $(CFLAGS) $(SRC) $(LDFLAGS) --output $@

clean:
	rm -f $(TARGET).elf $(TARGET).hex $(TARGET).obj \
	$(TARGET).o $(TARGET).d $(TARGET).eep $(TARGET).lst \
	$(TARGET).lss $(TARGET).sym $(TARGET).map $(TARGET)~ \
	$(TARGET).eeprom

##########------------------------------------------------------##########
##########              Programmer-specific details             ##########
##########           Flashing code to AVR using avrdude         ##########
##########------------------------------------------------------##########

flash: $(TARGET).hex
	$(AVRDUDE) -c $(PROGRAMMER_TYPE) -p $(MCU) $(PROGRAMMER_ARGS) -U flash:w:$<
