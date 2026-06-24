def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print(f"Day {day}")
    print("Harvest time!")


# #include <stdio.h>
# void ft_count_harvest_iterative()
# {
# 	int days;
# 	int i;
#
# 	i = 1;
# 	printf("Days until Harvest: ");
# 	scanf("%d", &days);
# 	while (i <= days)
# 	{
# 		printf("Day %d\n", i);
# 		i++;
# 	}
# 	printf("Harvest time!\n");
# }
#
# int main(void)
# {
# 	ft_count_harvest_iterative()
# 	return (0);
# }
