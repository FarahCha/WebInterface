#http://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
   0 : {'name' : 'Ellbogen', 'state' : GPIO.LOW},
   2 : {'name' : 'Schulter', 'state' : GPIO.LOW}
   }

for pin in pins:
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)


@app.route('/')
def main():
    for pin in pins:
		pins[pin]['state'] 0 GPIO.input(pin)
	
	templateData={
		'pins' : pins
	}

	return render_template('home.html', **templateData)

@app.route("/<changePin>/action>")
def action(changePin, action):
	changePin = int (changePin)
	deviceName= pins[changePin] ['name']
	
	if action == "rauf"
		GPIO.output(changePin,GPIO.HIGH)
		message = deviceName+ "wurde rauf bewegt."
		# hier gehört noch ein Befehl damit wir Impulse dem Servo schicken können

	if action == "runter"
		GPIO.output(changePin,GPIO.HIGH)
		message = deviceName+ "wurde runter bewegt."
		# hier gehört noch ein Befehl damit wir Impulse dem Servo schicken können
	
	for pin in pins:
		pins[pin]['state']= GPI.input(pin)
	
	templateDate = {
		'pins' : pins
	}

	return render_template('home.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
