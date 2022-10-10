import json
import pandas as pd
from datetime import datetime


def save_db(db):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    with open(f"data/messages/{ts}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(db, ensure_ascii=False))


def create_db():
    db = {"date": [], "author": [], "channel": [], "message": []}
    return db


def load_json(yemekhane_json="yemekhane.json"):
    with open("yemekhane.json", "r", encoding="utf-8") as f:
        return json.loads(f.read())


def save_json(yemekhane_dict="yemekhane.json"):
    with open("yemekhane.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(yemekhane_dict, ensure_ascii=False))


def update_json(new_json):
    old_json = load_json()
    updated_json = dict(old_json, **new_json)
    save_json(updated_json)


def add_message(db, message):
    db["date"].append(message.created_at.__str__())
    db["author"].append(message.author.__str__())
    db["channel"].append(message.channel.__str__())
    db["message"].append(message.content.__str__())
