# fibonacci - Django-RestFramework
Estructura del proyecto
/rest-fibonacci
  /env          - VM del proyecto
  /rest         - proyecto
    /rest       - proyecto django base
    /fibonacci  - entidad fibonacci, vistas y reglas rest
 


Levantar el sistema: Entrar a la carpeta /rest y ejecutar el comando 
  python manage.py runserver

endpoints
  fibonacci/        -consulta las peticiones anteriores
  fibonacci/new/<int:size>      -calcula la serie fibonacci(hasta 999 elementos) y la almacena
  fibonacci/delete/<int:size>   -elimina el registro

Funcionamiento del metodo new:
  Valida que el tamamaño (cantidad de sucesiones) sea menor a 1000 (3 digitos) y que ese valor no se encuentre en la base de datos,
  en caso de que ya exita se regresa el registro, en caso de no existir se guarda el registro en la base de datos, crea el archivo
  "./storage/[tamaño].json" con la sucesiony retorna el nuevo registro creado.

Funcionamiento del metodo delete:
  Elimina el registro y el archivo json en caso de encontrarlo en la base de datos. Retorna la lista actualizada.
  
  Nota: la base de datos se encuentra en ./rest/db.sqlite3
  
