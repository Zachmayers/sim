from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import json
from .Api_handler import Api_handler

API_handler = Api_handler()
views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('/home/home.html')



@views.route('/new', methods=['GET', 'POST'])
def new():
    activity_name_list = API_handler.get_activity_list()

    if request.method == 'POST':

        print(request.form.get('Simulation Name'))
        print(request.form.get('PlusOnes'))
        print(request.form.get('Clients'))
        return redirect('/new')

    return render_template('/new/new.html', activity_name_list=activity_name_list)