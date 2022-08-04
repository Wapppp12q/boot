def exam_password(password1, password2):
    strong1 = False
    strong2 = False
    strong3 = False
    symbols = '1234567890!@#$%^&*()_+-=:;'
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    rus_alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
    if len(password1) < 8:
        return 'Короткий пароль!!!'
    for elem in password1:
        if elem in symbols:
            strong1 = True
        if elem in alphabet:
            strong2 = True
        if elem in alphabet.upper():
            strong3 = True
        if elem in rus_alphabet or elem in rus_alphabet.upper():
            return 'Используйте толька латиницу'
    if not(strong1 and strong2 and strong3):
        return 'Слабый пароль!!!'
    if password2 != password1:
        return 'Пароли не совпадают'
    return True
