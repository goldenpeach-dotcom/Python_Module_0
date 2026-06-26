def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == 'packets':
        print(f"{seed_type.title()} seeds: {quantity} packets available")
    elif unit == 'grams':
        print(f"{seed_type.title()} seeds: {quantity} grams total")
    elif unit == 'area':
        print(f"{seed_type.title()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

# #include <stdio.h>

# void	ft_seed_invebtory(char *seed_type, int quantity, char *unit)
# {
# 	int i;
# 	char quant;

# 	i = 0;
# 	while(seed_type[i] != '\0')
# 	{
# 		if(i = 0 && 'a' <= seed_type[i] && seed_type[i] <= 'z')
# 			seed_type[i] = seed_type[i] - 32;
# 		printf("%s", seed_type[i]);
# 		i++;	
# 	}

# 	if (unit == "packets")
# 		printf(" seeds: %d packets available\n", quantity);
# 	else if (unit == "grams")
# 		printf(" seeds: %d grams total\n", quantity);
# 	else if (unit == "area")
# 		printf(" seeds: covers %d square meters\n", quantity);
# 	else
# 		printf("Unknown unit type\n")
# }

# int main(void)
# {
# 	ft_seed_invebtory("tomato", 13, "area");
# 	return (0);
# }