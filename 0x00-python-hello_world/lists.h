#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listing_s - singly linked list 
 * @n: is an integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure for ALX project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);

#endif 
