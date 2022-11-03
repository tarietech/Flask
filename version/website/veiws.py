from flask import Blueprint, render_template
from flask_login import login_required, login_user, logout_user, current_user



views = Blueprint('veiws', __name__)  

@views.route('/')
def home():
    return render_template("home.html")

     