/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_harvest_recursive.c                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkaneko <mkaneko@student.42tokyo.jp>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/25 02:05:47 by mkaneko           #+#    #+#             */
/*   Updated: 2026/06/28 15:32:59 by mkaneko          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_count_harvest_helper(int day)
{
	if (day == 0)
		return ;
	ft_count_harvest_helper(day - 1);
	printf("Day %d\n", day);
}

void	ft_count_harvest_recursive(void)
{
	int	days;

	printf("Days until Harvest: ");
	scanf("%d", &days);
	ft_count_harvest_helper(days);
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