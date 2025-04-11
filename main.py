def is_very_long(password: str) -> bool:
    return len(password) > 12


def has_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)


def has_lower_letters(password: str) -> bool:
    return any(char.islower() for char in password)


def has_upper_letters(password: str) -> bool:
    return any(char.isupper() for char in password)


def has_symbols(password: str) -> bool:
    symbols = ['%', '#', '!', '_', '-']
    return any(password.__contains__(symbol) for symbol in symbols)


def get_pass_rating(password: str) -> int:
    rating = 0
    checks = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]

    for check in checks:
        if check(password):
            rating += 2

    return rating


def main():
    password = input('Введите пароль: ')
    print('Рейтинг пароля:', get_pass_rating(password))


if __name__ == '__main__':
    main()
