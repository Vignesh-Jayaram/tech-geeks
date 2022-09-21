import csv
from flask import Flask, render_template, request, redirect

# app object created with the __main__ file.
app = Flask(__name__)




# Returns base root 
@app.route('/')
def base_root():
    return render_template("index.html")
 
# Returns all the html pages
@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)
 
# Save the user's info in a text format:
def data_to_txt(data):
    with open("database.txt", 'a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f"{email}, {subject}, {message}")
        file.write("\n")
    return 0


# Save the user's info in a csv format: 
def data_to_csv(data):
    with open("database.csv", newline='', mode='a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(file)
        writer.writerow([email, subject, message])
    return 0


# Submitting messages in the contact page:
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_to_csv(data)
        return redirect("thanks.html")
    else:
        return "Something went wrong. Try again."
    



