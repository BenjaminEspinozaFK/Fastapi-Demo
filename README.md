# 📚 FastAPI Demo - API de Alumnos

**Prueba FastAPI con REST y GraphQL**

## 🚀 Inicio Rápido

```bash
# Instalar dependencias
pip install fastapi uvicorn strawberry-graphql python-dotenv

# Ejecutar servidor
python -m uvicorn app.main:app --reload --port 8000
```

**URLs importantes:**
- API: http://localhost:8000
- Documentación: http://localhost:8000/docs
- GraphQL: http://localhost:8000/graphql

## 📊 Estructura de Datos

### Alumno
```json
{
  "id": 1,
  "nombre": "Benjamin Espinoza",
  "cursos": [
    {
      "id": 1,
      "nombre": "Diseño de Software",
      "notas": [
        {"id": 1, "valor": 7.0},
        {"id": 2, "valor": 6.5}
      ]
    }
  ]
}
```

### Modelos Pydantic
```python
class Nota(BaseModel):
    id: int
    valor: float

class Curso(BaseModel):
    id: int
    nombre: str
    notas: List[Nota]

class Alumno(BaseModel):
    id: int
    nombre: str
    cursos: List[Curso]

# Para PATCH (campos opcionales)
class AlumnoPatch(BaseModel):
    nombre: Optional[str] = None
    cursos: Optional[List[Curso]] = None
```

---

## 🔄 REST API Endpoints

### 🔓 **Sin Autenticación:**

#### GET - Obtener todos los alumnos
```
GET /alumnos/
Response: Array de Alumnos
```

#### GET - Obtener alumno por ID
```
GET /alumnos/{id}
Response: Alumno | 404 Error
```

### 🔒 **Con Autenticación (Bearer secret123):**

#### POST - Crear alumno
```
POST /alumnos/
Headers: Authorization: Bearer secret123
Body: {
  "nombre": "Nuevo Alumno",
  "cursos": []
}
Response: Alumno creado con ID asignado
```

#### PUT - Reemplazar alumno completo
```
PUT /alumnos/{id}
Headers: Authorization: Bearer secret123
Body: {
  "nombre": "Alumno Actualizado",
  "cursos": [...]
}
Response: Alumno actualizado | 404 Error
```

#### PATCH - Actualizar parcialmente
```
PATCH /alumnos/{id}
Headers: Authorization: Bearer secret123
Body: {
  "nombre": "Solo cambiar nombre"
  // cursos opcional, solo enviar campos a actualizar
}
Response: Alumno actualizado | 404 Error
```

#### DELETE - Eliminar alumno
```
DELETE /alumnos/{id}
Headers: Authorization: Bearer secret123
Response: {"message": "Alumno eliminado correctamente"} | 404 Error
```

---

## 🔍 GraphQL API

**Endpoint:** `/graphql`

### Query - Consultar datos
```graphql
query {
  alumnos {
    id
    nombre
    cursos {
      id
      nombre
      notas {
        id
        valor
      }
    }
  }
}
```

### Mutation - Crear alumno (en GraphiQL)
```graphql
mutation {
  createAlumno(nombre: "Ana García") {
    id
    nombre
    cursos {
      id
      nombre
    }
  }
}
```

### Mutation - Crear alumno (con Postman/JSON)
```json
{
  "query": "mutation { createAlumno(nombre: \"Ana García\") { id nombre cursos { id nombre } } }"
}
```

---
**Headers para REST:**
```
Authorization: Bearer secret123
```

**Métodos protegidos:** POST, PUT, PATCH, DELETE
**Métodos públicos:** GET

---

## 📝 Ejemplos Prácticos para la Prueba

### Ejemplo 1: Crear alumno con POST
```bash
curl -X POST "http://localhost:8000/alumnos/" \
  -H "Authorization: Bearer secret123" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Carlos Mendez",
    "cursos": [
      {
        "id": 1,
        "nombre": "Matemáticas",
        "notas": [
          {"id": 1, "valor": 6.8},
          {"id": 2, "valor": 7.2}
        ]
      }
    ]
  }'
```

### Ejemplo 2: Actualizar completo con PUT
```bash
curl -X PUT "http://localhost:8000/alumnos/1" \
  -H "Authorization: Bearer secret123" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Benjamin Espinoza Actualizado",
    "cursos": [
      {
        "id": 1,
        "nombre": "Ingeniería de Software",
        "notas": [
          {"id": 1, "valor": 7.0}
        ]
      }
    ]
  }'
```

### Ejemplo 3: Actualizar parcial con PATCH
```bash
curl -X PATCH "http://localhost:8000/alumnos/1" \
  -H "Authorization: Bearer secret123" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Solo cambio el nombre"
  }'
```

### Ejemplo 4: Eliminar con DELETE
```bash
curl -X DELETE "http://localhost:8000/alumnos/2" \
  -H "Authorization: Bearer secret123"
```

---

## 🧪 Prueba Rápida

1. **Iniciar servidor:**
   ```bash
   python -m uvicorn app.main:app --reload --port 8000
   ```

2. **Probar GET:**
   ```bash
   curl http://localhost:8000/alumnos/
   ```

3. **Probar POST (con auth):**
   ```bash
   curl -X POST http://localhost:8000/alumnos/ \
     -H "Authorization: Bearer secret123" \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Test", "cursos": []}'
   ```

4. **Ver documentación:**
   Ir a: http://localhost:8000/docs

---

## 🎯 Puntos Clave para la Prueba

✅ **REST:** GET, POST, PUT, PATCH, DELETE implementados    
✅ **GraphQL:** Query y Mutation básicas  
✅ **FastAPI:** Documentación automática en /docs  
✅ **Estructura:** JSON bien definido con validación Pydantic  

