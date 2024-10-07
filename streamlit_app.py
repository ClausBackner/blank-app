import streamlit as st
from PIL import Image, ImageOps
import random
from datetime import datetime, timedelta
import pandas as pd


# Título de la aplicación
st.title('Procesamiento básico de imágenes')

# Subida de la imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

# Si se ha subido un archivo
if uploaded_file is not None:
    # Abrir la imagen
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen original
    st.image(image, caption='Imagen original', use_column_width=True)
    
    # Añadir un separador
    st.write("---")
    
    # Opción para convertir la imagen a escala de grises
    if st.checkbox('Convertir a escala de grises'):
        grayscale_image = ImageOps.grayscale(image)
        st.image(grayscale_image, caption='Imagen en escala de grises', use_column_width=True)

    # Opción para voltear horizontalmente la imagen
    if st.checkbox('Voltear horizontalmente'):
        flipped_image = ImageOps.mirror(image)
        st.image(flipped_image, caption='Imagen volteada horizontalmente', use_column_width=True)
else:
    st.write("Por favor, sube una imagen para comenzar.")

# Título del juego
st.title('🎮 Minijuego: Adivina el Número')

# Generar el número secreto de forma aleatoria (entre 1 y 100)
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# Inicializar la variable de intentos si no existe
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Instrucciones del juego
st.write('He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?')

# Entrada del usuario
guess = st.number_input('Introduce tu suposición:', min_value=1, max_value=100, step=1)

# Botón para hacer una suposición
if st.button('¡Adivinar!'):
    st.session_state.attempts += 1
    # Comprobar si el usuario adivinó el número
    if guess == st.session_state.secret_number:
        st.success(f'🎉 ¡Felicidades! Has adivinado el número {st.session_state.secret_number} en {st.session_state.attempts} intentos.')
        # Reiniciar el juego
        if st.button('Jugar de nuevo'):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
    elif guess < st.session_state.secret_number:
        st.warning('El número es más **alto**. ¡Inténtalo de nuevo!')
    else:
        st.warning('El número es más **bajo**. ¡Inténtalo de nuevo!')

# Mostrar el número de intentos actuales
st.write(f'Intentos realizados: {st.session_state.attempts}')

# Título de la aplicación
st.title('🧠 Quiz Interactivo')

# Lista de preguntas y respuestas
questions = {
    "¿Cuál es el planeta más cercano al sol?": {
        "options": ["Venus", "Tierra", "Mercurio", "Marte"],
        "answer": "Mercurio"
    },
    "¿Cuál es el idioma más hablado en el mundo?": {
        "options": ["Inglés", "Chino mandarín", "Español", "Hindú"],
        "answer": "Chino mandarín"
    },
    "¿Quién escribió 'Don Quijote de la Mancha'?": {
        "options": ["Miguel de Cervantes", "Gabriel García Márquez", "William Shakespeare", "J.K. Rowling"],
        "answer": "Miguel de Cervantes"
    },
    "¿Qué gas es necesario para que se produzca la fotosíntesis?": {
        "options": ["Nitrógeno", "Oxígeno", "Dióxido de carbono", "Hidrógeno"],
        "answer": "Dióxido de carbono"
    },
    "¿En qué año llegó el hombre a la luna?": {
        "options": ["1959", "1969", "1979", "1989"],
        "answer": "1969"
    }
}

# Inicializar la puntuación si aún no existe
if 'score' not in st.session_state:
    st.session_state.score = 0

# Inicializar la pregunta actual si aún no existe
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

# Obtener la pregunta actual
current_question = list(questions.keys())[st.session_state.current_question]
options = questions[current_question]["options"]
correct_answer = questions[current_question]["answer"]

# Mostrar la pregunta
st.write(f"Pregunta {st.session_state.current_question + 1}: {current_question}")

# Mostrar las opciones como botones de radio
user_answer = st.radio("Elige tu respuesta:", options)

# Botón para enviar la respuesta
if st.button("Enviar respuesta"):
    # Verificar si la respuesta es correcta
    if user_answer == correct_answer:
        st.success("¡Correcto!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrecto. La respuesta correcta es: {correct_answer}")

    # Avanzar a la siguiente pregunta
    if st.session_state.current_question < len(questions) - 1:
        st.session_state.current_question += 1
    else:
        st.write("---")
        st.write(f"**Quiz completado. Tu puntuación final es: {st.session_state.score}/{len(questions)}**")
        if st.button('Reiniciar Quiz'):
            st.session_state.current_question = 0
            st.session_state.score = 0
else:
    st.write("Envía tu respuesta para continuar.")

def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Acuario"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Piscis"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Tauro"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Géminis"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cáncer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Escorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagitario"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricornio"

# Título de la aplicación
st.title("🔮 Adivina tu Signo Zodiacal")

# Entrada de fecha de nacimiento
birth_date = st.date_input("Introduce tu fecha de nacimiento")

# Verificar si se ha introducido la fecha
if birth_date:
    # Obtener el día y el mes de la fecha de nacimiento
    day = birth_date.day
    month = birth_date.month

    # Determinar el signo zodiacal
    zodiac_sign = get_zodiac_sign(day, month)

    # Mostrar el resultado
    st.write(f"Tu signo zodiacal es: **{zodiac_sign}**")
else:
    st.write("Por favor, introduce tu fecha de nacimiento.")
# Título de la aplicación
st.title('📅 Agenda Personal')

# Definir el almacenamiento de eventos en el estado de la aplicación
if 'events' not in st.session_state:
    st.session_state.events = []

# Función para añadir un evento
def add_event(event_name, event_date, event_time):
    event_datetime = datetime.combine(event_date, event_time)
    st.session_state.events.append({"Evento": event_name, "Fecha y Hora": event_datetime})
    st.success(f'Evento "{event_name}" agregado para el {event_datetime.strftime("%d/%m/%Y a las %H:%M")}')

# Formulario para agregar un nuevo evento
st.subheader('Agregar un nuevo evento')

# Entrada para el nombre del evento
event_name = st.text_input('Nombre del evento')

# Entrada para la fecha del evento
event_date = st.date_input('Fecha del evento')

# Entrada para la hora del evento
event_time = st.time_input('Hora del evento')

# Botón para agregar el evento
if st.button('Agregar Evento'):
    if event_name:
        add_event(event_name, event_date, event_time)
    else:
        st.error('Por favor, introduce un nombre para el evento.')

# Mostrar los eventos programados
st.subheader('Eventos Programados')

# Si hay eventos, mostrar una tabla con el cronograma
if st.session_state.events:
    events_df = pd.DataFrame(st.session_state.events)
    events_df = events_df.sort_values(by="Fecha y Hora")  # Ordenar por fecha y hora
    st.table(events_df)
else:
    st.write("No tienes eventos programados. Agrega uno utilizando el formulario de arriba.")
