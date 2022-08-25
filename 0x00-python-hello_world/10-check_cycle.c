#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Always checks if a singly linked list has a cycle
 * @list: The singly list link we want to chevk
 *
 * Return: 1 always if has a cycle in it or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;
	int found = 0;

	while ((turtle && hare) && hare->next)
	{
		turtle = turtle->next;

		if (hare->next || hare->next->next)
			hare = hare->next->next;
		else
			break;

		if (turtle == hare)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
