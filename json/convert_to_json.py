import json
import re
import collections

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    new_list = []
    pattern = r'[;,/\:|]'
    fixed = re.sub(pattern, ',', members)
    keys = fixed.strip().splitlines()[0].split(',')
    Point = collections.namedtuple('Point', keys)
    for elem in fixed.strip().splitlines()[1:]:
        e = elem.split(',')
        p = Point(e[0], e[1],e[2], e[3])
        d = p._asdict()

        new_list.append(d)
    return json.dumps(new_list)
