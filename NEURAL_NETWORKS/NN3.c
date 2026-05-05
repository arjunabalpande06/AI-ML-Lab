#include <stdio.h>

int mcculloch_pitts(int x[],int w[], int n, int threshold){
    int sum = 0;
    for(int i = 0;i < n; i++){
        sum += x[i]*w[i];
    }
    if(sum >= threshold){
        return 1;
    }
    else{
        return 0;
    }
}

int main() {
	int x[2];
	int w[0] = {1, 1};
	int threshold;
	printf("Enter inputs(0 or 1):\n");
	printf("x1: ");
	scanf("%d", &x[0]);
	printf("x2: ");
	scanf("%d", &x[1]);
	//AND gate
	threshold = 2;
	printf("\nAND gate of output: %d", mcculloch_pitts(x,w,2,threshold));
	//OR gate 
	threshold=1;
	printf("\n OR gate of output: %d\n", mcculloch_pitts(x,w,2,threshold));
	return 0;
}

