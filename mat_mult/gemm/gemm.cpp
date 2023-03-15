
// gemm -- general double precision dense matrix-matrix multiplication.
//
// implement: C = alpha * A x B + beta * C, for matrices A, B, C
// Matrix C is M x N  (M rows, N columns)
// Matrix A is M x K
// Matrix B is K x N
//
// Your implementation should make no assumptions about the values contained 
// in any input parameters.

#include <omp.h>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cstddef>
#include <iostream>
using namespace std;

void gemm(int M, int N, int K, double *A, double *B, double *C, 
          double alpha, double beta){
    int i, j, kk;
    // REPLACE THIS WITH YOUR IMPLEMENTATION
    // #pragma omp for
    // for (i=0; i<M; i++){
    //     for (j=0; j<N; j++){
    //         double inner_prod = 0;
    //         for (kk=0; kk<K; kk++){
    //             inner_prod += A[i*K+kk] * B[kk*N+j];
    //         }
    //         C[i*N+j] = alpha * inner_prod + beta * C[i*N+j];
	//     }
    // }
    // END OF NAIVE IMPLEMENTATION
    
    double* B_rearrange = (double*)malloc(N*K * sizeof(double));
    int count=0;
    // #pragma omp parallel default(shared)
    // { 
    //     #pragma omp for reduction (+:count)
        for(i=0;i<N;i++){
            for(j=0;j<K;j++){
                B_rearrange[count]=B[j*N+i];
                count++;
            }
        }
    // }
    


#pragma omp parallel default(shared)
    {   
        #pragma omp for
        for (i=0; i<M; i++){
            #pragma omp parallel shared(i, M)
            {
                #pragma omp for
                for (j=0; j<N; j++){
                    double inner_prod = 0;
                        for (kk=0; kk<K; kk++){
                            inner_prod += A[i*K+kk] * B_rearrange[j*K+kk];
                            // inner_prod += A[i*K+kk] * B[kk*N+j];
                        }
                        C[i*N+j] = alpha * inner_prod + beta * C[i*N+j];
                }
            }
        }
    }
}

