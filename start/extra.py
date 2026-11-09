import requests

def get_random_user():
    url = "https://randomuser.me/api/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        user = data['results'][0]
        
        title = user['name']['title']
        first_name = user['name']['first']
        last_name = user['name']['last']
        full_name = f"{title}. {first_name} {last_name}"
        
        gender = user['gender']
        email = user['email']
        phone = user['phone']
        username = user['login']['username']
        
        street_num = user['location']['street']['number']
        street_name = user['location']['street']['name']
        city = user['location']['city']
        state = user['location']['state']
        country = user['location']['country']
        postcode = user['location']['postcode']
        address = f"{street_num} {street_name}, {city}, {state}, {country} ({postcode})"
        
        print(f"Full Name   : {full_name}")
        print(f"Gender      : {gender}")
        print(f"Email       : {email}")
        print(f"Phone       : {phone}")
        print(f"Username    : {username}")
        print(f"Address     : {address}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")

if __name__ == "__main__":
    get_random_user()
