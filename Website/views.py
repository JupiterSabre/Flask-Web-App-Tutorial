# Store standard roots for your website (main directory)
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Bike
from . import db




views = Blueprint("views", __name__)



@views.route("/", methods=["GET", "POST"])
@login_required #Assured you cannot access homepage without being logged in.
def home():
    if request.method == "POST":
    # Get the data from the form:
        manufacture = request.form.get("manufacture")
        bike_type = request.form.get("type")
        frame_height = request.form.get("frame-height")
        lock_combo = request.form.get("lock-combo")
        date_registered = request.form.get("date-registered")

        new_bike = Bike(
            manufacture = manufacture,
            type = bike_type,
            frame_height = frame_height,
            lock_combo = lock_combo,
            date_registered = date_registered
        )

        db.session.add(new_bike)
        db.session.commit()
        flash("Bike Registered", category="success")
        return redirect(url_for("views.home"))
        

    return render_template("home.html", member=current_user)