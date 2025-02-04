from flask import Blueprint, render_template
from dotenv import load_dotenv
from forms import ContactForm
from models import Contact, db




load_dotenv()


siteBluePrint = Blueprint('site', __name__)

@siteBluePrint.route('/contact', methods=['GET', 'POST'])
def contact() -> str:
     form = ContactForm()
     if form.validate_on_submit():
          new_contact_message = Contact()
          new_contact_message.ContactName = form.name.data
          new_contact_message.ContactMail = form.email.data
          new_contact_message.ContactMsg = form.contact_msg.data
     
          db.session.add(new_contact_message)
          db.session.commit()
          return render_template('site/contactthanks.html')
     else:
          print(form.validate_on_submit())
     return render_template('site/contact.html', form=form)

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')
