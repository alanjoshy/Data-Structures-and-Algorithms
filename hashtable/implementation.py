class HashTable:
    def __init__(self, size=2):
        self.size = size
        self.table = [[] for _ in range(self.size) ]  # Initialize the table with empty lists for separate chaining

    def asciiHash(self, key):
        # Calculate the ASCII-based hash by summing up ASCII values of each character
        asciiSum = sum(ord(char) for char in key)
        return (
            asciiSum % self.size
        )  # Modulo with the table size to fit within the array bounds

    def insert(self, key, value):
        # Find the bucket index using the ASCII-based hash function
        index = self.asciiHash(key)
        bucket = self.table[index]

        # Update the value if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"Updated: {key} -> {value}")
                return

        # If the key is not found, add a new key-value pair
        bucket.append((key, value))
        print(f"Inserted: {key} -> {value}")

    def get(self, key):
        # Find the bucket index using the ASCII-based hash function
        index = self.asciiHash(key)
        bucket = self.table[index]

        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v
        return None  # Return None if the key is not found

    def remove(self, key):
        # Find the bucket index using the ASCII-based hash function
        index = self.asciiHash(key)
        bucket = self.table[index]

        # Remove the key-value pair if it exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print(f"Removed: {key}")
                return
        print(f"Key not found: {key}")

    def display(self):
        # Display the current state of the hash table
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")
            else:
                print(f"Bucket {i}: Empty")


# Example usage
hashTable = HashTable()

# Insert some key-value pairs
hashTable.insert("apple", 10)
hashTable.insert("apple", 20)
hashTable.insert("banana", 20)
hashTable.insert("grape", 30)
hashTable.insert("melon", 40)

# Retrieve a value
print("Value for 'apple':", hashTable.get("apple"))

# Remove a key-value pair
hashTable.remove("banana")

# Display the hash table
hashTable.display()
