# Template API Flask 


## Objetivos

Este temlate me permite demanera rápid prototipar APIs usando

    * Flask
    * SQLLite en disco o memoria
    * Pony ORM como gestor de la base de datos.

## Funcionalidades

    * Login (Usuario/Password)
    * Acceso básico a unas tablas (Employee/Team) como ejemplo de Uso


## Configuracion Basica

Configuración basica del fichero .env en local.

```bash
# PATH modulos test y src. Los test encontraran el codigo
FLASK_JWT_SUPER_SECRTET="SectretoChangeIt"
PYTHONPATH=./src:./src/test
DB_BASE_PATH=./.bbdd
DB_TEST=False
FLASK_APP=flaskr
FLASK_ENV=development
```
