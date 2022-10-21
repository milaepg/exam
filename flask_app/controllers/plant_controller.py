from flask_app import app
from flask_app import Flask, render_template, request, redirect, session, flash
from flask_app.models import user_model, plant_model 

@app.route('/plant/create', methods=['POST'])
def create_new_plant():
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')

    if not plant_model.Plant.validate_form(request.form):
        return redirect('/plant/new')
    data = {
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted'],
        'user_id': session['id']
    }
    plant_model.Plant.create_arbitrarily(data)
    return redirect('/dashboard') 

@app.route('/plant/new')
def plant_new():
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    data = { 'id': session['id'] }
    return render_template('new_plant.html', user=user_model.User.get_user_by_id(data))

@app.route('/plant/show/<int:plant_id>')
def plant_show_one(plant_id):
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    data = { 'id': plant_id }
    data_user = { 'id': session['id'] }
    return render_template('show.html', one_plant=plant_model.Plant.get_tree_by_id(data), user=user_model.User.get_user_by_id(data_user))

@app.route('/plant/edit/<int:plant_id>')
def edit_plant(plant_id):
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    data = { 'id': plant_id }
    data_user = { 'id': session['id'] }
    return render_template('edit.html', one_magazine=plant_model.Plant.get_by_id(data), user=user_model.User.get_user_by_id(data_user))
   
@app.route('/plant/update', methods=['POST'])
def update_plant():
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')

    if not plant_model.Plant.validate_form(request.form):
        id = int(request.form['id'])
        return redirect(f'/plant/edit/{id}')
    data = {
        'id': int(request.form['id']),
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'data_planted' : request.form['data_plantend']
    }
    plant_model.Plant.update_plant(data)
    return redirect('/dashboard') 

@app.route('/plant/delete/<int:plant_id>', methods=['POST'])
def delete_plant(plant_id):
    if 'id' not in session:
        flash("Please register or login to continue", "danger")
        return redirect('/')
    data = { 'id': plant_id }
    plant_model.Plant.delete_plant(data)
    return redirect('/dashboard')

@app.route('/plant/subscribe', methods=['POST'])
def subscribe_plant():
    plant_model.Plant.subscribe_plant(request.form)
    return redirect('/dashboard')

