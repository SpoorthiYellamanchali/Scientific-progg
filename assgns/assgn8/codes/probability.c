#include<stdio.h>
#include<math.h>
// function to calculate required probability
double probability(int N,int a,int b,int ab){
double pra = a/N;
double prb = b/N;
double prab = ab/N;
double prab1 = pra - prab;
return prab1;
}

