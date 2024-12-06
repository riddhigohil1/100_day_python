def calculate_love_score(name1, name2):
    name = name1.lower() + name2.lower()
    true_count = name.count('t') + name.count('r') + name.count('u') + name.count('e')
    love_count = name.count('l') + name.count('o') + name.count('v') + name.count('e')

    print(int(str(true_count) + str(love_count)))


calculate_love_score("Kanye West", "Kim Kardashian")