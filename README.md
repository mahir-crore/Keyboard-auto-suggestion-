#  Keyboard Auto-Suggest 

This is a Flask-based Natural Language Processing (NLP) web application that provides real-time keyboard auto-suggestions. It uses word frequency analysis from a custom text corpus to generate relevant suggestions as you type.

##  Features

-  Trains on a custom text file (`autocorrect book.txt`)
-  Real-time auto-suggestions based on input
-  Word probability model using frequency count
-  Simple and responsive web interface using HTML
-  Powered by Flask backend

Project Structure

- app.py
  → Main Flask backend script

- autocorrect book.txt
  → Text corpus used for word suggestions

- Keyboard_auto_suggest.ipynb
  → Jupyter notebook for testing and experimenting with NLP logic

- templates/
    └── index.html
        → Frontend HTML template for user input and displaying suggestions

  
##  How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/keyboard_auto_suggest.git
   cd keyboard_auto_suggest

 Install dependencies:

 pip install flask

Run the app:

python app.py



