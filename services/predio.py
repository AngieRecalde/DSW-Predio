from flask import Blueprint, request, jsonify
from model.predio import Predio
from model.tipo_predio import TipoPredio
from utils.db import db

#crear un blueprint para las rutas de Predio
predios=Blueprint('predios',__name__) 

@predios.route('/predios/v1',methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@predios.route('/predios/v1/listar',methods=['GET'])
def getPredios():
    result={}
    predios=Predio.query.all()
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se recupero los PREDIOS sin inconvenientes"
    return jsonify(result),200
@predios.route('/predios/v1/insert',methods=['POST'])
def insertPredio():
    result={}
    body=request.get_json()
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')

    #verifica que todos los datos esten presentes
    if not all([id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo]):
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
     # Crea un nuevo predio
    predio = Predio(id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo)
    db.session.add(predio)
    db.session.commit()
    result["data"] = predio
    result["status_code"] = 201
    result["msg"] = "Se agregó el predio"
    return jsonify(result), 201

@predios.route('/predios/v1/update',methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id_predio = body.get('id_predio')
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')
    
    if not all([id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo]):
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    #Encuentra el predio a actualizar
    predio = Predio.query.get(id_predio)
    if not predio:
        result["status_code"] = 400
        result["msg"] = "El predio no existe"
        return jsonify(result), 400
    
    # Actualiza los valores del predio
    predio.id_tipo_predio = id_tipo_predio
    predio.descripcion = descripcion
    predio.ruc = ruc
    predio.telefono = telefono
    predio.correo = correo
    predio.direccion = direccion
    predio.idubigeo = idubigeo
    #guarda los cambios   
    db.session.commit()
    
    result["data"]=predio
    result["status_code"]=202
    result["msg"]="Se modificó el predio"
    return jsonify(result),202

@predios.route('/predios/v1/delete',methods=['DELETE'])
def deletePredio():
    result={}
    body=request.get_json()
    id_predio = body.get('id_predio')   
    if not id_predio:  # Verifica que se proporciona un ID
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result),400
    #Encuentra predio a eliminar
    predio = Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="El predio no existe"
        return jsonify(result),400
    #elimina el predio
    db.session.delete(predio)
    db.session.commit()
    
    result["data"]=predio
    result["status_code"]=200
    result["msg"]="Se eliminó el predio"
    return jsonify(result),200