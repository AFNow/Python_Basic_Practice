def find_duplicates(lst):
    duplicates = []
    seen = set()
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

# Тестовые данные
print(find_duplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 5])) # вернет [1, 2, 5]