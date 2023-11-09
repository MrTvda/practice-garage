from flask import Blueprint, abort, jsonify, request
from shared.model.car import Car
import logging

bp = Blueprint(name='cars', import_name=__name__, url_prefix='/')

# @cars.route('/', defaults={'page': 'index'})
@bp.route('/garages/<int:garage_id>/cars', methods=["GET"])
def car_list(garage_id):
    print(request.args)
    if request.args and 'car' in request.args:
        car = Car.get(key=request.args.get('car'))
        return jsonify({
            'id': car.id,
            'name': car.name,
            'brand': car.brand,
            'garage_id': car.garage_id,
        })
    return jsonify(
        [
            {
                'id': c.id,
                'name': c.name,
                'brand': c.brand,
                'garage_id': c.garage_id,
            } for c in Car.list(garage_id=garage_id)
        ]
    )


@bp.route('/garages/<int:garage_id>/cars', methods=["POST"])
def car_add(garage_id):
    logging.warning(garage_id)
    logging.warning(request.json)
    car = Car.add(props=request.json)
    return jsonify({
        'id': car.id,
        'name': car.name,
        'brand': car.brand,
        'garage_id': garage_id
    })

@bp.route('/garages/<int:garage_id>/cars', methods=["PUT"])
def car_update(garage_id):
    props = request.json
    car = Car.get(key=props.pop('id'))
    # print(garage)
    car.update(props=props)
    return jsonify({
        'id': car.id,
        'name': car.name,
        'brand': car.brand,
        'garage_id': garage_id
    })

@bp.route('/cars', methods=["DELETE"])
def car_delete():
    car = Car.get(key=request.json.pop('car'))
    logging.warning(request.json)
    car.delete()
    return jsonify({'status': 'OK'})
