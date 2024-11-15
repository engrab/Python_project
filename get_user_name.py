import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

def get_user_info():
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_name = data["data"]["login"]["username"]
        country = data["data"]["location"]["country"]
        return user_name, country
    else:
        print("Something went wrong")
        
def main():
    try:
        user_name, country = get_user_info()
        print(f"User Name: {user_name} \nCountry: {country}")
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()
