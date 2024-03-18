# Abdula Kalus SM3201269
CC = gcc
CFLAGS = -O3 -fopenmp -march=native -std=c17 -Wall -pedantic -funroll-loops
HEADERS = ${wildcard *.h}
OBJECTS = main.o pgm.o mandelbrot.o

all: main

main: ${OBJECTS} ${HEADERS}
	${CC} ${CFLAGS} -o $@ ${OBJECTS} -lm

%.o: %.c ${HEADERS}
	${CC} ${CFLAGS} -c $<

.PHONY: clean

clean:
	rm -f *.o
	rm -f *.pgm
	rm -f *.out.*
	rm -f main