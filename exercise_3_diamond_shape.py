# Added introduction header centered with dashes
print(" Print-a-Diamond ".center(50, "-"))

def print_diamond():

    # Loop to repeatedly ask for an odd integer until the user provides one
    while True:
        n = int(input("\nEnter an odd integer: "))

        # Check if the number is even, prompting the user to try again
        if n % 2 == 0:
            print("\nPlease provide an odd integer.")

        else:
            break

# Displaying the upper portion of the diamond, top-middle
# Displaying the lower portion of the diamond
# Call the function to print the diamond
