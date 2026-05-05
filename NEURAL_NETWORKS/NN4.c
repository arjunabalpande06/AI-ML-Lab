#include <stdio.h>
#include<math.h>

double sigmoid(double x) {
    return 1.0 / (1.0 + exp(-x));
}

/*Feedback neural network*/
int main() {
    double input[2]  = {1.0 , 0.5};
    
    double weights_inputs_hidden[2][2] = {
        {0.15 , 0.20}
        ,{0.25 , 0.30}
    };
    
    /* Biases for hidden layer*/
    double bias_hidden[2] = {0.35, 0.35};
    
    /* Weights from hidden to output layer*/
    double weights_hidden_output[2] = {0.40, 0.45};
    
    /*Bias for output layer*/
    double bias_output = 0.60;
    
    /*Hidden layer output*/
    double hidden[2];
    
    /*Forwrd pass: Input - Hidden */
    for (int i = 0; i < 2; i++) {
        hidden[i] += input[j] * weights_inputs_hidden[j][i];
    }
    
    /*Forward pass: Hidden - Output*/
    double output = bias_output;
    for (int i = 0; i < 2 ; i++) {
        output += hidden[i] * weights_hidden_output;
    }
    output = sigmoid(output);
    
    /*Print result*/
    printf("Output of the neural network: %.6f\n", output);
    
    return 0;
}