def get_description(info:list):
    '''Get Course Description'''
    rating_index = info.index(list(filter(lambda x:x.startswith('Rating:'), info))[0])
    if rating_index==3:
        return info[rating_index-2]
    return '-'

def get_instructor(info:list):
    '''Get Instructor'''
    rating_index = info.index(list(filter(lambda x:x.startswith('Rating:'), info))[0])
    return info[rating_index-1]

def get_rating(info:list):
    '''Get Rating'''
    rating_index = info.index(list(filter(lambda x:x.startswith('Rating:'), info))[0])
    return info[rating_index+1]

def get_reviews(info:list):
    '''Clear reviews'''
    info = [detail.strip() for detail in info]
    rating_index = info.index(list(filter(lambda x:x.startswith('Rating:'), info))[0])
    return int(info[rating_index+2][1:-1].replace(',',''))

def get_total_hours(info:list):
    '''get total course hours'''
    info = [detail.strip() for detail in info]
    hours = list(filter(lambda x: 'total' in x, info))
    if len(hours) == 0:
        return '-'
    hours_index = info.index(list(filter(lambda x: 'total' in x, info))[0])
    return info[hours_index]
    
def get_num_of_lectures(info:list):
    '''Get number of lectures'''
    info = [detail.strip() for detail in info]
    lectures = list(filter(lambda x: x.endswith('lectures'), info))
    if len(lectures)==0:
        return '-'
    lecture_index = info.index(lectures[0])
    num_of_lecture = info[lecture_index]
    return num_of_lecture[0:num_of_lecture.index('lectures')-1]

def get_difficulty(info:list):
    '''Get Difficulty level'''
    info = [detail.strip() for detail in info]
    price_index = info.index('Current price')
    return info[price_index-1]

def get_price(info:list):
    '''generate current course price'''
    info = [detail.strip() for detail in info]
    price_index = info.index('Current price')
    if info[price_index+1] == 'Free':
        return 0
    return int(info[price_index+1][2:].replace(',',''))

def get_badge(info:list):
    '''classify course badge (high-rated, best-seller, new, etc.)'''
    info = [detail.strip() for detail in info]
    if info[-1][:2] != 'Rp' and info[-1] != 'Free':
        return info[-1]
    return '-'