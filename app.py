from flask import Flask, render_template, jsonify, request, redirect, url_for
import json

app = Flask(__name__)

application_data = []

Available_Internships = [
    {
    'id': 1,
    'title': 'system analyst',
    'location': 'Bamenda, Cameroon',
    'monthly_stipend': '100,000',
    'responsibilities': 'Responsibility 1\n Responsibility 2',
    'requirements': 'Requirement 1\n Requirement 2',
    'currency': 'CFA'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Yaounde, Cameroon',
    'monthly_stipend': '50,000',
    'responsibilities': 'Responsibility 1\n Responsibility 2',
    'requirements': 'Requirement 1\n Requirement 2',
    'currency': "CFA"
  },
  {
    'id': 3,
    'title': 'Frontend developer',
    'location': 'Remote',
    'responsibilities': 'Responsibility 1\n Responsibility 2',
    'requirements': 'Requirement 1\n Requirement 2'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Buea, Cameroon',
    'monthly_stipend': '150,000',
    'responsibilities': 'Responsibility 1\n Responsibility 2',
    'requirements': 'Requirement 1\n Requirement 2',
    'currency': 'CFA'
  },
  {
    'id': 5,
    'title': 'System Administrator',
    'location': 'Nevada, USA(remote)',
    'monthly_stipend': '7000',
    'responsibilities': 'Responsibility 1\n Responsibility 2',
    'requirements': 'Requirement 1\n Requirement 2',
    'currency': '$'
  },
  
] 

@app.route('/internships')
def internships():
  return render_template('index.html',
                         jobs=Available_Internships,
                         company_name="Rodrick's Internships")
  

@app.route('/contact')
def contact():
  return render_template('contact_page.html')


@app.route("/")
def welcome():
    return render_template('welcome_page.html')
  
    
@app.route("/api/internships")
def list_internships():
    return jsonify(Available_Internships)
  
  
@app.route("/internships/<int:id>")
def show_internship(id):
  internship = Available_Internships[id - 1]
  if not internship:
    return 'Internship not available', 404
  return render_template("internship_page.html", internship=internship, company_name="Rodrick's Internship")


@app.route("/internships/<int:id>/apply", methods =['post'])
def internship_apply(id):
  internship = Available_Internships[id - 1]
  data = request.form
  if request.method == "POST":
    name = data['full_name']
    email = data['email']
    linkedIn = data['linkedIn']
    education = data['education']
    experience = data['experience']
    resume = data['resume_url']
    application_data.append({
      'name': name,
      'email': email,
      'linkedIn': linkedIn,
      'education': education,
      'experience': experience,
      'resume': resume
    })
  return render_template('submitted_application.html', application=data, internship=internship)


@app.route('/admin')
def admin():
  json_data = jsonify(application_data)
  render_template('admin.html', applications=json_data)
  
  
@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
        # Process signup form data here
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # We could add users to database here but we have not yet found free hosting site!!
        
        # Redirecting to homepage after signup
        return redirect(url_for('internships'))
  return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)