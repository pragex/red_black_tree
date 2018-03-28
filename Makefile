# Copyright 2018 Richard Savard

DEBUG=yes
CC=gcc

EXEC=tree
DEPS= utistr.h \
      htree.h \

SRC=  utistr.c \
      htree.c \
      main.c

OBJ= $(SRC:.c=.o)

# CFLAGS+=`pkg-config --cflags sqlite3`
LDFLAGS=
# LDLIBS=`pkg-config --libs sqlite3`
LDLIBS=

ifeq ($(DEBUG),yes)
	CFLAGS=-Wall -Wextra -Wno-unused-parameter -g -O0
else
	CFLAGS=-Wall -O3
endif

all: $(EXEC)

$(EXEC): $(OBJ)
	@$(CC) -o $@ $^ $(LDFLAGS) $(LDLIBS)

main.o: $(DEPS)

%.o: %.c 
	@$(CC) -o $@ -c $< $(CFLAGS) 

.PHONY: clean mrproper

clean:
	@rm -rf *.o

mrproper: clean
	@rm -rf $(EXEC)
