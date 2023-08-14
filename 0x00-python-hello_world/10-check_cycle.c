#include "lists.h"
#include <stdio.h>
#include <stdbool.h>

/**
 * check_cycle - checks if singly linked list has a cycle in it.
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	if (!list)
		return (0);

	while (true)
	{
		if (f->next != NULL && f->next->next != NULL)
		{
			f = f->next->next;
			s = s->next;

			if (f == s)
				return (1);
		}
		else
			return (0);
	}

}
