import random
from flask import Flask
from flask import jsonify

app = Flask(__name__)

recipes = [
    {
        "name": "Grilled Buttermilk Chicken",
        "ingredients": ["buttermilk", "thyme sprigs", "garlic cloves", "salt","boneless skinless chicken breast"],
        "instructions": "Place the buttermilk, thyme, garlic and salt in a large bowl or shallow dish. Add chicken and turn to coat. Refrigerate 8 hours or overnight, turning occasionally.Drain chicken, discarding marinade. Grill, covered, over medium heat until a thermometer reads 165°, 5-7 minutes per side.", 
        "ptime": 10,
        "ctime": 7,
    },
    {
        "name": "No-Bake Chocolate Oatmeal Cookies",
        "ingredients": ["brown sugar", "butter", "whole milk", "unsweetend cocoa powder", "oats", "coconut","peanut butter", "hazelnut spread", "vanilla extract", "salt"],
        "instructions": "Bring the sugar, butter, milk, and cocoa powder to a rolling boil in a medium saucepan over medium-high heat. Let boil for 1 to 2 minutes, stirring often, until mixture measures 230° on an instant read thermometer. Remove from the heat. Stir in the oats, coconut, peanut butter, chocolate-hazelnut spread, vanilla, and salt until everything is combined. Working quickly before the mixture sets up, drop tablespoons of the mixture onto the prepared pans, flattening slightly, if you like. Immediately sprinkle with more coconut; press gently to help the coconut stick to the cookies. Let stand at room temperature until firm, about 30 minutes. Store in an airtight container in a cool, dry place.",
        "ptime": 5,
        "ctime": 40,
    },
    {
        "name": "Sage Rubbed Salmon",
        "ingredients": ["Fresh Sage", "Garlic Powder", "Kosher Salt", "ground pepper", "salmon fillet","olive oil"],
        "instructions": "Preheat oven to 375°. Mix first 4 ingredients rub onto flesh side of salmon. Cut into 6 portions. In a large cast-iron skillet, heat oil over medium heat. Add salmon, skin side down cook 5 minutes. Transfer skillet to oven bake just until fish flakes easily with a fork, about 10 minutes.",
        "ptime": 10,
        "ctime": 10,
    }
]
@app.route('/Random')
def getRandomRecipe():
    random_recipe = random.choice(recipes)

    formatted_output = (
        f'<!DOCTYPE html>'
        f'<html>'
        f'<head>'
        f'    <title>Random Recipe</title>'
        f'</head>'
        f'<body>'
        f'    <h1>{random_recipe["name"]}</h1>'
        f'    <p>Ingredients: {", ".join(random_recipe["ingredients"])}</p>'
        f'    <p>Instructions: {random_recipe["instructions"]}</p>'
        f'    <p>Prep Time: {random_recipe["ptime"]} minutes</p>'
        f'    <p>Cook Time: {random_recipe["ctime"]} minutes</p>'
        f'</body>'
        f'</html>'
    )

    return formatted_output

if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
