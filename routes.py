from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages

# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route('/', methods=['GET', 'POST'])
def home():
    form=MessageForm()
    
    if form.validate_on_submit():
        # check if user exits in database
        # if not create user and add to database
        # create row in Message table with user (created/found) add to ta database

        #from Messsageform, getting info that is submitted by user and filtered by first in the list      
        user = User.query.filter_by(author=form.author.data).first()
        if user is None:
            #supposed to create new users if none are found
            new_user = User(author = form.author.data)
            db.session.add(new_user)
            db.session.commit()
            
            

            #supposed to create a row in message table  with user and add to database
            comment = Messages(message = form.message.data, user_id = User.query.filter_by(author = form.author.data).first().id)
            db.session.add(comment)
            db.session.commit()
            
        
    posts = [
        {
            'author': 'Carlos',
            'message': 'Yo! Where you at?!'
        },
        {
            'author': 'Jerry',
            'message': 'Home. You?'
        }
    ]
    
    # this is supposed to get a list and then add it to posts
    list_log = Messages.query.all()
    
    for l in list_log:
    
        list = [
            {
                'author': f'{User.query.filter_by(id = l.id).first().author}',
                'message': f'{l.message}'
            }         
        ] 
    
        posts.append(list)
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    return render_template('home.html', posts=posts, form=form)

