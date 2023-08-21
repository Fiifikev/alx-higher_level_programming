#include "lists.h"


/*
 * check_cycle - checks if a linked list
 * @list: linked list to check
 * Return: 1  and 0
 */

int check_cycle(listint_t *list)
{	
	

	listint_t *cpt  = list;
      	listint_t *cpt1 = list;

	if (list == NULL)
		return (0);


        while (cpt  && cpt1  && cpt1->next)
	{

                cpt = cpt->next;
		cpt1  = cpt->next->next;

                if (cpt  == cpt1)
			return (1);

        }


        return (0);

}
