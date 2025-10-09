import requests

def main():
    print("Welcome to the Weather Forcast!")
    print("Are you planning to go somewhere?") #to get weather report
    print("Perhaps you would like to know the weather for this place.")
    print("Look no further!")
    print("")
    print("With this program, you can get the weather of any location very easily!")
    city = input("Just enter the name of the city: ")
    report(city)

def report(c):
    url = 'https://wttr.in/{}'.format(c)
    try:
        data = requests.get(url)
        T = data.text
    except: 
        T = "Error Occurred"
    print(T)

if __name__ == "__main__":
    main()