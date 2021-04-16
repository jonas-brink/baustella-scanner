import time
import RPi.GPIO as GPIO
from keypad import keypad

GPIO.setwarnings(False)

def inputDigit():
	digit = None
	while digit == None:
		digit = kp.getKey()
	time.sleep(0.4)
	return str(digit)

if __name__ == '__main__':
	# Initialize
	kp = keypad(columnCount = 4)
	day1 = inputDigit()
	day2 = inputDigit()
	dot1 = inputDigit()
	month1 = inputDigit()
	month2 = inputDigit()
	dot2 = inputDigit()
	year1 = inputDigit()
	year2 = inputDigit()
	year3 = inputDigit()
	year4 = inputDigit()
	print(day1 + day2 + dot1 + month1 + month2 + dot2 + year1 + year2 + year3 + year4)
