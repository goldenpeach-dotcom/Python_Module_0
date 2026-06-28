def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    ft_count_harvest_helper(day)
    print("Harvest time!")


def ft_count_harvest_helper(day: int) -> None:
    if day == 0:
        return
    ft_count_harvest_helper(day - 1)
    print(f"Day {day}")
