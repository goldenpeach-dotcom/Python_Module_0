def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_harvest_helper(1, days)
    print("Harvest time!")


def ft_count_harvest_helper(day, days):
    if day > days:
        return
    print(f"Day {day}")
    ft_count_harvest(day + 1, days)