import collections

RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
KNOWN_FREQUENCIES = {
    'а': 0.081, 'б': 0.016, 'в': 0.048, 'г': 0.017, 'д': 0.028, 'е': 0.084, 'ё': 0.001, 'ж': 0.009,
    'з': 0.017, 'и': 0.073, 'й': 0.012, 'к': 0.035, 'л': 0.044, 'м': 0.032, 'н': 0.067, 'о': 0.107,
    'п': 0.028, 'р': 0.047, 'с': 0.053, 'т': 0.056, 'у': 0.021, 'ф': 0.0003, 'х': 0.009, 'ц': 0.004,
    'ч': 0.014, 'ш': 0.007, 'щ': 0.003, 'ъ': 0.0004, 'ы': 0.019, 'ь': 0.017, 'э': 0.003, 'ю': 0.006,
    'я': 0.020
}


def letter_frequency(text):
    total_chars = len(text)
    counter = collections.Counter(char for char in text if char in RUSSIAN_ALPHABET)
    return {char: count / total_chars for char, count in counter.items()}


def find_key(encrypted_text):
    encrypted_freqs = letter_frequency(encrypted_text)
    min_diff = float('inf')
    best_key = None

    for key in range(len(RUSSIAN_ALPHABET)):
        total_diff = 0
        for encrypted_char, encrypted_freq in encrypted_freqs.items():
            decrypted_char = RUSSIAN_ALPHABET[
                (RUSSIAN_ALPHABET.index(encrypted_char) - key) % len(RUSSIAN_ALPHABET)]
            diff = abs(encrypted_freq - KNOWN_FREQUENCIES[decrypted_char])
            total_diff += diff

        if total_diff < min_diff:
            min_diff = total_diff
            best_key = key

    return best_key


def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char in RUSSIAN_ALPHABET:
            decrypted_text += RUSSIAN_ALPHABET[(RUSSIAN_ALPHABET.index(char) - key) % len(RUSSIAN_ALPHABET)]
        else:
            decrypted_text += char
    return decrypted_text


encrypted_text = """

Фвгнкщмх орипр рстжёжнкфю мвм цкйкщжумк стрщпэл, пвёзипэл прукфжню скуюожппрл кпцртовшкк, рфпрукфжнюпр хёргпэл д срдужёпждпро кусрнюйрдвпкк к фтвпусртфктрдмж. Скъхыко утжёуфдро д яфро унхщвж, мвм ствдкнр, дэуфхсвнр уфкнр. Орипр дэёжнкфю ёдв рупрдпэч фксв фвгнкщжм: енкпбпэж (пвсткожт, х пвужнжпкб ёрнкпэ ожиёх Фкетро к Ждцтвфро), мрфртэж щвуфр кусрнюйрдвнкую ёнб скуюов мнкпрскуюа, к друмрдэж. Срунжёпкж стжёуфвднбнк ургрл ёрыжщмк, срмтэфэж унржо друмв, д фр дтжоб мвм енкпбпэж срнпруфюа уруфрбнк кй енкпэ к срунж пвпжужпкб пвёскужл щвуфр ргикевнкую ёнб сткёвпкб ко ёрсрнпкфжнюпрл стрщпруфк. Срунж яфрл стршжёхтэ, уррфджфуфджппр, кйожпкфю фжмуф гэнр хиж пждрйорипр; пвстрфкд, йвскук пв друмрдэч фвгнкщмвч орипр гэнр уфжтжфю к кусрнюйрдвфю прукфжню срдфртпр."""
key = find_key(encrypted_text)
decrypted_text = decrypt(encrypted_text, key)

print(f"Key: {key}")
print(f"Decrypted text: {decrypted_text}")
