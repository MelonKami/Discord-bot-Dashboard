from bot.utils import config
import json, codecs, time
from flask import Flask
app = Flask(__name__)


def update_config():
    with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
        config = json.load(File)
    return config


def save_config(config):
    with codecs.open('bot_status.json', 'w', encoding='utf8') as File:
        json.dump(config, File, sort_keys=True, indent=4, ensure_ascii=False)


def shut_bot(config):
    if config["status"] == 'Shut down':
        statement = 'Bot has already been shut down'
    elif config["status"] == 'Running':
        statement = 'Shutting down bot'
        config["status"] = "Shut down"
        save_config(config)
    else:
        statement = 'Could not shut down bot'

    return statement

def restart_bot(config):
    if config["status"] == 'Running':
        statement = 'Restarting bot'
        config["status"] = 'Restart'
        save_config(config)
    else:
        statement = 'Could not restart'
    
    return statement

def starting_bot(config):
    if config["status"] == 'Shut down':
        statement = 'Bot is starting up'
        config["status"] = 'Start'
        save_config(config)
    else:
        statement = 'Could not start bot'

    return statement

@app.route('/restart')
def restart():
    return restart_bot(update_config())

@app.route('/shut')
def shutting_bot():
    return shut_bot(update_config())

@app.route('/start')
def start_bot():
    return starting_bot(update_config())

app.run(debug = True)