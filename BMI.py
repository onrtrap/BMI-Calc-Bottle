from bottle import route, run, get, request, Bottle, post, template

tempBMI = 'BMI.tpl'
tempResult = 'Result.tpl'
temp = tempBMI
weight = 10
height = 10


@route('/')
def default():
    return '''
    <h1>Placeholder</h1>
    <h2><a href= /BMI><em>Go to BMI Calculator<em></a></h2>
    '''


@route('/BMI')
@route('/BMI/<name>')
def start():
    return template(tempBMI)


@route('/Result', method='GET')
def get_bmi():
    bmi = 'Bad Input'
    if request.query.get('weight') != '' and request.query.get('height') != '':
        if int(request.query.get('weight')) > 0 and int(request.query.get('height')) > 0:
            weight = float(request.query.get('weight'))
            height = float(request.query.get('height'))
            bmi = (weight / height ** 2) * 703
    return template(tempResult, bmi=bmi)


run(host='localhost', port=8080)
