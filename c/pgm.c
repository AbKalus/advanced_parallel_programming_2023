/*|**************************|*/
/*| Abdula Kalus | SM3201269 |*/
/*|**************************|*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>

#include "pgm.h"

/*
 * Function:  open_image
 * --------------------
 * inzilizza la struttura per la lettura e scrittura del file:
 *
 *   path: percorso del file su cui lavorare
 *   img: struttura di tipo pgm
 */
int open_image(char * path, pgm_ptr img)
{
  img->fd = fopen(path, "r+");
  if (img->fd == NULL) {
    return -1;
  }
  struct stat sbuf;
  stat(path, &sbuf);
  img->size = sbuf.st_size;
  if (fscanf(img->fd, "P5\n%d %d\n255\n", &img->width, &img->height) != 2) {
    fclose(img->fd);
    return -2;
  }
  img->offset = ftell(img->fd);
  img->data = mmap((void *)0, img->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno(img->fd), 0);
  if (img->data == MAP_FAILED) {
    fclose(img->fd);
    return -3;
  }
  return 0;
}

/*
 * Function:  empty_image
 * --------------------
 * apertura e creazione di un file vuoto
 *
 *   path: percorso del file su cui lavorare
 *   img: struttura di tipo pgm
 *   width: larghezza dell'immagine
 *   height: altezza dell'immagine
 * 
 * return: valore per specificare se l'apertura e avventua con successo
 *          se si ottiene un numero negativo è andata male
 */
int empty_image(char * path, pgm_ptr img, int width, int height)
{
  FILE * fd = fopen(path, "w+");
  if (fd == NULL) {
    return -1;
  }
  int written = fprintf(fd, "P5\n%d %d\n255\n", width, height);
  ftruncate(fileno(fd), written + width * height);
  fclose(fd);
  return open_image(path, img);
}

/*
 * Function:  save_img
 * --------------------
 * salvataggio dei dati nel file
 *
 *   img: struttura di tipo pgm
 *   m: puntatore allo spazio di memoria della matrice
 */
void save_img(pgm_ptr img, float *m)
{
  for (int y = 0; y < img->height; y++) {
    for (int x = 0; x < img->width; x++) {
      img->data[y * img->width + x + img->offset] = m[y*img->width + x];
    }
  }
}

/*
 * Function:  close_image
 * --------------------
 * chiusura del collegamento all'immagine
 *
 *   img: struttura di tipo pgm
 * 
 * return: 0 se la chiusura è avvenuta con successo 1 altrimenti
 */
int close_image(pgm_ptr img)
{
  if (img == NULL) {
    return -1;
  }
  if (munmap(img->data, img->size)) {
    return -1;
  }
  fclose(img->fd);
  return 0;
}