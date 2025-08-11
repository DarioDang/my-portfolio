import os
from flask import Flask, render_template

app = Flask(__name__)

# ✅ Google Analytics config
# Read Measurement ID from environment variable (set on Render or locally)
app.config['GA_MEASUREMENT_ID'] = os.environ.get('GA_MEASUREMENT_ID', '')

# Make GA_MEASUREMENT_ID available to all templates
@app.context_processor
def inject_ga_id():
    return {'GA_MEASUREMENT_ID': app.config['GA_MEASUREMENT_ID']}

@app.route('/')
def home():
    return render_template('index.html')  # Homepage

@app.route('/taxi_ride')
def taxi_ride():
    return render_template('taxi_ride.html')  # Project detail page

@app.route('/student_retention')
def student_retention():
    return render_template('student_retention.html')

@app.route('/geospatial_crash')
def geospatial_crash():
    return render_template('geospatial_crash.html')

@app.route('/projects/million-songs')
def million_songs():
    return render_template('million_songs.html')

@app.route('/precipitation-project')
def precipitation_project():
    return render_template('precipitation_project.html')

@app.route('/cert1')
def cert1():
    return render_template('cert1.html')  

@app.route('/cert2')
def cert2():
    return render_template('cert2.html') 

@app.route('/cert3')
def cert3():
    return render_template('cert3.html') 

@app.route('/cert4')
def cert4():
    return render_template('cert4.html') 

@app.route('/cert5')
def cert5():
    return render_template('cert5.html') 

@app.route('/cert6')
def cert6():
    return render_template('cert6.html') 

if __name__ == '__main__':
    app.run(debug=True)
