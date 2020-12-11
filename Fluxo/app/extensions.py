from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint, request, jsonify

db = SQLAlchemy()
migrate = Migrate()
