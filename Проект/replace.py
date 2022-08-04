def replacce(object):
    object = str(object)
    object = object.replace('(', '').replace(')', '').replace(',', '').replace("'", '')
    return object