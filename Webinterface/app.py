#http://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
#ein Array erstellen wo die pins drinnen sind mit ihrem namen und state 
pins = {
   0 : {'name' : 'Ellbogen', 'state' : GPIO.LOW},
   2 : {'name' : 'Schulter', 'state' : GPIO.LOW}
   }

#pins als output und low einstellen
for pin in pins:
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

#wenn man die Seite ganz normal aufruft
@app.route('/')
def main():
    for pin in pins:
		pins[pin]['state'] 0 GPIO.input(pin)
	
	templateData={
		'pins' : pins
	}

	return render_template('home.html', **templateData)

#wenn man in der Html-Datei auf eine Funktion drückt, übergibt diese der Phyton-Datei dieses den Pin und ob rauf oder runter weiter 
@app.route("/<changePin>/action>")
def action(changePin, action):
	changePin = int (changePin)
	deviceName= pins[changePin] ['name']
	
	if action == "rauf"
		GPIO.output(changePin,GPIO.HIGH)
		message = deviceName+ "wurde rauf bewegt."
		#mit dem Befehl unten sollte man die Impulse ändern(bin mir aber nicht sicher was für Impulse wir brauchen, deshalb bitte statt dem Hashtag das Richtige hinschreiben)
		pins[changePin].ChangeDutyCyle(#)
			
	if action == "runter"
		GPIO.output(changePin,GPIO.HIGH)
		message = deviceName+ "wurde runter bewegt."
		#mit dem Befehl unten sollte man die Impulse ändern(bin mir aber nicht sicher was für Impulse wir brauchen, deshalb bitte statt dem Hashtag das Richtige hinschreiben)
		pins[changePin].ChangeDutyCyle(#)
			
	for pin in pins:
		pins[pin]['state']= GPI.input(pin)
	
	templateDate = {
		'pins' : pins
	}

	return render_template('home.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
