# @memencionaste

[@memencionaste](https://twitter.com/memencionaste) es un bot de twitter que responde memes creados con inteligencia artificial a las cuentas que lo mencionen. Este bot puede crear memes de 10 plantillas predefinidas por medio de redes neuronales. En este repositorio encontrará los archivos y bases de datos usados para estimar el modelo, así como la arquitectura del bot.  

## Presentación

[![AI Meme Generator](https://img.youtube.com/vi/xT2BuXp1N7o/0.jpg)](https://www.youtube.com/watch?v=xT2BuXp1N7o)

[Presentación en pdf](imagenes/presentacion_memencionaste.pdf)


## Contenido del Git

1. [Data](data/): En esta carpeta encuentra las bases de memes originales y sus transformaciones.
2. [Notebooks](notebooks/): Aquí se encuentran los notebooks que se usaron para construir la red neuronal y crear el bot. También incluye un notebook con un análisis exploratorio de datos (EDA).



## Fases del proyecto

1. **Fuentes de información:**
  Usamos como fuente la base de datos recopilada por [memegenerator.es](https://www.memegenerator.es/). La base de datos de memegenerator se encuentra organizadas de acuerdo a plantillas por defecto y un número consecutivo que identifica el memes. De acuerdo con estas propiedades, se realizó un proceso de web-scrapping que nos permitió extraer desde la página web el identificador de la plantilla usada así como el texto de los memes. Después de un proceso de limpieza, se obtuvo una base de datos de 762.920 memes, distribuidos en 10 plantillas. 
  
2. **Modelamiento**
  El modelo seleccionado en esta etapa inicial es el [GTP2-Small](https://openai.com/blog/better-language-models/) refinado para español con base en wikipedia. El modelo se basa en Transformers y tiene como objetivo predecir la siguiente palabra condicionado a una cadena de texto previa. 

3. **Bot generador de memes**
  El generador de memes se encuentra en twitter bajo la cuenta [@memencionaste](https://twitter.com/memencionaste). La arquitectura del bot se basa en la integración del API de Twitter y Tweepy en Python y funciona bajo el siguiente flujo:
  
![flujo_unal_bot](/imagenes/flujo_unal_bot.jpg)


## Estado del proyecto

El proyecto se desarrolló bajo tres frentes. A continuación encontrará un listado de las actividades o hitos esperados dentro del proyecto y su estado al **02 de julio de 2021**:

### 1. Fuentes de información:
- [x] Definición de plantillas.
- [x] Extracción de base de memes.
- [x] Limpieza y separación de texto.

### 2. Modelo:
- [x] Investigación de modelos y estado del arte.
- [x] Preprocesamiento de la base de memes.
- [x] Entrenamiento del modelo.
- [x] Creación de flujo.

### 3. Producto
- [x] Creación del bot.
- [x] Generador de imágenes.
- [x] Conexión con el modelo.


