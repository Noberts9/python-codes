class Temperature:
    def convert_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")

    def convert_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

# Create an instance of Temperature
temp = Temperature()

# Convert Celsius to Fahrenheit
celsius_temp = float(input("Enter temperature in Celsius: "))
temp.convert_fahrenheit(celsius_temp)

# Convert Fahrenheit to Celsius
fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
temp.convert_celsius(fahrenheit_temp)