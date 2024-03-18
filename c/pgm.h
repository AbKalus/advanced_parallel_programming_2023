/*|**************************|*/
/*| Abdula Kalus | SM3201269 |*/
/*|**************************|*/

#ifndef _PGM_H
#define _PGM_H 

struct _pgm_img {
  int width;
  int height;
  int offset;
  int size;
  FILE * fd;
  char * data;
};

typedef struct _pgm_img pgm;
typedef struct _pgm_img * pgm_ptr;

int open_image(char * path, pgm_ptr img);

int empty_image(char * path, pgm_ptr img, int width, int height);

void save_img(pgm_ptr img, float *m);

int close_image(pgm_ptr img);

#endif
