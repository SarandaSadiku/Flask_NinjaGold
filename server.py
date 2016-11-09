from flask import Flask, render_template,request,redirect,session
import random, datetime
app=Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities']=[]
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    buildings = {
    'farm':random.randint(10,20),
    'cave':random.randint(5,10),
    'house':random.randint(2,5),
    'casino':random.randint(-50,50)
    }
    building = request.form['building']
    if building in buildings:
        gold_gained_or_lost = buildings[building]
        session['gold'] += gold_gained_or_lost
        activity_result = {
        'color':('red','green') [gold_gained_or_lost > 0 ],
        'activity':('Entered a '+building+' and lost '+str(-(gold_gained_or_lost))+' golds...OUCH! ('+time+')','Earned '+str(gold_gained_or_lost)+' golds from the '+building+'! ('+time+')')[gold_gained_or_lost > 0]
        }
        session['activities'].append(activity_result)
    return redirect('/')

app.run(debug=True)
