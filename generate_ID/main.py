# Import the stringid functions
from utils import is_short_id, truncate_id, generate_random_id, generate_non_crypto_id

# Example usage
example_id = generate_random_id()
print(f"Generated Random ID: {example_id}")

# Check if the generated ID looks like a short ID
if is_short_id(example_id):
    print("The generated ID looks like a short ID.")
else:
    print("The generated ID does not look like a short ID.")

# Truncate the ID to a shorter version
truncated_example_id = truncate_id(example_id)
print(f"Truncated ID: {truncated_example_id}")

# Generate a non-cryptographic random ID
non_crypto_id = generate_non_crypto_id()
print(f"Generated Non-Crypto ID: {non_crypto_id}")
