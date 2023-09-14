from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': '1',
    'title': ' JAVASCTIPT software developer',
    'location': 'bengaluru',
    'salary': '4000000'
}, {
    'id': '2',
    'title': 'FULL-STACK software developer',
    'location': 'bengaluru',
    'salary': '3000000'
}, {
    'id': '3',
    'title': ' FRONT-END software developer',
    'location': 'bengaluru',
    'salary': '2500000'
}, {
    'id': '4',
    'title': ' bACKEND software developer',
    'location': 'HYDERABAD',
    'salary': '2700000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="jovian")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
