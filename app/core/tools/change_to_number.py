import phonenumbers

def to_number_style(text):
    for match in phonenumbers.PhoneNumberMatcher(text, "PL"):
            check_number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
            return check_number
    return False

def change_to_number(number):
    number = to_number_style(number)

    if number:
        response = number
    else:
        response = "000"

    return response