from flask import Flask,render_template,url_for,request,redirect,flash
from interface import createStory,emergency,updateStatus,Data

app = Flask(__name__)
app.secret_key='ScrumBoard'

@app.route('/')
def home():
		iceboxList,emergencyList,inprogressList,testingList,completeList,user = Data()

		return render_template('index.html', iceboxList = iceboxList, emergencyList = emergencyList, inprogressList = inprogressList, testingList = testingList, completeList = completeList,user = user)
@app.route('/addStory',methods=['GET','POST'])
def addStory():
	try:
		if request.method == 'POST':
			story = request.form['story']
			createStory(story)
			flash('Story added successfully','success')
			return redirect(url_for('home'))
	except Exception:
		flash('Error while creating story','danger')
		return redirect(url_for('home'))

@app.route('/update',methods=['GET','POST'])
def update():
	try:
		if request.method == 'POST':
			storyID = int(request.form['storyID'])
			updateStatus(storyID)
			flash('Story Updated','success')
			return redirect(url_for('home'))
	except Exception:
		flash('Error while Updating','danger')
		return redirect(url_for('home'))

@app.route('/emergency',methods=['GET','POST'])
def Emergency():
	try:
		if request.method == 'POST':
			storyID = int(request.form['storyID'])
			emergency(storyID)
			flash('Important !!','warning')
			return redirect(url_for('home'))
	except Exception:
		flash('Error while Updating','danger')
		return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)