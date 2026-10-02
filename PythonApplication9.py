def count_vowels_in_text():
    text = input("Введіть текст із цифр і латинських літер: ")
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}
    
    # Приводимо текст до нижнього регістру та створюємо множину символів з тексту
    text_chars_set = set(text.lower())
    
    # Визначаємо, які саме голосні присутні в тексті (перетин множин)
    found_vowels_set = text_chars_set.intersection(vowels_set)
    
    # Підраховуємо загальну кількість усіх входжень голосних літер у тексті
    # Оскільки множина містить лише унікальні елементи, для підрахунку кількості
    # кожного повторення ми перетворюємо множину знайдених голосних у список
    vowels_list = list(found_vowels_set)
    
    total_vowels_count = sum(text.lower().count(vowel) for vowel in vowels_list)
    
    # Для демонстрації зворотно перетворюємо список у множину при виведенні
    result_set = set(vowels_list)
    
    print("\n--- Результати роботи з множинами ---")
    print(f"Введений текст: {text}")
    print(f"Унікальні голосні, знайдені в тексті (множина): {result_set}")
    print(f"Загальна кількість голосних літер у тексті: {total_vowels_count}")

if __name__ == "__main__":
    count_vowels_in_text()

