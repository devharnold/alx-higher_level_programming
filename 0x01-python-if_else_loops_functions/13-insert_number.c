#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Performing the node insertion function
 * @head: Pointer to the head list
 * @number: To be added in the list
 * Return: Upon Success - A list with new node
 * 		Else - on error otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new_node, *current;

        if (head == NULL)
                return (NULL);


        new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
                return (NULL);

        
        new_node->n = number;
        new_node->next = NULL;

        
        if (*head == NULL || number < (*head)->n)
        {
                new_node->next = *head;
                *head = new_node;
                return (*head);
        }

        current = *head;

	while (current->next != NULL && current->next->n < number)
        current = current->next;

        new_node->next = current->next;
        current->next = new_node;

        return (*head);
}
