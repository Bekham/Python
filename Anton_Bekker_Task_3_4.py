def thesaurus(args):
    """Sort names by last and first letter"""
    d_last_names = {}
    for last_names in args:
        last_names_sample = filter(lambda el: el.split()[1].startswith(last_names.split()[1][:1]), args)
        d_last_names[last_names.split()[1][:1]] = list(last_names_sample)
    for key, item in d_last_names.items():
        d_first_names = {}
        for first_names in item:
            first_names_sample = filter(lambda x: x.startswith(first_names[:1]), item)
            d_first_names[first_names[:1]] = list(first_names_sample)
            d_last_names[key] = d_first_names
    return d_last_names


names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
print(names)
print(thesaurus(names))
