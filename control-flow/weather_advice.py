weather_conditions = ("sunny", "rainy", "cold")

user_input = input("What's the weather like today? (sunny/rainy/cold): ")

if user_input in weather_conditions:
    match user_input:
        case "sunny":
            print("Wear a t-shirt and sunglasses.")
        case "rainy":
            print("Don't forget your umbrella and a raincoat.")
        case "cold":
            print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
