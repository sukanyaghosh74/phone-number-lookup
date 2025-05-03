def generate_numbers(prefixees, ending_digits, output_file):
    with open(output_file, 'w') as f:
        for prefix in prefixes:
            for middle in range(10000, 100000):
                number = f"{prefix}{middle}{ending_digits}"
                f.write(number + '\n')


# Customize here
provider = "YOUR_DESIRED_PROVIDER"
state = "YOUR_DESIRED_STATE"
known_ending_digits = "02"

# Customize here
prefixes = ['XXXXX', 'XXXXX', 'XXXXX']

# Output file
output_file = "generated_numbers.txt"

# Run generator
generate_numbers(prefixes, known_ending_digits, output_file)
print(f"Numbers saved to {output_file}")
