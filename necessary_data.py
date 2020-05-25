import pandas as pd
import datetime
from datetime import date

#Shows ALL ROWS - remove for testing
pd.set_option('display.max_rows', None)

#Dataframes of county & state counts
states_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
states = pd.read_csv(states_url, delimiter = ',')
counties_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
counties = pd.read_csv(counties_url, delimiter = ',')
testvar = "lol"

#Most recent dates in each dataset
recent_states = states['date'].iloc[-1]
recent_counties = counties['date'].iloc[-1]

#State abbreviations
state_abbs = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def validate_state(state):
    upper_state = state.upper()
    if(len(state) == 2 and upper_state in state_abbs.keys()):
        entered_state = state_abbs.get(state)
        return entered_state, True
    else:
        return "State not found. Remember to send the state's abbreviation, not its full name.", False

def state_recent_stats(state_name):
    wanted = states.query('state == @state_name & date == @recent_states').drop(['fips'], axis = 1)
    state_cases = wanted['cases'].values[0]
    return state_cases

def validate_county(valid_state, county):
    capital_county = county.capitalize()
    ret = False
    try:
        wanted = counties.query('state == @valid_state & county == @capital_county & date ==@recent_states').drop(['fips'], axis = 1)
        county_cases = wanted['cases'].values[0]
        ret = True
    except:
        county_cases = "County not found. Make sure you've entered the county's name correctly & that the county is in the state you requested."
        ret = False
    return county_cases, ret