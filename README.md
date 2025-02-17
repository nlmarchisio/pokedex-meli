# 🏆 Pokedex API - MercadoLibre Challenge

Este proyecto es una aplicación web que permite consultar información de Pokémon utilizando la **PokéAPI**.  
Está desarrollada con **Flask**, dockerizada y lista para ejecutarse fácilmente con **Docker Compose**.

---

## 🚀 Características
✅ Autenticación con **JWT y código de verificación por email**  
✅ Consulta de **tipos de Pokémon**  
✅ Búsqueda de **Pokémon aleatorio según tipo**  
✅ Obtención del **Pokémon con el nombre más largo**  
✅ UI inspirada en **MercadoLibre**

---

## 🔧 **Requisitos**
Antes de comenzar, asegúrate de tener instalado en tu sistema:

- [Docker](https://www.docker.com/get-started)  
- [Docker Compose](https://docs.docker.com/compose/install/)  
- Git (para clonar el repositorio)

---

## 📦 **Cómo ejecutar el proyecto**
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/nlmarchisio/pokedex-meli.git
cd pokedex-meli
```

### 2️⃣ Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto y define tus credenciales de email:
```env
SECRET_KEY=tu_secreto_super_seguro
EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_contraseña
```
🚨 **IMPORTANTE:** No subas este archivo a GitHub.

### 3️⃣ Construir y levantar los contenedores
Ejecuta el siguiente comando:
```bash
docker-compose up --build
```
Esto:
- Construirá la imagen Docker
- Iniciará los contenedores
- Expondrá la aplicación en `http://127.0.0.1:5000/`

### 4️⃣ Acceder a la aplicación
Abre en tu navegador:
```
http://127.0.0.1:5000/
```

### 5️⃣ Detener la aplicación
Para detener y eliminar los contenedores:
```bash
docker-compose down
```

---

## 📝 **Estructura del Proyecto**
```
/pokedex-meli
│── app.py                 # Lógica de la API con Flask
│── templates/             # HTMLs de la aplicación
│   ├── index.html         # Página principal
│   ├── login.html         # Página de login
│   ├── verify.html        # Página de verificación
│── requirements.txt       # Dependencias de Python
│── Dockerfile             # Configuración de la imagen Docker
│── docker-compose.yml     # Configuración de Docker Compose
│── .env                   # Variables de entorno (NO subir a GitHub)
│── README.md              # Documentación
```

---

## ⚠️ **Notas Importantes**
- **Si usas Windows**, ejecuta los comandos en **PowerShell o Git Bash**.  
- **Si el puerto 5000 está ocupado**, puedes cambiarlo en `docker-compose.yml`:  
  ```yaml
  ports:
    - "5001:5000"
  ```
  Luego accede a `http://127.0.0.1:5001/`

- **Si tienes problemas con `EMAIL_PASSWORD`**, activa **"Acceso de aplicaciones menos seguras"** en tu cuenta de Gmail o usa una contraseña de aplicación.

---

## 📩 **Contacto**
📧 Email: nlmarchisio93@gmail.com  
💼 LinkedIn: [linkedin.com/in/nlmarchisio93](https://www.linkedin.com/in/nlmarchisio93/)  
🚀 GitHub: [github.com/nlmarchisio](https://github.com/nlmarchisio)  

---

🌟 **¡Gracias por revisar este proyecto!** 🌟  
Si tienes algún problema al ejecutarlo, **abre un issue en GitHub** o contáctame. 🚀

