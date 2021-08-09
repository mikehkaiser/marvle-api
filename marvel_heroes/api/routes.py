from flask import Blueprint, request, jsonify
from marvel_heroes.helpers import token_required
from marvel_heroes.models import db, User, Hero, hero_schema, heroes_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getData():
    return {'some_hero': 'snapped', 'another_hero': 'unsnapped'}

@api.route('/heroes', methods = ['POST'])
@token_required
def createHero(current_user_token):
    name = request.json['name']
    alter_ego = request.json['alter_ego']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    owner_token = current_user_token.token

    hero = Hero(name, alter_ego, description, comics_appeared_in, super_power, owner_token = owner_token)

    db.session.add(hero)
    db.session.commit()

    response = hero_schema.dump(hero)
    return jsonify(response)

@api.route('/heroes', methods = ['GET'])
@token_required
def getHeroes(current_user_token):
    owner = current_user_token.token
    heroes = Hero.query.filter_by(owner_token = owner).all()
    response = heroes_schema.dump(heroes)
    return jsonify(response)

@api.route('/heroes/<id>', methods = ['GET'])
@token_required
def getHero(current_user_token, id):
    hero = Hero.query.get(id)
    response = hero_schema.dump(hero)
    return jsonify(response)

@api.route('/heroes/<id>', methods = ['POST'])
@token_required
def updateHero(current_user_token, id):
    hero = Hero.query.get(id)
    if hero:
        hero.name = request.json['name']
        hero.alter_ego = request.json['alter_ego']
        hero.description = request.json['description']
        hero.comics_appeared_in = request.json['comics_appeared_in']
        hero.super_power = request.json['super_power']
        hero.owner_token = current_user_token.token
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({'Error': "Sorry. That hero isn't here yet."})

@api.route('heroes/<id>', methods = ['DELETE'])
@token_required
def snapHero(current_user_token, id):
    hero = Hero.query.get(id)
    if hero:
        db.session.delete(hero)
        db.session.commit()
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({'Error': "Sorry. That hero isn't here yet."})