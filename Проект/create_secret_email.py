def create_secret_email_or_number(email_or_number, email):
    if email:
        email_com = email_or_number.split('.')[1]
        email_add = email_or_number.split('@')[1].split('.')[0]
        email_add = len(email_add) * '*'
        email_name = email_or_number.split('@')[0]
        email_name = email_name[0] + (len(email_name) - 2) * '*' + email_name[-1]
        secret_email = email_name + '@' + email_add + '.' + email_com
        return secret_email
    else:
        if email_or_number[0] == '+':
            secret_number = email_or_number[:2] + '-' + '***' + '-' + '++' + '-' + email_or_number[-2:]
        else:
            secret_number = email_or_number[:1] + '-' + '***' + '-' + '++' + '-' + email_or_number[-2:]
        return secret_number