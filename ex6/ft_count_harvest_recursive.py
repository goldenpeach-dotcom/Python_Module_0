def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_harvest_helper(1, days)
    print("Harvest time!")

def ft_count_harvest_helper(day: int, days: int):
    if day > days:
        return
    print(f"Day {day}")
    ft_count_harvest_helper(day + 1, days)
