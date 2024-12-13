# **Optimización Solar API**

## 🌟 **Descripción**
Esta API permite calcular y optimizar la energía generada por un panel solar mediante un modelo matemático implementado con `numpy` y `scipy`. Calcula:
- Inclinación óptima del panel solar (θ) por hora.
- Orientación óptima del panel solar (φ) por hora.
- Energía generada hora a hora.
- Energía total generada durante el día.

Ideal para simulaciones y análisis de sistemas fotovoltaicos.

---

## 📁 **Estructura del Proyecto**

```
├── src/
│   ├── routes/
│   │   ├── __init__.py        # Inicialización del módulo de rutas
│   │   ├── SolarRoutes.py     # Definición de las rutas de la API
│   ├── services/
│   │   ├── __init__.py        # Inicialización del módulo de servicios
│   │   ├── SolarService.py    # Lógica de cálculo y optimización solar
│   ├── __init__.py            # Inicialización de la aplicación Flask
├── .gitignore                 # Archivos y carpetas a ignorar por Git
├── main.py                    # Punto de entrada principal de la API
├── README.md                  # Documentación del proyecto
├── requirements.txt           # Dependencias del proyecto
```

---

## 🛠 **Instalación**

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/
   cd "ruta/del/proyecto"
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno** (opcional):
   - Si es necesario, crea un archivo `.env` con las configuraciones específicas del entorno.

---

## 🚀 **Uso**

1. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

2. **Probar la API**:
   La API estará disponible en `http://localhost:5000`.

3. **Endpoint principal**:

   **POST** `/api/v1/solar/`

   ### **Parámetros de Entrada**
   Enviar un JSON con los siguientes campos:
   | Campo          | Tipo      | Descripción                                               |
   |----------------|-----------|-----------------------------------------------------------|
   | `A`            | `float`   | Área del panel solar (m²)                                  |
   | `eta`          | `float`   | Eficiencia del panel solar (en porcentaje, e.g., `0.20`)   |
   | `I_promedio`   | `float`   | Radiación solar promedio diaria (kWh/m²)                  |
   | `horas_sol`    | `int`     | Duración del día (en horas)                                |

   ### **Ejemplo de Entrada**
   ```json
   {
       "A": 10,
       "eta": 0.20,
       "I_promedio": 5.5,
       "horas_sol": 12
   }
   ```

   ### **Respuesta**
   | Campo                  | Tipo          | Descripción                                         |
   |------------------------|---------------|-----------------------------------------------------|
   | `Hora`                 | `int`         | Hora del día                                        |
   | `Radiación Solar`      | `float`       | Radiación solar en esa hora (kWh/m²)               |
   | `Inclinación (θ)`      | `float`       | Inclinación óptima del panel solar (°)             |
   | `Orientación (φ)`      | `float`       | Orientación óptima del panel solar (°)             |
   | `Energía Generada`     | `float`       | Energía generada por hora (kWh)                    |
   | `total_energy`         | `float`       | Energía total generada durante el día (kWh)        |

   ### **Ejemplo de Respuesta**
   ```json
   {
       "status": "success",
       "results": [
           {
               "Hora": 6,
               "Radiación Solar (kWh/m²)": 5.1,
               "Inclinación (θ)": 28.34,
               "Orientación (φ)": -10.23,
               "Energía Generada (kWh)": 8.23
           },
           {
               "Hora": 7,
               "Radiación Solar (kWh/m²)": 6.0,
               "Inclinación (θ)": 32.12,
               "Orientación (φ)": -5.10,
               "Energía Generada (kWh)": 9.41
           }
           // Más registros por cada hora del día...
       ],
       "total_energy": 85.3
   }
   ```

---

## ⚠️ **Manejo de Errores**

- **400 Bad Request**:
  - Datos faltantes o inválidos en la solicitud.
  - Ejemplo de respuesta:
    ```json
    {
        "status": "error",
        "message": "Faltan claves requeridas: {'A', 'eta'}"
    }
    ```

- **500 Internal Server Error**:
  - Error inesperado durante la ejecución del modelo.
  - Ejemplo de respuesta:
    ```json
    {
        "status": "error",
        "message": "Ocurrió un error inesperado. Por favor, intenta nuevamente."
    }
    ```

---

## 🧪 **Pruebas**

1. **Herramientas sugeridas**:
   - [Postman](https://www.postman.com/) o [cURL](https://curl.se/) para probar manualmente.
   - `pytest` para pruebas unitarias.

2. **Ejemplo con cURL**:
   ```bash
   curl -X POST http://localhost:5000/api/v1/solar/ \
   -H "Content-Type: application/json" \
   -d '{
       "A": 10,
       "eta": 0.20,
       "I_promedio": 5.5,
       "horas_sol": 12
   }'
   ```

3. **Salida esperada**:
   ```json
   {
       "status": "success",
       "results": [
           {
               "Hora": 6,
               "Radiación Solar (kWh/m²)": 5.1,
               "Inclinación (θ)": 28.34,
               "Orientación (φ)": -10.23,
               "Energía Generada (kWh)": 8.23
           }
       ],
       "total_energy": 85.3
   }
   ```

---

## 🖋 **Contribuciones**

1. Haz un fork del repositorio.
2. Crea una rama: `git checkout -b feature-nueva-funcionalidad`.
3. Realiza commits: `git commit -m 'Añadida nueva funcionalidad'`.
4. Envía un pull request.

---

## 📜 **Licencia**

Este proyecto está licenciado bajo la [MIT License](LICENSE).
```

Este README proporciona una guía completa para la instalación, uso y pruebas de la API de optimización solar. Si necesitas ajustes, ¡avísame! 😊