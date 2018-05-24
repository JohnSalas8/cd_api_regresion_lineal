from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Resource, Api
from Services.Multiple import Multiple
from Services.Polynomial import Polynomial

app = Flask(__name__)
api = Api(app)

class APIRmultiple(Resource):
    def get(self, x1, x2, y):
        return Multiple().get_result(
            map( float, x1.split(',') ),
            map( float, x2.split(',') ),
            map( float, y.split(',') )
        )

class APIRpolynomial(Resource):
    def get(self, x, y):
        return Polynomial().get_result(
            map(float, x.split(',')),
            map(float, y.split(','))
        )

class Information(Resource):
    def get(self):
        return redirect(url_for('information.html'))
        

api.add_resource (
    APIRmultiple, 
    '/rlm/<x1>/<x2>/<y>'
)

api.add_resource (
    APIRpolynomial,
    '/rp/<x>/<y>'
)

@app.route('/')
def root():
    return render_template('information.html')


if __name__ == '__main__':
    app.run(port=2409)
    