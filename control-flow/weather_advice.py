current_weather = input('what is the weather like today? (sunny/rainy/cold):')

if current_weather == 'sunny':
    print('wear a t-shirt and sunglass')
elif current_weather == 'rainy':
      print(f"don't forget your umbrella and raincoat.")
elif current_weather == 'cold':
    print('make sure to ware a warm coat and a scarf.')
else:
    print("sorry, i don't have a recommendations for this weather")
