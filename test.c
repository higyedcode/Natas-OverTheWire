#include<stdio.h>
#include<unistd.h>

int main()
{

	char name[100];
	for(int i = 0; i < 10; i++)
	{	printf("What is your name sir?\n");
		sleep(1);
	}
	gets(name);

	printf("Hello there, mr %s\n", name);
	return 0;
}
