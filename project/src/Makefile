# Compiler
CC = clang++

# Compiler flags
CFLAGS = -Wall -Wextra -std=c++11

# Source file
SRC = main.cpp

# Output file
OUT = main

all: $(OUT)

$(OUT): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(OUT)

clean:
	rm -f $(OUT)