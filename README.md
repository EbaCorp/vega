# Getting started with EBA VEGA

EBA Vega is my personal project. I'm taking chatbot to a whole new level. 
The purpose of my app is to bring speech-to-speech solution with neural networks solution in the backend.

## Voice output (text-to-speech)
This is a simple implementation of `python-espeak` open-source library.

First things first. Your system should have `Python 2`. Then install package manager `pip` and environment manager `virtualenv`.

## Dependencies

Project is using `python-espeak` package for voice synthesizing.

## How to run

Enter to the local environment profile by typing:

```
virtualenv my-project && cd my-project && source bin/activate
```

Run `python-espeak` package local installation by typing:

```
pip install python-espeak
```

Finally, run python file with all the code in:

```
python voice_test.py
```

That's it, you're ready to use my text-to-speech Python wrapper.

## TODO:

- Create RESTful API on wrapper level
- Add logging to a separate file/directory

![alt text](https://i.pinimg.com/736x/79/02/1a/79021a6541f178e1e06bd70102c34ba3.jpg "Snorky")
