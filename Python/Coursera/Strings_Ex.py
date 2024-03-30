store_id = '1101'

def zip_checker (zipcode):
    if len(zipcode) == 5:
        if zipcode[0:2] == '00':
            return 'Invalid ZIP code'
        else:
            return zipcode
    elif zipcode[0] != 0:
        zipcode = '0' + zipcode
        return zipcode
    else:
        return 'Invalid ZIP code'
        
print(zip_checker('00923'))
    
# URL_CHECKER

# Sample valid URL for reference while writing your function:
url = 'https://exampleURL1.com/r626c36'


### YOUR CODE HERE ###
def url_checker(url):
    url = url.split('/')
    protocol = url[0]
    store_id = url[-1]
    # If both protocol and store_id bad
    if protocol != 'https:' and len(store_id) != 7:
        print(f'{protocol} is an invalid protocol.',
            f'\n{store_id} is an invalid store ID.')
    # If just protocol bad
    elif protocol != 'https:':
        print(f'{protocol} is an invalid protocol.')
    # If just store_id bad
    elif len(store_id) != 7:
        print(f'{store_id} is an invalid store ID.')
    # If all ok
    else:
        return store_id
    
    
    animal = 'penguin'
    
    print(animal[ :3])