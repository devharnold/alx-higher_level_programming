#include "lists.h"

/**
 * check_cycle - cheking for cycles in a list using this function
 * @list: The pointer to the begining of the node
 *
 * Return: Upon Success - Found cycle (1) if otherwise (0)
 */
int check_cycle(listint_t *list)
{
        listint_t *current, *check;

        if (list == NULL || list->next == NULL)
                return 0;
        current = list;
        check = current->next;

        while (current != NULL && check->next != NULL
                && check->next->next != NULL)
        {
                if (current == check)
                        return 1;
                current = current->next;
                check = check->next->next;
        }
        return 0;
}

