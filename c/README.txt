Abdula Kalus SM3201269

Frattale_di_Mandelbrot
----------------------

Il progetto non è particolarmente articolato, sono state definite esclusivamente i file necessari ovvero
pgm per la lettura e scrittura su file e mandelbrot per la generazione dell'insieme.

Nel file mandelbort.c è stata possibile aggiungere un'unica paralelizzazione nei cicli for innestati, e 
rendendo il codice dove possibile branchless.

Un ultima ottimizzazione applicata è a livello di ottimizzazione, ovvero olltre alle solite ottimizzazione
è stato aggiunto -funroll-loops al comando di compilazione, il quale abilità lo srotolamento dei cicli
ovvero un ciclo di 1000 iterazioni nella forma v[i]++; è sostituito da 100 iterazioni della forma:
 v[i]++; v[i+1]++; … v[i+9]++