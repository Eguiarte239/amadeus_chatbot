import nltk
from nltk.chat.util import Chat, reflections

# Configura las reglas de respuesta del chatbot
pairs = [

    (r'(.*)personajes principales(.*)',
    ['Los personajes principales de Steins;Gate son Rintarou Okabe, Kurisu Makise, Mayuri Shiina, Daru, y otros miembros del laboratorio.']),

    (r'(.*)(de qué trata|cuál es la trama)(.*)',
    ['La trama principal de Steins;Gate trata sobre un grupo de amigos quienes accidentalmente descubren la forma de alterar el pasado mediante emails pero con un alto precio a pagar.']),

    (r'(.*)cómo se llama el laboratorio(.*)',
    ['El nombre del laboratorio fundado por Okabe es "Laboratorio de Artefactos Futuristas".']),

    (r'(.*)quién es (Okabe|Rintaro|Okabe Rintaro|Hououin|Kyouma|Hououin Kyouma)(.*)',
    ['Okabe Rintaro, también conocido como el científico loco y destructor de mundos, Hououin Kyouma (Okarin para Mayuri) es el líder y miembro fundador del Laboratorio de Artefactos Futuristas en Steins;Gate.']),

    (r'(.*)quién es (Kurisu|Makise|Makise Kurisu|Kurisu Makise)(.*)',
    ['Kurisu Makise, también conocida como Kuristina, the zombie, tsundere, entre otros apodos, es la chica genio y cuarta miembro del laboratorio de Artefactos Futuristas quien hizo posible recrear el accidente del D-mail inicial y con ello crear la máquina de saltos en el tiempo.']),
    
    (r'(.*)quién es (Daru|Itaru|Hashida|Itaru Hashida)(.*)',
    ['Itaru Hashida o Daru, también llamado Supa hacka por Mayuri, es el segundo miembro del Laboratorio de Aparatos Futuristas y mejor amigo de Okabe. Es gracias a él que el grupo logra hackear a SERN y con ello descubrir los temibles actos que han cometido con el fin de viajar en el tiempo.']),

    (r'(.*)quién es (Mayuri|Mayurii|Shiina Mayuri)(.*)',
    ['Shiina Mayuri es la mejor amiga de Okabe y es la tercer miembro del Laboratorio de Aparatos Futuristas. A pesar de no ser una genio como Okabe, Daru o Kurisu ella fue una pieza clave para llegar a la Steins;Gate.']),

    (r'(.*)qué es la organización(.*)',
    ['La organización es, como dice su nombre, una organización ficticia creada por Kyouma, el alter ego de Okabe. Después se descubriría que dicha organización es real y es llamada el comité de los 300, personas tan poderosas que dominan el mundo desde las sombras.']),

    (r'Tuturu',
    ['Tuturu! Hi Okarin']),

    (r'(.*)qué es tuturu(.*)',
    ['Tuturu es una forma particular que tiene Mayuri para saludar a sus amigos']),

    (r'(.*)qué es la Dr.Pepper(.*)',
    ['¡Es la bebida de los elegidos!']),

    (r'(.*)cuántos saltos temporales dio Okabe(.*)',
    ['En el año 2036 Okabe realizó más de 3 mil saltos temporales con el único fin de volver al pasado y así evitar la tercera guerra mundial']),

    (r'(ya me cansé|ya no quiero ver|me aburrió) steins;gate',
    ['¡Es la organización controlando tu mente para que desistas de pelear!, te prometo que se pone bueno a partir del capítulo 6']),
    
    (r'space has a beginning',
    ['But it has no end. - infinite. Stars too have a beginning, but are by their own power destroyed - finite. history dictates that he who holds wisdom is the greatest fool. The fish in the sea know not the land. If they too hold wisdom, they woo will be destroyed. it is more ridiculous for man to exceed lightspeed, than for fish to live ashore. This could be called Gods final warning to those that still rebel.']),

    (r'(qué tiene de|por qué es) bueno steins;gate(.*)',
    ['Tuturu! Hi Okarin']),

    (r'(.*)Okabe muere(.*)',
    ['Tanto en el campo alfa como beta, Okabe morirá en el año 2025 ante ojos del mundo. No obstante, en el campo de atracción Beta, Okabe desaparece ante ojos del mundo para ir en busca de Suzuha y Mayuri a través del tiempo, una promesa que hizo con el fin de lograr detener la tercer guerra mundial y con ello darle la clave a su versión pasada para alcanzar la Steins;Gate']),

    (r'(.*)qué significa Steins;Gate(.*)',
    ['En palabras del propio Okabe este nombre no significa nada. No obstante, este es el nombre que recibe única línea temporal que asegura un mundo sin una distopía futura, esto después de la llamada entre el Okabe del futuro y del pasado']),

    (r'Hola|Hola!|Hey', ['¡Hola! ¿En qué puedo ayudarte hoy?']),
    (r'Adiós', ['¡Hasta luego! Si tienes más preguntas sobre Steins;Gate, no dudes en regresar.']),

    (r'(.*)', ['No tengo una respuesta para esto, ¡Debe ser obra de la organización!']),
]

# Crea un objeto Chatbot
chatbot = Chat(pairs, reflections)

# Función para iniciar el chat
def run_chatbot():
    print("¡Hola! Soy Amadeus 2.0. Puedes preguntarme sobre lo que necesites acerca de Steins;Gate.")
    print("Escribe 'Adiós' para salir del chat.")
    chatbot.converse(quit="Adiós")

if __name__ == "__main__":
    run_chatbot()