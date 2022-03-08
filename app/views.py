"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os

import flask
from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Property
from . import db


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

def get_uploaded_images():
    imgPaths = []
    for subdir, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
        imgPaths = files
    return imgPaths

@app.route('/properties/create', methods=["GET", "POST"])
def createProperty():
    """Render the Property Form"""
    form = PropertyForm()


    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            noBedRooms = form.noBedRooms.data
            noBathRooms = form.noBathRooms.data
            location = form.location.data
            price = form.price.data
            type = form.type.data
            description = form.type.data

            photo = request.files['photo']
            photoname = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photoname))

            property = Property(title,noBedRooms,noBathRooms,location,price,type,description,photoname)
            db.session.add(property)
            db.session.commit()
            
            flash("Property Was Added!", "success")
            return redirect(url_for("viewProperties"))

    return render_template('propertyForm.html', form=form)

@app.route('/properties')
def viewProperties():
    """Render all the properties"""
    return render_template('propertiesView.html')


@app.route('/properties/<propertyid>')
def viewProperty(propertyid):
    """Render a property by it's ID"""
    return render_template('propertyByID.html')

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
