#include <stdio.h>

/**
 * test function - test funciton that is a test
 *
 * @arg1: first argument
 * @arg2: 2nd argument
 * @arg3: 3rd arumgnet
 *
 * Return: Return value
 */

int test_function(int arg1, int arg2, int arg3)
{
	return (arg1 + arg2 + arg3);
}

/**
 * main - entry point
 *
 * Return: 0
 */
int main(void)
{
	int i =test_function(1, 2, 3);
	printf("%d\n", i);

	return (0);
}

