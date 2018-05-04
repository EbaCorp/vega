# EBA VEGA
Speech-to-Speech solution

[![BCH compliance](https://bettercodehub.com/edge/badge/EbaCorp/vega?branch=master)](https://bettercodehub.com/)

## Intro
EBA Vega is my personal project. I'm taking chatbot to a whole new level. 
The purpose of my app is to bring speech-to-speech solution with neural networks solution in the backend.

## Project Structure
```
vega/
├ common/
```

`common/` is utils directory

## Voice output (text-to-speech) part
This is a simple implementation of `python-espeak` open-source library.

First things first. Your system should have `Python 2`. Then install package manager `pip` and environment manager `virtualenv`.

## Dependencies
Project is using `python-espeak` package for voice synthesizing.

Enter to the local environment profile by typing:

```
virtualenv my-project && cd my-project && source bin/activate
```

Run `python-espeak` package local installation by typing:

```
pip install python-espeak
```

## Usage

To use `speech.py` class' method `say()` you gotta import it firstly. Then use as a static method, like this:

```
import Speech from speech

Speech.say("Have you seen an alien, please??!!")
```

That's it, you're ready to use my text-to-speech Python wrapper.

## TODO:

- Create RESTful API on wrapper level
- Add logging to a separate file/directory

![alt text](https://i.pinimg.com/736x/79/02/1a/79021a6541f178e1e06bd70102c34ba3.jpg "Snorky")
