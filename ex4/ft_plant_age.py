def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

# #include <stdio.h>

# void ft_plant_age(void)
# {
# 	int plant_age;

# 	printf("Enter plant age in days: ")
# 	scanf("%d",&plant_age);
# 	if (plant_age > 60)
# 		printf("Plant is ready to harvest!");
# 	else
# 		printf("Plant needs more time to grow.");
# }

# int main(void)
# {
# 	ft_plant_age()
# 	return (0);
# }
