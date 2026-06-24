def ft_harvest_total():
    day_1_harvest = int(input("Day 1 harvest: "))
    day_2_harvest = int(input("Day 2 harvest: "))
    day_3_harvest = int(input("Day 3 harvest: "))
    total = day_1_harvest + day_2_harvest + day_3_harvest
    print(f"Total harvest: {total}")

# #include <stdio.h>

# void    ft_harvest_total(void)
# {
#     int day_1_harvest;
#     int day_2_harvest;
#     int day_3_harvest;
#     int total;

#     printf("Day 1 harvest: ");
#     scanf("%d", &day_1_harvest);
#     printf("Day 2 harvest: ");
#     scanf("%d", &day_2_harvest);
#     printf("Day 3 harvest: ");
#     scanf("%d", &day_3_harvest);
#     total = day_1_harvest + day_2_harvest + day_3_harvest;
#     printf("Total harvest: %d\n", total);
# }
# int main(void)
# {
#     ft_harvest_total();
#     return (0);
# }
