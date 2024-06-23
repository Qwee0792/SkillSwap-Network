import yaml

# Cargar el archivo YAML
with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Obtener los valores de debug
debug_host = data['debug']['host']
debug_port = data['debug']['port']
debug_debug = data['debug']['debug']

# Obtener el valor de la clave flask
flask_key = data['keys']['flask']
