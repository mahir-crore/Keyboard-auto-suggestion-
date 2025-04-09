from flask import Flask, render_template, request
import pandas as pd
import textdistance
import re
from collections import Counter

app = Flask(__name__)

# Load and preprocess text
with open('autocorrect book.txt', 'r', encoding='utf-8') as f:
    data = f.read().lower()
    words = re.findall(r'\w+', data)
    words += words  # increase frequency

# Create probability model
words_freq_dict = Counter(words)
total = sum(words_freq_dict.values())
probs = {word: freq / total for word, freq in words_freq_dict.items()}

@app.route('/')
def index():
    return render_template('index.html', suggestions=None)

@app.route('/suggest', methods=['POST'])
def suggest():
    keyword = request.form['keyword'].lower()
    if keyword:
        similarities = [1 - textdistance.Jaccard(qval=2).distance(v, keyword) for v in words_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df.columns = ['Word', 'Prob']
        df['Similarity'] = similarities
        suggestions = df.sort_values(['Similarity', 'Prob'], ascending=False)[['Word', 'Similarity']].head(10)
        suggestions_list = suggestions.to_dict('records')
        return render_template('index.html', suggestions=suggestions_list, keyword=keyword)
    return render_template('index.html', suggestions=None)

if __name__ == '__main__':
    app.run(debug=True)
