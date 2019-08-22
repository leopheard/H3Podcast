import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup)
    return soup
get_soup("http://h3h3roost.libsyn.com/rss")


def get_playable_podcast(soup):
    """
    @param: parsed html page            
    """
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = desc.get_text('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "http://static.libsyn.com/p/assets/4/5/5/0/4550d3ef7a74e62b/H3_PODCAST_1_1_large.jpg"
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast(playable_podcast):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items


def get_playable_podcast1(soup):
    """
    @param: parsed html page            
    """
    subjects = []
    for content in soup.find_all('item', limit=7):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = desc.get_text('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "http://static.libsyn.com/p/assets/4/5/5/0/4550d3ef7a74e62b/H3_PODCAST_1_1_large.jpg",
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items
