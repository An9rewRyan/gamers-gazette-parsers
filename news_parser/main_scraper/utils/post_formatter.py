import re
import unicodedata

def format_post(post):
    
    title = format_title(post["title"])
    text = format_text(post["text"])
    date_time = format_date_time(post['date_time'])
    image = format_image(post["image"])

    formatted_post = {
        'title' : title,
        'text' : text,
        'date_time' : date_time,
        'image' : image,
    }
    return formatted_post

def delete_spaces_and_line_breaks(text):
    #usefull bullshit (for all sites)
    if type(text)==list:
        text = ' '.join(text)
    text = text.replace('\n', '')
    text = text.replace(u'\xa0', u' ')
    to_many_spaces = re.compile(r'\s\s+')
    hashtags = re.compile(r'\#\w+?\s')
    text = to_many_spaces.sub(' ', text)
    text = hashtags.sub('', text)
    text = text.strip()
    return text
    ###

def format_text(text):
    text = delete_spaces_and_line_breaks(text)
    #dtf bullshit
    twitter_window_bullshit = re.compile(r'\[\{.*\}\]')
    text = twitter_window_bullshit.sub('', text)
    ##
    return text

def format_title(title):
    title = delete_spaces_and_line_breaks(title)
    return title

def format_image(image):
    return image

def format_date_time(data_time):
    data_time = data_time.replace('T', ' ')
    data_time = data_time.replace('MSK', ' ')
    timezone_markers_end = re.compile(r'(\(.+\))|(\+.+)')
    data_time = timezone_markers_end.sub('', data_time)
    data_time = data_time.strip()

    # dtf bullshit
    if '.' in data_time:
        data_time_list = data_time.split(' ')
        date = data_time_list[0]
        time = data_time_list[1]
        
        date_list = date.split('.')
        year =  date_list[2]
        month =  date_list[1]
        day = date_list[0]

        data_time = year+'-'+month+'-'+day+' '+time
    ##
    return data_time

    # postgresql recommended datetime format:
    # 1999-01-08 04:05:06

    # dtf date_time
    # 13.02.2022 10:17:31 (Europe/Moscow)

    # igrm date_time 
    # 2022-02-11T17:14:26+03:00

    # kanob date_time
    # 2022-02-10T19:49:00+03:00

    # pgd date_time 
    # 2022-02-09T21:13:36+03:00

    # sg date_time
    # 2022-02-08T21:48:01+03:00

    # vg date_time
    # 2022-02-11MSK17:09:40+00:00

