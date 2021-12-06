PYBITES_LINK = 'http://www.amazon.com/dp/{}/?tag=pyb0f-20'


def generate_affiliation_link(url):
    asin = url.split('dp/')[-1].split('/')[0]
    return PYBITES_LINK.format(asin)