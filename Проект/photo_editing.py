from PIL import Image


def editing_photo(path_file):
    image = Image.open(path_file)
    if image.size[0] == image.size[1] and image.size[0] != 250:
        new_im = image.resize((250, 250))
    if image.size[0] > image.size[1]:
        k = image.size[1] / 250
        size_1 = 250
        size_0 = int(image.size[0] / k)
        new_im = image.resize((size_0, size_1))
        borders = int((new_im.size[0] - 250) / 2)
        new_im = new_im.crop((borders, 0, borders + 250, 250))
    if image.size[1] > image.size[0]:
        k = image.size[0] / 250
        size_0 = 250
        size_1 = int(image.size[1] / k)
        new_im = image.resize((size_0, size_1))
        borders = int((new_im.size[1] - 250) / 2)
        new_im = new_im.crop((0, borders, 250, borders + 250))
    return new_im
