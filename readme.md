# Proyecto de Asistente Virtual de Turismo en Ecuador

Este proyecto tiene como objetivo desarrollar un asistente virtual de turismo enfocado en Ecuador, utilizando la inteligencia artificial de OpenAI. El asistente virtual proporcionará información y recomendaciones sobre destinos turísticos, actividades, alojamientos y más.

## Tecnologías utilizadas

- Backend: Python y Django
- Frontend: Vue.js 3

## Cómo levantar el proyecto

1. Clona el repositorio desde GitHub:

   ```
   git clone git@github.com:AndersonParra01/ia-tourism.git
   ```

2. Configura el entorno virtual e instala las dependencias del backend:

   ```
   cd tu-repositorio/backend
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Configura la base de datos y realiza las migraciones:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Levanta el servidor backend:

   ```
   python manage.py runserver
   ```

5. Instala las dependencias del frontend:

   ```
   cd ../frontend
   npm install
   ```

6. Levanta el servidor frontend:

   ```
   npm run serve
   ```

7. Accede a la aplicación en tu navegador:

   ```
   http://localhost:8080
   ```

## Colaboración

Si deseas colaborar en este proyecto, sigue los pasos anteriores para clonar y levantar el proyecto en tu entorno local. Luego, puedes realizar cambios, agregar nuevas funcionalidades y enviar pull requests para revisión.

¡Esperamos tus contribuciones!
