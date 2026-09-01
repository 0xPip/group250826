def concetenate_two_strings(string_1: str, string_2: str = '123') -> str:
    result = str(string_1) + str(string_2)
    print(result)
    return result





def is_nuber_positive(number: int | float) -> bool:
    result = number > 0
    return result