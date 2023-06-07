#include "lists.h"
#include <stdbool.h>

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: linked list to check
 *
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *mainp = list;
    listint_t *skipp = list;
    bool exit = true;

    if (list == NULL)
        return (0);

    if (mainp == NULL || skipp == NULL)
        exit = false;
    else if (skipp->next == NULL)
        exit = false;

    while (exit)
    {
        mainp = mainp->next;
        skipp = skipp->next->next;
        if (mainp == skipp)
            return (1);
        if (mainp == NULL || skipp == NULL)
            exit = false;
        else if (skipp->next == NULL)
            exit = false;
    }
    return (0);
}
