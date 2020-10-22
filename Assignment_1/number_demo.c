/*
Date: 09/17/2020  
Class: CS4541  
Assignment: Assignment 1 - Number Demonstration 
Author(s): Darryl Ming Sen Lee 
*/

#include<limits.h>
#include<stdio.h>

int main(){
    	//Problem 1
	printf("Problem 1\n");
    	float p1_float_var1 = 2.5;
    	printf("%.10f\n",p1_float_var1);
	printf("\n\n");

	//Problem 2
	printf("Problem 2\n");
	float p2_float_var1 = -1.0/10.0;
	printf("%.10f\n",p2_float_var1);
	printf("\n\n");

	//Problem 3
	printf("Problem 3\n");
	double p3_double_var1 = 1/3;
	printf("%f\n",p3_double_var1);

	p3_double_var1 = 1.0/3.0;
	printf("%f\n",p3_double_var1);
	printf("\n\n");

	//Problem 4
	printf("Problem 4\n");
	double p4_double_var1 = 9999999.3399999999;
	printf("%f\n",p4_double_var1);
	printf("%f\n",(float)p4_double_var1);
	printf("\n\n");

	//Problem 5
	printf("Problem 5\n");
	int p5_int_var1 = 30000*30000;
	printf("%d\n",p5_int_var1);

	p5_int_var1 = 40000*40000;
	printf("%d\n",p5_int_var1);

	p5_int_var1 = 50000*50000;
	printf("%d\n",p5_int_var1);

	p5_int_var1 = 60000*60000;
	printf("%d\n",p5_int_var1);

	p5_int_var1 = 70000*70000;
	printf("%d\n",p5_int_var1);
	printf("\n\n");
	
	//Problem 6
	printf("Problem 6\n");
	float p6_float_var1=1e20;
	printf("%f\n",p6_float_var1);

	p6_float_var1=1e20+3500000000;
	printf("%f\n",p6_float_var1);
	
	p6_float_var1=1e20+(3500000000*1000000000);
	printf("%f\n",p6_float_var1);

	float p6_float_var2=1e20;
	for(int i=0;i<1000000000;i++){
		p6_float_var2+=3500000000;
	}
	printf("%f\n",p6_float_var2);
	
	return 0;
}