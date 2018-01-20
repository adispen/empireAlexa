import logging
from lights import get_tonights_lights
from flask import Flask
from flask_ask import Ask, statement

REPOSITORY = 'adispen/empireAlexa'
ENDPOINT = 'https://api.github.com/repos/{}'.format(REPOSITORY)

app = Flask(__name__)
ask = Ask(app, '/')
logger = logging.getLogger()


@ask.launch
def launch():
    return tonights_lights()


@ask.intent("LightsTonight")
def tonights_lights():
    speech = get_tonights_lights()
    logger.info('speech = {}'.format(speech))
    return statement(speech)
