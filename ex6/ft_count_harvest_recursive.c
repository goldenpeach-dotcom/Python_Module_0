/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkaneko <mkaneko@student.42tokyo.jp>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/25 02:05:47 by mkaneko           #+#    #+#             */
/*   Updated: 2026/06/25 02:47:21 by mkaneko          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_count_harvest_helper(int day, int days)
{
	int	i;

	i = day;
	if (i > days)
		return ;
	printf("Day %d\n", i);
	ft_count_harvest_helper(i + 1, days);
}

void	ft_count_harvest_recursive(void)
{
	int	days;

	printf("Days until Harvest: ");
	scanf("%d", &days);
	ft_count_harvest_helper(1, days);
	printf("Harvest time!");
}

int main(void)
{
	ft_count_harvest_recursive();
	return (0);
}

// def ft_count_harvest_recursive():
//     days = int(input("Days until harvest: "))
//     ft_count_harvest_helper(1, days)
//     print("Harvest time!")
// 
// 
// def ft_count_harvest_helper(day, days):
//     if day > days:
//         return
//     print(f"Day {day}")
//     ft_count_harvest(day + 1, days)