from flask import Flask, render_template, url_for, request, redirect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    sid = SentimentIntensityAnalyzer()

    if(request.method=='POST'):
        
        comment=request.form['comment']
        data=comment
        s=sid.polarity_scores(data)
        if s['compound']<0:
            my_prediction=0
        elif s['compound']>0:
            my_prediction=1
        return render_template('home.html', prediction=my_prediction)
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)