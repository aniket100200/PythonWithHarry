import pyjokes
# print("Hello World")
"""
This is a simple joke telling program. It uses the pyjokes library to fetch a random joke and print it to the console. The joke is fetched using the get_joke() function from the pyjokes library, which returns a random joke as a string. The joke is then printed to the console using the print() function.
"""
joke = print(pyjokes.get_joke())
print(joke)