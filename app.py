from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de datos
data = {
    'operaciones': [
        {'id': 1, 'nombre': 'Operación A', 'estado': 'completo'},
        {'id': 2, 'nombre': 'Operación B', 'estado': 'pendiente'},
        {'id': 3, 'nombre': 'Operación A', 'estado': 'pendiente'},
        {'id': 4, 'nombre': 'Operación C', 'estado': 'pendiente'}
    ],
    'documentos': [
        {'id': 1, 'titulo': 'Documento A', 'tipo': 'pdf'},
        {'id': 2, 'titulo': 'Documento B', 'tipo': 'word'},
        {'id': 3, 'titulo': 'Documento C', 'tipo': 'txt'}
    ]
    # Agregar más datos simulados según sea necesario
}

def filter_data(dataset, filters):
    return [item for item in dataset if all(item.get(k) == v for k, v in filters.items())]

@app.route('/operaciones', methods=['GET'])
def get_operaciones():
    filters = request.args.to_dict()
    filtered_data = filter_data(data['operaciones'], filters)
    return jsonify(filtered_data)

@app.route('/documentos', methods=['GET'])
def get_documentos():
    filters = request.args.to_dict()
    filtered_data = filter_data(data['documentos'], filters)
    return jsonify(filtered_data)

# Añadir más endpoints según sea necesario

if __name__ == '__main__':
    app.run(debug=True)
