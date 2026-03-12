# Especificaciones de diseno de tarjetas

## Tamano y configuracion InDesign

### Documento nuevo

| Campo | Valor |
|-------|-------|
| Ancho | 63 mm |
| Alto | 88 mm |
| Paginas | 2 (frontal + posterior) |
| Paginas opuestas | Si |
| Margenes | 3 mm (todos los lados) |
| Sangrado (bleed) | 3 mm (todos los lados) |

Area util dentro de margenes: 57 x 82 mm

### Impresion

- 8 tarjetas por hoja A4 (2 columnas x 4 filas)
- Impresion a doble cara (cara frontal + cara posterior alineadas)
- Lineas de corte incluidas en la exportacion PDF

## Sistema de colores

### Colores de tarjeta por tipo/caja (pastel, fondo de la tarjeta)

| Caja | Tipo | Color pastel | Codigo HEX |
|------|------|-------------|-------------|
| Caja 1 | Vocabulario | Rosa pastel | #F2D7D9 |
| Caja 2 | Gramatica / Pistas | Verde pastel | #D4EDDA |
| Caja 3 | Estrategia | Amarillo pastel | #FFF3CD |

El color pastel del fondo permite al profesor identificar de un vistazo el tipo de tarjeta.

### Colores de campo semantico (oscuros, para icono/badge)

| Campo semantico | Color | Codigo HEX aproximado |
|----------------|-------|----------------------|
| Familia | Violeta oscuro | #6B3FA0 |
| Profesiones | Naranja oscuro | #D4730E |

El badge/icono con color oscuro identifica el campo semantico dentro de cada tarjeta.

### Colores de genero gramatical (para detalle/acento visual)

| Genero | Color | Codigo HEX | CMYK |
|--------|-------|-----------|------|
| Masculino | Azul celeste | #7EC8E3 | C=45 M=5 Y=5 K=0 |
| Femenino | Rojo coral | #F28B82 | C=0 M=50 Y=40 K=0 |

Colores claros para buen contraste sobre los fondos oscuros de campo semantico (violeta, naranja).

### Colores de texto sobre fondo de genero

| Fondo genero | Color texto principal | HEX | Color texto secundario | HEX |
|-------------|----------------------|-----|----------------------|-----|
| Azul celeste (masculino) | Azul marino | #1B3A5C | Blanco | #FFFFFF |
| Rojo coral (femenino) | Pendiente de definir | - | Pendiente de definir | - |

## Tipografia

| Uso | Fuente | Peso |
|-----|--------|------|
| Palabra (titulo) | Proxima Nova | Bold |
| Frase de ejemplo | Proxima Nova | Regular |
| Informacion posterior | Proxima Nova | Light / Regular |

Proxima Nova: elegante, cercana, legible en tamanos pequenos. Soporte completo latin + cirilico. Disponible en Adobe Fonts.

## Cara frontal (pagina 1)

Distribucion vertical (de arriba a abajo, dentro de margenes):

| Zona | Altura aprox. | Contenido |
|------|--------------|-----------|
| Franja superior | ~10 mm | Palabra + icono de campo semantico + estrellas |
| Imagen | ~58 mm | Ilustracion del personaje/concepto (rectangular, mas alta que ancha) |
| Franja inferior | ~14 mm | Frase de ejemplo |

### Frame de imagen en InDesign

- Ancho: 53 mm (57 mm de area util - 2 mm de margen interno a cada lado)
- Alto: 58 mm
- Posicion: centrado horizontalmente

### Imagen (Photoshop)

- Tamano: 53 x 58 mm (626 x 685 px a 300 ppp)
- Fondo purpura (#7B5EA7) incluido en la imagen
- Todas las imagenes deben tener el mismo tamano exacto para Data Merge

## Cara posterior (pagina 2)

### Seccion Combos

Combinaciones frecuentes de la palabra (chunks / patrones de construccion). Nombre visible en la tarjeta: Combos.

Ejemplo para "padre":
- mi/tu/su + padre
- el padre de + nombre
- es el padre de
- padre + madre = padres

Cada tarjeta incluye 4 combos relevantes para nivel A1.

## Produccion

### Data Merge (InDesign)

- Fuente de datos: CSV con columna @imagen para las ilustraciones
- Multiple Record Layout para colocar 8 tarjetas por hoja A4
- Lineas de corte incluidas en la exportacion PDF

### Preparacion de imagenes (Photoshop)

1. Todas las imagenes al mismo tamano: 626 x 685 px, 300 ppp
2. Fondo purpura (#7B5EA7)
3. Personaje centrado
4. Guardar como PNG
5. Nombre del archivo = palabra (padre.png, madre.png, etc.)
