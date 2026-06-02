# Glosario — Día 1

## IA / LLM
- **LLM:** programa de IA que predice la siguiente palabra (token) según patrones aprendidos de enormes cantidades de texto. Como un practicante que leyó todo, pero inventa con seguridad y olvida entre tareas.
- **Token:** el pedazo mínimo de texto que el modelo procesa (≈ una palabra o parte de una). El modelo "piensa" en tokens, no en letras.
- **Ventana de contexto:** todo lo que el modelo puede "ver" en un momento (tu prompt + la conversación actual). Fuera de ahí, no recuerda nada.
- **Alucinación:** cuando el modelo produce algo que suena correcto pero es falso. Por eso nunca se confía un dato crítico sin verificar.
- **Temperatura:** perilla de aleatoriedad. Baja = respuestas consistentes; alta = más creativas y variadas.
- **Prompt:** la instrucción o texto de entrada que le das al modelo.
- **Modelo:** el "cerebro" entrenado que hace las predicciones (ej. Claude, GPT).
- **API:** la "puerta" por la que tu programa le habla a un modelo en la nube y recibe su respuesta.
- **Agente:** un LLM conectado a herramientas y a un bucle (razona → actúa → observa) para cumplir tareas, no solo responder. (El objetivo de tu año.)
- **Ingeniería de prompts:** el arte de escribir instrucciones para que el modelo haga lo que quieres de forma confiable.

## Python
- **Variable:** un nombre que guarda un valor (ej. `precio_kg = 29`).
- **Lista:** una colección ordenada de valores entre corchetes `[ ]` (ej. `[20, 21.5, 22]`).
- **Función:** un bloque de código que hace una tarea; algunas ya vienen con Python: `len()` cuenta, `sum()` suma, `print()` muestra.
- **Condicional (if/else):** hace que el programa decida: "si se cumple X, haz esto; si no, haz lo otro".
- **Indentación (sangría):** los espacios al inicio de una línea. En Python no son decoración: definen qué código pertenece a un bloque.
- **Operador:** símbolo que opera valores: `+ - * /` (aritmética), `>= > < ==` (comparación).
- **Comentario:** texto que empieza con `#`; notas para humanos que Python ignora.
- **Error / Traceback:** el reporte que da Python cuando algo falla. Se lee de abajo hacia arriba y dice qué y dónde. Es un mapa, no un regaño.

## Git / GitHub
- **Repositorio (repo):** la carpeta de tu proyecto que git rastrea, con todo su historial.
- **Git:** herramienta de control de versiones; guarda "fotos" (commits) de tu trabajo en el tiempo.
- **Commit:** una "foto" guardada de tu trabajo, con un mensaje que describe el cambio.
- **Push:** subir tus commits locales a la nube (GitHub).
- **README:** archivo que explica de qué trata tu repo; la cara de tu proyecto.
- **.gitignore:** lista de archivos que git debe ignorar (basura temporal que no quieres subir).
