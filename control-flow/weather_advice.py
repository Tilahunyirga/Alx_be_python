current_weather = input("What's the weather like today? (sunny/rainy/cold):")

if current_weather == 'sunny':
    print('Wear a t-shirt and sunglasses.')
elif current_weather == 'rainy':
      print(f"don't forget your umbrella and raincoat.")
elif current_weather == 'cold':
    print('make sure to ware a warm coat and a scarf.')
else:
    print("Sorry, I don't have recommendations for this weather.")