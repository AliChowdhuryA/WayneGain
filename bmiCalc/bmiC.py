import random
from flask import Flask
from flask import request


from flask import render_template_string

app = Flask(__name__)

def calculate_bmi(wPound, hFeet, hInch):
    wkg = wPound * 0.453592
    hTotal = (hFeet * 12) + hInch
    hMeters = hTotal * 0.0254
    bmi = wkg / (hMeters ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    
    elif 25 <= bmi < 29.9:
        return "Overweight"
    
    else:
        return "Obese"

@app.route('/bmi', methods=['GET', 'POST'])

def bmiCal():
    if request.method == 'POST':
        try:
            wPound = float(request.form['weight'])

            hFeet = float(request.form['hFeet'])

            hInch = float(request.form['hInch'])

            bmi = calculate_bmi(wPound, hFeet, hInch)
            category = interpret_bmi(bmi)

            result = f"""
                <h1>BMI Calculator</h1>
                <br>
                <h3> Less Than 18.5 Underweight </h3>
                <h3> 18.5 to 24.9 Normal Weight </h3>
                <h3> 25 to 29.9 Overweight </h3>
                <h3> More Than 30 Underweight </h3>
                </br>

                <P>Current BMI: {bmi:.1f}</P>

                <p>You are {category}.</p>

            """

            return render_template_string(result)
        
        except ValueError:
            error = "Input Invalid"
            return render_template_string(f"<p>{error}</p>")

    else:
        input_template = """
            <h1>BMI Calculator</h1>
                <br>
                <h3> Less Than 18.5 Underweight </h3>
                <h3> 18.5 to 24.9 Normal Weight </h3>
                <h3> 25 to 29.9 Overweight </h3>
                <h3> More Than 30 Underweight </h3>
                </br>

            <form action="/bmi" method="post">

                <label for="weight">Weight(lb)   </label>
                <input type="text" name="weight" id="weight" required>
                <br>

                <label for="hFeet">Height (ft)    </label>
                <input type="text" name="hFeet" id="hFeet" required>

                <br>

                <label for="hInch">Height (in)    </label>
                <input type="text" name="hInch" id="hInch" required>
                </br>
                <input type="submit" value="Submit">

            </form>
        """

        return render_template_string(input_template)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=8000)

