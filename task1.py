class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][i]
                    return True
        return False


# Тестуємо нашу хеш-таблицю:
H = HashTable(5)

# Вставка ключів і значень
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

# Перевірка вставлених значень
print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

# Тестуємо видалення
print("Deleting 'orange':", H.delete("orange"))  # Виведе: True (успішно видалено)
print(H.get("orange"))  # Виведе: None (коли вже не існує)

print("Deleting 'apple':", H.delete("apple"))    # Виведе: True (успішно видалено)
print(H.get("apple"))   # Виведе: None (коли вже не існує)

# Тестування видалення неіснуючого ключа
print("Deleting 'grape':", H.delete("grape"))    # Виведе: False (не існує)


