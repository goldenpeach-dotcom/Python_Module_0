def ft_harvest_total():
    total = 0
    for i in range(1, 4):
        harvest = int(input(f"Day {i} harvest: "))
        total += harvest
    print(f"Total harvest: {total}")
