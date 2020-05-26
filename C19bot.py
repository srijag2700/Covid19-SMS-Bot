from flask import Flask, request, redirect, render_template
from twilio.twiml.messaging_response import MessagingResponse
from apscheduler.schedulers.background import BackgroundScheduler
from importlib import reload
import necessary_data as nd

# Refreshes data once every hour
def refresh():
    reload(nd)
    #print("Data Refreshed")

sched = BackgroundScheduler(daemon=True)
sched.add_job(refresh, 'interval', minutes=60)
sched.start()

# Start of Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    # Get the message the user sent
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    valid_resp = False
    credit_msg = "\n\nData courtesy of the New York Times, as of " + nd.recent_counties + "."

    list_args = body.split()

    # Single input - state abbreviation
    if (len(list_args) == 1):
        state_name, result = nd.validate_state(list_args[0].upper())
        if (result):
            state_cases = nd.state_recent_stats(state_name)
            msg_response = "There are currently " + str(state_cases) + " cases in " + state_name + ". \n\nIf you would like the count for a specific county, format your message as <state abbreviation> <county name>." + credit_msg
            #valid_resp = True
            resp.message(msg_response)
        else:
            resp.message(state_name)

    # Two inputs - state abbr. + county name
    elif (len(list_args) == 2):
        state_name, result = nd.validate_state(list_args[0].upper())
        if (result):
            # add county check with list_args[1]
            county_name = list_args[1].capitalize()
            county_cases, c_result = nd.validate_county(state_name, county_name)
            if (c_result):
                state_cases = nd.state_recent_stats(state_name)
                msg_response = "There are currently " + str(state_cases) + " cases in " + state_name + ", with " + str(county_cases) + " in " + county_name + " County." + credit_msg
                #valid_resp = True
                resp.message(msg_response)
            else:
                state_cases = nd.state_recent_stats(state_name)
                msg_response = "There are currently " + str(state_cases) + " cases in " + state_name + ". \n\n" + county_cases + credit_msg
                #valid_resp = True
                resp.message(msg_response)
        else:
            resp.message(state_name)

    # Everything else
    else:
        resp.message("Your text could not be read. Try again and format it as just <state abbreviation>, or <state abbreviation> <county>.")
    
    # Provide credit if the input is valid
    #if (valid_resp):
        #resp.message("Data courtesy of the New York Times, as of " + nd.recent_counties + ".")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)