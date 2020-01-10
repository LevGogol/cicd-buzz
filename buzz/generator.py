import random

first = ('Пластасовый', 'Траурный', 'Мраморный', 'солнечный')
second = ('зайчик', 'мячик', 'Нальчик')
thirth = ('стеклянного', 'дешевого', 'нелепого', 'незрячего')
fourth = ('мира', 'глаза', 'марша')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = 'Ооо, моя оборона!\n'
    phrase = buzz_terms + sample(first) + ' ' + sample(second) + ' ' + sample(thirth) + ' ' + sample(fourth)
    return phrase.title()

if __name__ == "__main__":
    print (generate_buzz())