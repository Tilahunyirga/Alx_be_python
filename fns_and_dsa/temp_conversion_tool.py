
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return round(celsius, 1)

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return round(fahrenheit,1)


def main():
    try:
        user_temp = float(input("Enter the temperature to convert:"))
        user_unit = input("Is this temperature in Celsius or Fahrenheit?(C/F):").strip().upper()

        if user_unit == "C":
            converted_temperature = convert_to_fahrenheit(user_temp)
            print(f"{user_temp}°C is {converted_temperature}°F")
        elif user_unit == "F":
            converted_temperature = convert_to_celsius(user_temp)
            print(f"{user_temp}°F is {converted_temperature}°C")
        else:
            print("Invalid unit , please enter 'C' for celsius or 'F' for fahrenheit.")
    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value.{e}")


if __name__ == "__main__":
    main()
