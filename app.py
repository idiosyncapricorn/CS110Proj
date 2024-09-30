from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_weekday', methods=['GET', 'POST'])
def calculate_weekday():
    if request.method == 'POST':
        try:
            january_1st_weekday = int(request.form['january_1st_weekday'])
            days_into_year = int(request.form['days_into_year'])

            january_1st = datetime.date(datetime.date.today().year, 1, 1)
            target_date = january_1st + datetime.timedelta(days=days_into_year - 1)
            target_weekday = (january_1st_weekday + target_date.weekday()) % 7  # Weekday number from 0 (Monday) to 6 (Sunday)

            weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            weekday_name = weekdays[target_weekday]

            return render_template('calculate_weekday.html', result=f"Weekday number for the given day: {target_weekday} ({weekday_name})")
        except ValueError:
            return render_template('calculate_weekday.html', result="Invalid input. Please enter valid numbers.")
    return render_template('calculate_weekday.html')

@app.route('/wedding_planning', methods=['GET', 'POST'])
def wedding_planning():
    if request.method == 'POST':
        try:
            bride_name = request.form['bride_name']
            groom_name = request.form['groom_name']
            guests = int(request.form['guests'])

            bus_capacity = 40
            num_buses = guests // bus_capacity
            extra_seats = guests % bus_capacity

            return render_template('wedding_planning.html', result=(f"Newlyweds {bride_name} and {groom_name} "
                                                                    f"need {num_buses} buses"
                                                                    f" and will have {extra_seats} extra seats available"))
        except ValueError:
            return render_template('wedding_planning.html', result="Invalid input. Please enter a valid number of guests.")
    return render_template('wedding_planning.html')

@app.route('/jackalope_population', methods=['GET', 'POST'])
def jackalope_population():
    if request.method == 'POST':
        try:
            initial_population = int(request.form['initial_population'])
            num_generations = int(request.form['num_generations'])

            final_population = calculate_jackalope_population(initial_population, num_generations)
            return render_template('jackalope_population.html', result=(f"Initial population: {initial_population}<br>"
                                                                        f"Final population: {final_population}"))
        except ValueError:
            return render_template('jackalope_population.html', result="Invalid input. Please enter valid numbers.")
    return render_template('jackalope_population.html')

def calculate_jackalope_population(initial_population, num_generations):
    population = initial_population
    for _ in range(num_generations):
        births = round(0.1 * population)
        deaths = round(0.02 * population)
        population += births - deaths
    return population

if __name__ == '__main__':
    app.run(debug=True)
