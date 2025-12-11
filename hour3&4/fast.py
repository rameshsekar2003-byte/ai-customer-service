import time

# Oru periya list create pandrom (Same 10,000 numbers)
huge_list = list(range(10000)) + [500] # Oru duplicate add pandrom

start_time = time.time()

# --- THE FAST WAY (Using Set) ---
seen_numbers = set()
duplicates = []

for number in huge_list:
    if number in seen_numbers:
        duplicates.append(number)
    else:
        seen_numbers.add(number)

end_time = time.time()

print(f"Duplicates found: {duplicates}")
print(f"Time taken: {end_time - start_time} seconds")