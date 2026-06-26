/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_seed_inventory.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkaneko <mkaneko@student.42tokyo.jp>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/26 14:57:44 by mkaneko           #+#    #+#             */
/*   Updated: 2026/06/26 15:01:44 by mkaneko          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <ctype.h>

void	ft_seed_invebtory(char *seed_type, int quantity, char *unit)
{
	int		i;

	i = 0;

	if (unit != "packets" && unit != "grams" && unit != "area")
	{
		printf("Unknown unit type\n");
		return ;
	}
// 1文字目だけ大文字、残りはそのまま
	printf("%c%s seeds: ", toupper(seed_type[0]), seed_type + 1);
	if (unit == "packets")
		printf("%d packets available\n", quantity);
	else if (unit == "grams")
		printf("%d grams total\n", quantity);
	else if (unit == "area")
		printf("covers %d square meters\n", quantity);
}

int	main(void)
{
	ft_seed_invebtory("basil", 13, "spot");
	return (0);
}
