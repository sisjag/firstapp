from flask import Flask

app = Flask(__name__)

@app.route('/vdi1')
def vdi1():
	f = open("vd1.txt")
	devuelto =f.read()
	f.close()
	return devuelto
@app.route('/vdi2')
def vdi2():

	f = open("vd2.txt")
	devuelto =f.read()
	f.close()
	return devuelto

if __name__== '__main__':
	app.run(debug = True,host='localhost',port= 8000)

