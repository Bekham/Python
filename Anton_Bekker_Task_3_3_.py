def thesaurus(args):
    """Sort names by first letter"""
    d_names = {}
    for name in args:
        names_sample = filter(lambda el: el.startswith(name[:1]), args)
        d_names[name[:1]] = list(names_sample)
    return d_names


names = ['Иван', 'Мария', 'Петр', 'Илья', 'Антон', 'Ольга', 'Олег']
print(names)
print(thesaurus(names))
