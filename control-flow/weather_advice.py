weather_conditions = ("sunny", "rainy", "cold")

weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather in weather_conditions:
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
            print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
