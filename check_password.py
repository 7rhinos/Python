# Use this function to check your password:
# 1. have at least 10 characters;
# 2. have at least 1 uppercase letter
# 3. have at least 1 lowercase letter
# 4. have at least 1 number


def check_password(data: str) -> str:
    count_upper = 0
    count_lower = 0
    count_digit = 0

    if len(data) < 10:
        return 'Warning! At least 10 characters！'
    else:
        for ch in data:
            if ch.isupper():
                count_upper += 1
            else:
                if ch.islower():
                    count_lower += 1
                else:
                    if ch.isnumeric():
                        count_digit += 1
        if count_upper == 0:
            return 'Warning! At least one uppercase!'
        else:
            if count_lower == 0:
                return 'Warning! At least one lowercase!'
            else:
                if count_digit == 0:
                    return 'Warning! At least one number!'
                else:
                    return 'Congrats! Your password is very safe :)'


print('Please input your password to check:')
password = input()
print(check_password(password))
