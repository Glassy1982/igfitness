from flask import Flask, render_template, request, url_for, redirect 

app = Flask(__name__)

@app.route ('/')
def index():
	return render_template('index.html')

@app.route ('/whyus')
def whyus():
	return render_template('whyus.html')

@app.route ('/about')
def about():
	return render_template('about.html')

@app.route ('/testimonials')
def testimonials():
	return render_template('testimonials.html')

@app.route ('/contact')
def contact():
        return render_template('contact.html')

@app.route ('/blog')
def blog():
        return render_template('blog.html')


if __name__ == ('__main__'):
	app.run(debug=True)
