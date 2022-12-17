from flask import Flask, render_template

# init app
app = Flask(__name__)

#To replace with real datas
data = [
	("17-12-2022", 60),
	("16-12-2022", 100),
	("15-12-2022", 85),
	("14-12-2022", 90),
	("13-12-2022", 110),
	("12-12-2022", 60),
	("11-12-2022", 45)
]

# Route
@app.route('/')
def index():

	dates = [row[0] for row in data]
	counting = [row[1] for row in data]

	return render_template("graph.html", labels = dates, values = counting)

if __name__ == '__main__':
	app.run(debug=True)