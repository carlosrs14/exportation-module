import os
import sys
from decoder import *


plant_uml_path = os.path.join(os.getcwd(), "plant_uml_exc")
plant_uml_version = "plantuml-1.2025.2.jar"

# Tomar el argumento directamente sin añadir "inputs"
json_path = os.path.abspath(sys.argv[1])  # Se cambia por una ruta absoluta para evitar errores

output_path = os.path.join(os.getcwd(), "output")
diagram_name = "output"

# Se verifica si el archivo existe antes de continuar
if not os.path.exists(json_path):
    print(f"Error El archivo JSON no fue encontrado en {json_path}")
    sys.exit(1)

config = {
    "plant_uml_path": plant_uml_path,
    "plant_uml_version": plant_uml_version,
    "json_path": json_path,
    "output_path": output_path,
    "diagram_name": diagram_name,
}

json_puml = JsonPuml(config=config)
json_puml.generate_diagram()
