#include "lists.h"

/**
 * check_cycle - We check for cycles in a list
 * @list: The pointer to the begining node
 *
 * Return: 0 if cycle not found, 1 if cycle found
 */
int check_cycle(listint_t *list)
{
    if (list == NULL || list->next == NULL)
        return 0;

    listint_t *current = list;
    listint_t *check = current->next;

    do {
        if (current == check)
            return (1);

        current = current->next;
        if (check->next != NULL && check->next->next != NULL)
            check = check->next->next;
        else
            return (0);
    } while (current != NULL);

    return (0);
}
