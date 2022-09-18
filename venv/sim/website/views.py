from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import json


views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('/home/home.html')

@views.route('/new', methods=['GET', 'POST'])
def new():

    if request.method == 'POST':
        print('got it!')
        print(request.form.get('Simulation Name'))
        print(request.form.get('PlusOnes'))
        print(request.form.get('Clients'))
        return redirect('/new')

    return render_template('/new/new.html', doodoo="dog")