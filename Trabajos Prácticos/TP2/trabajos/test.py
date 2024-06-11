def doblemayus(direccion):
    anterior = ''
    mayusdobles = False
    for car in direccion:
        if anterior.isupper() and car.isupper():
            mayusdobles = True
        anterior = car
    return mayusdobles

print(doblemayus("di aaai 1357."))

""" def doblemayus(direccion):
    anterior = ''
    mayusdobles = False
    for car in direccion:
        if car == " " or car == ".":
            continue
        else:
            if anterior.isupper() and car.isupper():
                mayusdobles = True
            anterior = car
    if mayusdobles:
        return True
    return False """


