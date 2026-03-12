# Guia Didactica del Profesor — Nuevo Companeros 1

> Proyecto en desarrollo activo. Todo puede cambiar.

Sistema de 3 capas para generar la guia del profesor del curso de espanol A1.1 "Nuevo Companeros 1" (SGEL, adolescentes 12-15 anos).

## Las 3 capas

1. **Guia impresa** (en desarrollo) — Guia editorial con explotaciones didacticas para 9 unidades. Producto impreso para SGEL.
2. **Sistema de agentes** (en redefinicion) — Agentes IA que generan las explotaciones. Arquitectura sujeta a cambio.
3. **Guias personalizadas** (futuro) — Los agentes sirven a profesores individuales para adaptar la guia a su grupo y necesidades.

## Estructura del repositorio

```
guia-didactica-profesor-IA/
├── CLAUDE.md                      # Instrucciones del proyecto
├── 00-curso-general.md            # Orientaciones del curso
├── marco-teorico-metodologico.md  # Fundamentos teoricos
├── CHANGELOG.md                   # Historial de cambios
│
├── agentes/                       # Agentes + orquestador (puede cambiar)
├── repertorios/                   # Opciones de explotacion (puede cambiar)
├── unidades/                      # U01-U09, cada una en su carpeta (UXX/)
├── datos/                         # Inventarios JSON + imagenes del libro
├── referencias/                   # Bancos de tecnicas pedagogicas
├── materiales/                    # Pildoras formativas (LaTeX/PDF) + tarjetas
├── material-complementario/       # PDFs editoriales + PowerPoint
├── tarjetas/                      # Diseno InDesign de tarjetas
└── diseno/                        # Propuestas del sistema de agentes
```

## Estado actual

- **U03 (La Familia):** Vocabulario, Gramatica e Itinerarios completos. Comunicacion, Destrezas, Cultura, Reflexion y Evaluacion pendientes.
- **U01-U02, U04-U09:** Plantillas preparadas, sin contenido.
- **Infraestructura pedagogica:** Marco teorico, curso general y bancos de tecnicas completos.

Ver `CLAUDE.md` para estado detallado.
