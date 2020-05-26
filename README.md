# Covid19-SMS-Bot
SMS bot that takes a state name and/or county name and returns the number of COVID-19 cases in that state and/or county. Made using Twilio and Flask, using the NYTimes COVID-19 dataset.

Text 33030-COVID (330-302-6843) with any of the following:

..*{State abbreviation} (eg. "nj" or "CA")
..*{State abbreviation} {County abbreviation} (eg. "nj mercer" or "IL Cook")

and you will get a text back with data about COVID-19 cases in that state and/or county!
Data courtesy of the New York Times.

[Instructions](https://c19-sms.herokuapp.com/)
