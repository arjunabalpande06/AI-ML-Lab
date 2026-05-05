#include <stdio.h>

int step_function(int net){
    if(net>=0){
        return 1;
    }
    else{
        return 0;
    }
}

int main() {
	int x[4][2] = {{0,0}, {0,1}, {1,0}, {1,1}};
	int target[4] = {0,0,0,1};
	float w[2] = {0.0, 0.0};
	float bias = -0.5;
	float learning_rate = 0.1;
	int epoch, i;
	int output;
	float net;
	int error;
	for(epoch = 0; epoch<10; epoch++){
	    printf("\nEpoch %d\n", epoch + 1);
	    for(i = 0; i<4; i++){
	        net = x[i][0] * w[0] + x[i][1] * w[1] + bias;
	        output = step_function(net);
	        error = target[i] - output;
	        w[0] =w[0] + learning_rate*error*x[i][0];
	        w[1] = w[1] + learning_rate*error*x[i][1];
	        bias = bias + learning_rate * error;
	        printf("Input: %d %d Output: %d Error: %d\n", x[i][0], x[i][1], output, error);
	    }
	}
	printf("\nFinal weights:w1 = %.2f, w2 = %.2f, bias = %.2f\n", w[0], w[1], bias);
	return 0;
}

