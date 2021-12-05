from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    names = []
    new_list = []
    new_new_list =[]


    for line in data[34:].splitlines():

        splitted = line.split(',')
        popped = splitted.pop()
        names = splitted[1]+' ' + splitted[0]
        new_list.append(popped)
        new_list.append(names)
        new_new_list.append(new_list)
        new_list = []
        names = []
    sorted_new_new_list = sorted(new_new_list)
    #print(sorted_new_new_list)

    res = tuple(tuple(sub) for sub in sorted_new_new_list)
    #print(res)
    for k, v in res:
        countries[k].append(v)
        d = defaultdict(str, countries)

    return d