/*|**************************|*/
/*| Abdula Kalus | SM3201269 |*/
/*|**************************|*/

#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>
#include <omp.h>

#include "mandelbrot.h"


/*
 * Function:  is_mandelbort_point
 * --------------------
 * ritorna il valore dell'ultima iterazione prima di uscire dall'insime di mandelbort:
 *
 *   a: parte reale del punto
 *   r: parte immaginaria del punti
 *   M: numeri di iterazioni
 *   r: raggio tale per cui se un elemento della successione supera r
 *     in modulo si considera la successione non limitata
 *  
 *  return: numero di iterazioni fatte prima di sucrei dall'insieme
 */
int is_mandelbort_point(float a, float b, int M, float r)
{
    double complex c = a + b * I;
    double complex z = c;
    double complex z_aux = 0;
    int k = 1;
    while ((k <= M) && (cabs(z) <= r))
    {   
        // Calcolo in sucecssioni di due punti della successione per ciclo
        // Dimezza il numero di cicli fatti
        z_aux = z * z + c;
        z = z_aux * z_aux + c;
        k += 2;
    }

    // Siccome vengono fatti due salti bisogna verificare che il punto precedente
    // sia minore o uguale del raggio
    k += (cabs(z_aux) < r) * 1;
    return k;
}

/*
 * Function:  mandelbort_matrix
 * --------------------
 * crea la matrice contenente l'insieme di Mandelbort (contenente il colore del pixel):
 *
 *   M: numero (intero) di iterazioni
 *   r: raggio tale per cui se un elemento della successione supera r
 *     in modulo si considera la successione non limitata
 *   nrow: numero (intero) di righe, ovvero il numero di punti compresi tra -i ed i
 *   ncol: numero (intero) di colonne, ovvero il numero di punti compresi tra -2 e 1
 *
 *  returns: ritorna un puntatore alla matrice creata
 */
float *mandelbort_matrix(int M, float r, int nrows, int ncols)
{   
    // Creo un puntatore a una zona di memoria di dimnesione nrows * ncols * sizeof(float)
    float *m = (float *)malloc(nrows * ncols * sizeof(float));

    // Definisico i limiti degli intervalli 
    // Sono state usate delle costanti in modo tale da permettere la modifica dal file .h
    float a_max = R_r;
    float a_min = R_l;
    float b_max = I_r;
    float b_min = I_l;

    // Calcolo della distanza dei punti
    float dx = (a_max - a_min) / ncols;
    float dy = (b_max - b_min) / nrows;

    float a, b, k;
    
    // Allocazione del colore del punto calcoalto come da consegna nella matrice
    // Parallelizzazione dei due cicli innestatu per la scrittura sulla matrice 
    #pragma omp parallel for collapse(2) 
    for (int i = 0; i < nrows; i += 1) {
        for (int j = 0; j < ncols; j += 1) {
            b = b_max - i * dy;
            a = a_min + j * dx;

            // Calcolo appartenenza del punto
            k = is_mandelbort_point(a, b, M, r);
            m[i * ncols + j] = (k < M) * round(255 * log(k) / log(M)) + (k >= M) * 255;
        }
    }
    return m;
}