/*|**************************|*/
/*| Abdula Kalus | SM3201269 |*/
/*|**************************|*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>

#include "pgm.h"
#include "mandelbrot.h"

int main(int argc, char *argv[]){

    // Se non sono stati passati tutti gli argomenti necessari fermare il programma
    if(argc != 4) {
        printf("The value passed as parameter are wrong\n");
        return 0;
    }

    // Inizializzazione degli attributi con i valori passati dal main
    int M = atoi(argv[2]);
    int nrows = atoi(argv[3]);
    int ncols = nrows * 1.5;
    pgm image;

    // Creazione e collegamento al file
    // Se il colelgametno nonva a buon fine stampare errore e sucire dal programma
    int err = empty_image(argv[1], &image, ncols, nrows);
    if (err != 0) {
        printf("Unable to open target image: %d\n", -err);
        return 0;
    }

    // Creazione della matrice rappresentante l'insieme di Mandelbort
    float * m = mandelbort_matrix(M, R, nrows, ncols);

    // Salvataggio immagine
    save_img(&image, m);

    // Chiusura collegamento file
    err = close_image(&image);
    if (err != 0) {
        printf("Error un-mmapping the file");
    }
    return 0;
}