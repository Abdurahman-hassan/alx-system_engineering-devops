#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		/* Create a child process */
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			/* Child process exits immediately to become a zombie */
			exit(0);
		}
		else
		{
			perror("fork");
			return (1);
		}
	}

	/* Keep the parent process running */
	infinite_while();

	return (0);
}
