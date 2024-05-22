# Flask app
from flask import Flask, render_template

app_flask = Flask(__name__)

@app_flask.route('/')
def index():
    return render_template('index.html')

# Streamlit app
import streamlit as st

def main():
    st.title('Mi Aplicación Streamlit')
    st.write('Esta es una aplicación de Streamlit integrada con Flask.')

if __name__ == '__main__':
    main()
