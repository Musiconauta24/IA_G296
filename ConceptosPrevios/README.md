# Comandos
```
python --version
Python 3.13.2
git --version
git version 2.49.0.windows.1
pip list
python.exe -m pip install --upgrade pip
pip install pandas
```

## Crear entorno virtual
Creador de la carpeta env
````
python -m venv env
````
Activador del entorno virtual
````
env\scripts\activate
````
Desactivacor del entorno virtual
````
deactivate
````
Si no se activa ejecutre el comando en PowerShell como administrador:
````
set-ExecutionPolicy Unrestricted
S
 ````
# Estructura de datos en Pandas
| Tipo      | Contenido                                     |
| --------- | --------------------------------------------- |
| Series    | Arrau de una dimensión                        |
| DataFrame | Se corresponde con una tabla de 2 dimensiones |
| Palel     | Similar a un diccionario de DataFrame         |

Ejecutar un archivo de panda al estar en la carpeta que lo contiene
````
python nombrearchivo.py
````
alt + Shift + F (Formatear Hoja)

# Creación de Objeto Serie
s = pd.Series([2,4,6,8,10])
print(s)

Manejo de git
````
git init
git add .
git commit -m "Nombre"
git config --global user.email "fabianpersa24@gmail.com"
git config --global user.name "Fabián DJ Pérez"
PS D:\Trabajos de la U\Curso IA Mintic\IA_G296> git branch -M main
git remote add origin https://github.com/Musiconauta24/IA_G296.git
git push -u origin main
````
Clonar Repositorio GitHub
````
git clone https://github.com/Musiconauta24/IA_G296.git
````
Crar Archivo de requerimientos:
````
pip freeze > requirements.txt
````
Recuperar requerimientos de otro archivo
````
pip install -r requirements.txt
````