/*|**************************|*/
/*| Abdula Kalus | SM3201269 |*/
/*|**************************|*/

#ifndef _MANDELBORT_H
#define _MANDELBORT_H

// Estremo sinistro e destro dell'insieme
// Parte reale
#define R_l -2
#define R_r 1
// Parte immaginaria
#define I_l -1
#define I_r 1
// Raggio
#define R 2.0

int is_mandelbort_point(float a, float b, int M, float r);

/*
 * Function:  mandelbort_matrix 
 * --------------------
 * crea la matrice di Mandelbort contenente il colore del pixel :
 *
 *   M: numero (intero) di iterazioni 
 *   r: raggio tale per cui se un elemento della successione supera r 
 *     in modulo si considera la successione non limitata
 *   nrow: numero (intero) di righe, ovvero il numero di punti compresi tra -i ed i
 *   ncol: numero (intero) di colonne, ovvero il numero di punti compresi tra -2 e 1
 *
 *  returns: ritorna un puntatore alla matrice creata
 */
float *mandelbort_matrix(int M, float r, int nrow, int ncol);

#endif