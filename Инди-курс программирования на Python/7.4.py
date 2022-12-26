def shift_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"

    c = chr(ord('a') + (ord(letter) - ord('a') + shift) % 26)
    return c


shift_letter('a', 1)
shift_letter('b', 2)
shift_letter('z', 2)


def caesar_cipher(string: str, s: int) -> str:
    "Шифр цезаря"
    ciphered = ''.join([shift_letter(i, s) if i.isalpha() else i for i in string])
    return ciphered
