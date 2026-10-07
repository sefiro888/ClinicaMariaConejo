"""Contenido editorial de la web de Fisioterapia María Conejo.

Fuentes: textos facilitados por la clínica, publicaciones de Instagram (@fisiomariacm),
ficha de Google (5,0 · 38 opiniones) y directorios profesionales. Lo que no está
confirmado (precios, duración exacta de sesiones, zona de domicilio) se indica como
«consultar» y nunca se inventa.
"""

PHONE = "656 64 33 30"
PHONE_INTL = "34656643330"
ADDRESS = "C. Fuente Toril, 24"
CITY = "29312 Villanueva del Rosario, Málaga"
NICA = "65223"
RATING = "5,0"
REVIEWS_COUNT = 38

# Reels de Instagram (vídeos en assets/video). "video": False = solo enlace a Instagram.
REELS = {
    "tecnologia": {"title": "Fisioterapia avanzada con tecnología de vanguardia", "text": "Winback y ecografía integradas en nuestros tratamientos ⚡️", "url": "https://www.instagram.com/p/DTNgkfKjDf0/", "video": True, "tag": "Tecnología"},
    "familia": {"title": "Cuidamos de ti y de los tuyos 🤎", "text": "Fisioterapia, pediatría, ejercicio y FisioPilates: así es nuestro día a día en la clínica.", "url": "https://www.instagram.com/p/DQEh81hjNHT/", "video": True, "tag": "La clínica", "credit": "Vídeo: @fofilms.es"},
    "fisiopilates-clases": {"title": "Así son las clases de Fisio Pilates ✨", "text": "Movimiento consciente, fuerza y bienestar en cada sesión 💪 Adaptadas a tus necesidades, con supervisión profesional para que entrenes seguro y eficaz.", "url": "https://www.instagram.com/p/DNx2Fq42Dr0/", "video": True, "tag": "FisioPilates"},
    "pilates-naturaleza": {"title": "Respira, muévete, conecta 🍃", "text": "Pilates en su forma más natural: FisioPilates al aire libre.", "url": "https://www.instagram.com/p/DQUIMn4DHBD/", "video": False, "tag": "Al aire libre"},
}

# 0 = lunes … 6 = domingo. Tramos en horas decimales.
HOURS = [
    ("Lunes", [(11, 14), (15, 21)]),
    ("Martes", [(11, 14), (15, 21)]),
    ("Miércoles", [(11, 14), (15, 21)]),
    ("Jueves", [(11, 14), (15, 21)]),
    ("Viernes", [(11, 14), (15, 20)]),
    ("Sábado", []),
    ("Domingo", []),
]

ANNOUNCEMENTS = [
    ("star", "5,0 en Google · 38 opiniones de pacientes"),
    ("leaf", "FisioPilates al aire libre · grupos reducidos guiados por fisioterapeuta"),
    ("wave", "Ecografía musculoesquelética en consulta: ver para tratar mejor"),
    ("bolt", "Tecnología Winback: radiofrecuencia de alta, media y baja frecuencia"),
    ("gift", "Bonos de sesiones y tarjetas regalo · pregúntanos sin compromiso"),
    ("baby", "Fisioterapia pediátrica: cólico del lactante, plagiocefalia y desarrollo"),
    ("home", "Fisioterapia y podología a domicilio para movilidad reducida"),
    ("clock", "Lunes a jueves 11:00–14:00 y 15:00–21:00 · viernes hasta las 20:00"),
]

REVIEWS = [
    ("Laura Granados", "Hace 6 meses", "Una primera visita de 10. Te explica todo al detalle y sabe en cada momento exactamente qué necesitas. Cuenta con todo lo necesario para tratar cualquier lesión y ayudarte a mejorar (eco, punción, tratamiento de calor…). Además, te manda ejercicios para hacer en casa, explicándolos y comprobando cómo los haces para asegurarse de que los realizas correctamente. Se nota que se preocupa de verdad por sus pacientes."),
    ("Rosario Fernández", "Hace un año", "Estoy encantada con el trato y la profesionalidad de María Conejo. Desde la primera sesión me sentí en buenas manos: supo escucharme, valorar mi caso y aplicar el tratamiento adecuado. Gracias a ella he notado una gran mejoría y, lo más importante, me ha dado herramientas para prevenir futuras molestias. 100% recomendable, tanto por su experiencia como por su cercanía y empatía."),
    ("Maria Cozar", "Hace 6 meses", "Tanto mi pareja como yo hemos sido tratados por María por diferentes lesiones con resultados muy satisfactorios. Es una gran profesional y además cuenta con tecnología avanzada que ayuda mucho al diagnóstico y tratamiento. Te explica todo con claridad y te ayuda en el proceso de recuperación. Muy satisfecha con su trato y resultados."),
]

COLLABORATIONS = [
    ("U.D. Rosario", "Club de fútbol de Villanueva del Rosario, fundado en 1981."),
    ("C.D. Hondonero", "Club deportivo de montaña y carrera."),
    ("Sauce Capacita", "Entidad local con la que compartimos la pasión por la salud y el bienestar."),
]

POLICY = [
    ("Puntualidad", "Se ruega acudir a la cita con puntualidad. En caso de retraso, la sesión finalizará a la hora prevista para no perjudicar al siguiente paciente."),
    ("Cancelaciones y avisos", "Si no puedes asistir a tu cita programada, es obligatorio avisar con al menos 12 horas de antelación. De no hacerlo o no presentarse, se aplicará el recargo íntegro del importe de la sesión."),
    ("Ausencias repetidas", "Las faltas de asistencia reiteradas o el incumplimiento constante de las normas de aviso previo podrán suponer la suspensión del servicio."),
    ("Bonos y tarjetas regalo", "Tanto los bonos de sesiones como las tarjetas regalo tienen un plazo de validez de 1 año a partir de la fecha de su adquisición. Transcurrido este periodo sin haber sido utilizados, perderán su validez."),
]

AMENITIES = [
    ("access", "Acceso y aseo adaptados para silla de ruedas"),
    ("card", "Pago con tarjeta y con el móvil (NFC)"),
    ("car", "Aparcamiento gratuito en la calle"),
    ("heart", "Espacio seguro e inclusivo para todas las personas"),
]

EXERCISE_BENEFITS = [
    "Mejora la tolerancia al dolor",
    "Agiliza el proceso de recuperación",
    "Ayuda a una recuperación óptima y de calidad",
    "Evita que se agrave la lesión",
    "Mantiene e incrementa la movilidad y la fuerza",
    "Restablece la capacidad funcional del tejido afectado",
]

WINBACK_LEVELS = [
    ("Alta frecuencia", "Profundo", "Estimula los tejidos profundos y favorece la regeneración celular.", 92),
    ("Media frecuencia", "Medio", "Mejora la circulación y la oxigenación de la zona tratada.", 62),
    ("Baja frecuencia", "Superficial", "Efecto analgésico y antiinflamatorio desde la propia sesión.", 32),
]

TEAM = [
    {
        "name": "María Conejo Martín",
        "role": "Fisioterapeuta · Directora del centro",
        "image": "maria",
        "bio": [
            "Graduada en Fisioterapia, María ha continuado su formación con un Máster de Formación Permanente en Fisioterapia Manual e Invasiva para el Tratamiento del Dolor y de la Disfunción, impartido por la Universidad de Granada (UGR), lo que le permite abordar diversas patologías desde un enfoque integral y actualizado.",
            "Además, cuenta con especialización en fisioterapia pediátrica, atención temprana, neonatología y educación, desarrollada en Sevilla. Esta formación le ha permitido trabajar con los más pequeños desde sus primeros días de vida, acompañando a las familias en procesos tan importantes como el desarrollo motor, la estimulación temprana y la recuperación funcional.",
            "Su enfoque combina la ciencia, la técnica y la empatía, siempre priorizando el bienestar y la confianza del paciente. María cree firmemente en el poder del acompañamiento terapéutico, la educación en salud y la escucha activa como pilares fundamentales para una recuperación efectiva.",
        ],
        "milestones": [
            ("Grado", "Graduada en Fisioterapia"),
            ("Máster · UGR", "Fisioterapia Manual e Invasiva para el Tratamiento del Dolor y de la Disfunción"),
            ("Especialización · Sevilla", "Fisioterapia pediátrica, atención temprana, neonatología y educación"),
            ("Hoy", "Dirige su clínica de fisioterapia, nutrición y podología en Villanueva del Rosario"),
        ],
    },
    {
        "name": "Ana María Sancho",
        "role": "Nutricionista",
        "image": "",
        "bio": [
            "Graduada en Nutrición Humana y Dietética y con Máster Universitario en Nutrición Clínica, Ana María es la responsable del servicio de nutrición del centro.",
            "Acompaña a cada persona con planes de alimentación personalizados, educación nutricional y seguimiento continuo, tanto para objetivos de salud y peso como para rendimiento deportivo o condiciones como diabetes, hipertensión o colesterol.",
        ],
        "milestones": [
            ("Grado", "Nutrición Humana y Dietética"),
            ("Máster universitario", "Nutrición Clínica"),
        ],
    },
]

PILLARS = [
    ("Valoración completa", "Siempre empezamos analizando tu historial, tus hábitos y tus necesidades específicas. Solo así podemos diseñar un plan adaptado a ti."),
    ("Tecnología con sentido", "Ecógrafo de última generación y diatermia Winback: herramientas que aportan precisión, seguridad y seguimiento real de tu evolución."),
    ("Acompañamiento cercano", "Te explicamos cada paso, te enseñamos ejercicios para casa y comprobamos cómo los haces. Tu recuperación también es tuya."),
]

HOME_FAQS = [
    ("¿Necesito volante médico para pedir cita?", "No. Puedes reservar directamente por WhatsApp o por teléfono. Si tienes informes, pruebas de imagen o indicaciones de tu médico, tráelos a la primera visita: nos ayudan a entender mejor tu caso."),
    ("¿Cómo es la primera visita?", "Empieza con una valoración completa: conversamos sobre tu historia, tus hábitos y lo que te ocurre, exploramos cómo te mueves y, cuando aporta información, utilizamos la ecografía. Con todo ello te explicamos qué ocurre y diseñamos contigo un plan de tratamiento."),
    ("¿Qué ropa debo llevar?", "Ropa cómoda que permita moverte y acceder con facilidad a la zona a tratar. Para FisioPilates, ropa deportiva y calcetines; para el estudio de la pisada, el calzado que usas habitualmente."),
    ("¿Cuál es el horario de la clínica?", "De lunes a jueves de 11:00 a 14:00 y de 15:00 a 21:00, y los viernes de 11:00 a 14:00 y de 15:00 a 20:00. Sábados y domingos, cerrado. Se atiende con cita previa."),
    ("¿Tenéis bonos o tarjetas regalo?", "Sí. Hay bonos de sesiones de fisioterapia y tarjetas regalo, con una validez de 1 año desde su adquisición. Pregúntanos sin compromiso por las modalidades disponibles."),
    ("¿Qué pasa si no puedo acudir a mi cita?", "Avísanos con al menos 12 horas de antelación. Así otra persona que lo necesite podrá aprovechar ese hueco. Las ausencias sin aviso conllevan el cargo íntegro de la sesión."),
    ("¿Atendéis a domicilio?", "Sí, ofrecemos fisioterapia y podología a domicilio, pensadas especialmente para personas con movilidad reducida. Escríbenos con tu localidad y te confirmamos disponibilidad."),
    ("¿Cómo puedo pagar?", "Puedes pagar con tarjeta de crédito o débito y también con el móvil mediante pago sin contacto (NFC)."),
]

# Buscador «¿Qué te ocurre?»: etiqueta -> (texto, servicios recomendados)
FINDER = [
    ("Dolor de espalda o cuello", "Una valoración nos dirá de dónde viene el dolor. Solemos combinar terapia manual, ejercicio y, si está indicado, técnicas invasivas o diatermia.", ["fisioterapia-musculoesqueletica", "terapia-manual", "tecnicas-invasivas"]),
    ("Lesión deportiva", "Ecografía para ver el tejido, tratamiento preciso y una vuelta progresiva a tu deporte, apoyada en el ejercicio.", ["ecografia-musculoesqueletica", "ejercicio-terapeutico", "tecarterapia-diatermia"]),
    ("Después de una operación", "Acompañamos la recuperación tras cirugía ortopédica o traumatológica paso a paso, en clínica o a domicilio.", ["rehabilitacion-postquirurgica", "ejercicio-terapeutico", "fisioterapia-domicilio"]),
    ("Mi bebé o mi hijo", "Cólico del lactante, deformidades craneales, desarrollo motor y asesoramiento de lactancia con una fisioterapeuta formada en pediatría y neonatología.", ["fisioterapia-pediatrica"]),
    ("Quiero moverme mejor", "Postura, fuerza del core y prevención de lesiones con ejercicio guiado por fisioterapeuta, en grupos reducidos o sesiones individuales.", ["fisiopilates", "ejercicio-terapeutico"]),
    ("Quiero comer mejor", "Valoración nutricional completa, plan personalizado y seguimiento para salud, peso o deporte.", ["valoracion-nutricional", "planes-alimentacion", "educacion-nutricional"]),
    ("Tengo una enfermedad crónica", "Nutrición adaptada a diabetes, hipertensión, colesterol, enfermedades digestivas e intolerancias, siempre junto a tu equipo médico.", ["nutricion-clinica", "podologia-general"]),
    ("Me duelen los pies", "Estudio de la pisada, plantillas a medida, quiropodia y órtesis para caminar sin molestias.", ["estudio-pisada", "plantillas-personalizadas", "quiropodia"]),
]

CATEGORIES = {
    "fisioterapia": {
        "title": "Fisioterapia",
        "eyebrow": "Movimiento, recuperación y prevención",
        "lead": "Valoración individual, terapia manual, ejercicio y tecnología avanzada para aliviar el dolor y recuperar tu movilidad.",
        "image": "sesion",
        "hero": "hombro",
        "pro": "María Conejo Martín",
        "intro": [
            "En la clínica sabemos que la fisioterapia va más allá de tratar una zona que duele: se trata de comprender a fondo el estado de cada paciente y acompañarlo de manera cercana y segura durante todo el proceso.",
            "Por eso combinamos razonamiento clínico, terapia manual, ejercicio terapéutico, técnicas invasivas y tecnología como el ecógrafo y la diatermia Winback. Cada herramienta se elige tras la valoración, nunca por rutina.",
        ],
        "highlights": [
            ("Valoración con ecografía", "Vemos músculos, tendones y ligamentos en tiempo real para precisar el tratamiento."),
            ("Máster en fisioterapia invasiva", "Punción seca, electropunción y neuromodulación con formación de posgrado (UGR)."),
            ("Pediatría y neonatología", "Atención especializada para bebés y niños, acompañando a las familias."),
            ("Ejercicios para casa", "Te enseñamos y comprobamos cada ejercicio para que avances entre sesiones."),
        ],
        "faqs": [
            ("¿Cuántas sesiones voy a necesitar?", "Depende de tu caso, del tiempo de evolución y de tus objetivos. Tras la valoración te daremos una estimación orientativa y la revisaremos según cómo respondas."),
            ("¿La fisioterapia duele?", "Algunas técnicas pueden resultar algo molestas, pero siempre trabajamos dentro de lo que toleras y te explicamos qué vas a notar. El objetivo es que salgas mejor de lo que entraste."),
            ("¿Puedo venir si no sé qué me pasa?", "Sí. Precisamente para eso está la valoración inicial: entender qué ocurre y, si algo requiere estudio médico, orientarte para que lo consultes."),
            ("¿Combináis varias técnicas en una sesión?", "Sí, cuando tiene sentido. Una misma sesión puede incluir terapia manual, ejercicio y tecnología, siempre adaptado a tu valoración."),
        ],
    },
    "nutricion": {
        "title": "Nutrición",
        "eyebrow": "Tu bienestar empieza en el plato",
        "lead": "Evaluación completa, planes personalizados, educación alimentaria y seguimiento continuo con nuestra nutricionista.",
        "image": "interior",
        "hero": "pasillo",
        "pro": "Ana María Sancho",
        "intro": [
            "Tu bienestar comienza con una alimentación adecuada y personalizada. En la consulta nutricional no encontrarás dietas genéricas: partimos de una evaluación completa de tus hábitos, tu salud y tus objetivos.",
            "Con esa información diseñamos un plan que encaje en tu vida real —horarios, gustos, familia, entrenamiento— y te acompañamos con seguimiento continuo para ajustar lo que haga falta.",
        ],
        "highlights": [
            ("Nutricionista titulada", "Graduada en Nutrición Humana y Dietética con Máster en Nutrición Clínica."),
            ("Composición corporal", "Determinación del estado de salud mediante antropometría."),
            ("Condiciones especiales", "Diabetes, hipertensión, colesterol, enfermedades digestivas, cáncer e intolerancias."),
            ("Seguimiento continuo", "Revisiones para ajustar el plan y consolidar hábitos que duren."),
        ],
        "faqs": [
            ("¿Tengo que pesarme en cada consulta?", "No es obligatorio. Las mediciones se acuerdan contigo y se usan solo cuando aportan información útil para tus objetivos."),
            ("¿Voy a tener que comer cosas que no me gustan?", "No. El plan se construye a partir de tus preferencias, tu cultura alimentaria y tu día a día."),
            ("¿Sirve si no quiero perder peso?", "Por supuesto. La consulta también se orienta a salud, rendimiento deportivo, ganancia muscular o mejora de hábitos."),
            ("¿Cada cuánto son las revisiones?", "Se acuerdan en función de tu objetivo y de cómo avances. El acompañamiento continuo forma parte del servicio."),
        ],
    },
    "podologia": {
        "title": "Podología",
        "eyebrow": "Cuidado integral de tus pies",
        "lead": "Estudio de la pisada, plantillas personalizadas, quiropodia, órtesis y atención a domicilio para caminar sin molestias.",
        "image": "salas",
        "hero": "fachada",
        "pro": "Servicio de podología del centro",
        "intro": [
            "Tus pies sostienen todo tu cuerpo, y cualquier alteración en ellos puede repercutir en rodillas, caderas o espalda. Por eso el área de podología trabaja de forma coordinada con fisioterapia.",
            "Desde el cuidado habitual de piel y uñas hasta el análisis biomecánico de la marcha, atendemos las necesidades de cada pie con soluciones personalizadas, también a domicilio para quien no puede desplazarse.",
        ],
        "highlights": [
            ("Análisis biomecánico", "Estudio de la pisada y de la marcha para corregir problemas de postura."),
            ("Plantillas a medida", "Diseñadas a partir de tu estudio y adaptadas a tu calzado y actividad."),
            ("Pie diabético", "Prevención y cuidado especializado de pies con mayor riesgo."),
            ("A domicilio", "Atención en casa para personas con movilidad reducida o necesidades especiales."),
        ],
        "faqs": [
            ("¿Cada cuánto debería ir al podólogo?", "Depende de cada persona. Si tienes diabetes, problemas circulatorios o durezas recurrentes, las revisiones periódicas son especialmente recomendables."),
            ("¿Las plantillas son para siempre?", "Las plantillas se revisan con el tiempo: el pie, la actividad y el calzado cambian. Te indicaremos cuándo conviene revisarlas."),
            ("¿Qué calzado debo llevar?", "El que uses habitualmente y, si practicas deporte, también tus zapatillas. Nos ayuda a entender tu forma de caminar."),
            ("¿Tratáis uñas encarnadas?", "Sí, forma parte de la quiropodia, junto con durezas, callosidades y otras molestias habituales."),
        ],
    },
}


def service(**kw):
    kw.setdefault("note", "")
    kw.setdefault("place", "En clínica")
    kw.setdefault("tile", "")
    kw.setdefault("hero", kw["image"])
    kw.setdefault("reel", "")
    return kw


SERVICES = [
    # ───────────────────────── FISIOTERAPIA ─────────────────────────
    service(
        category="fisioterapia", slug="fisioterapia-musculoesqueletica", title="Fisioterapia musculoesquelética",
        short="Dolor, lesiones y movilidad", kicker="Dolor y movimiento", image="reel-tratamiento", hero="modelo", reel="tecnologia",
        lead="Alivio del dolor, recuperación de lesiones y mejora de la movilidad con un plan construido a partir de tu valoración.",
        intro=[
            "La fisioterapia musculoesquelética se ocupa de músculos, articulaciones, tendones y ligamentos: es el tratamiento de referencia para dolores de espalda y cuello, esguinces, tendinopatías, contracturas o rigidez tras una lesión.",
            "En la clínica no aplicamos protocolos de serie. Escuchamos tu historia, valoramos cómo te mueves —con ayuda de la ecografía cuando aporta información— y elegimos contigo la combinación de terapia manual, ejercicio y tecnología que tiene sentido para tu caso.",
        ],
        facts=[("Primera visita", "Valoración completa"), ("Técnicas", "Manual · ejercicio · tecnología"), ("Profesional", "María Conejo")],
        benefits=[("Menos dolor", "Trabajamos sobre la causa del dolor, no solo sobre el síntoma."), ("Más movilidad", "Recuperas rango de movimiento y confianza al moverte."), ("Comprendes tu lesión", "Te explicamos qué ocurre y por qué hacemos cada cosa."), ("Prevención", "Te llevas herramientas para evitar recaídas.")],
        audience=["Dolor de espalda, cuello u hombro", "Esguinces, contracturas y sobrecargas", "Tendinopatías (codo, rodilla, Aquiles…)", "Rigidez o pérdida de movilidad", "Dolor que se repite o se ha vuelto crónico", "Molestias relacionadas con el trabajo o la postura"],
        process=[("Escuchamos", "Tu historia, cuándo empezó, qué lo empeora y qué lo alivia."), ("Valoramos", "Exploración física y, si procede, ecografía musculoesquelética."), ("Tratamos", "Terapia manual, ejercicio, electroterapia o Winback según tu caso."), ("Avanzamos", "Ejercicios para casa y revisión de la evolución en cada sesión.")],
        prepare=["Ropa cómoda que permita acceder a la zona", "Informes o pruebas de imagen si los tienes", "Una lista de la medicación que tomas", "Tus dudas: apúntalas para no olvidarlas"],
        faqs=[
            ("¿Hay una valoración antes de empezar?", "Sí. Cada tratamiento comienza con una valoración completa y personalizada de tu historial, tus hábitos y tus necesidades."),
            ("¿Siempre se utilizan las mismas técnicas?", "No. La elección depende de la valoración y de tus objetivos: terapia manual, ejercicio terapéutico, electroterapia, reeducación o tecnología cuando aporta valor."),
            ("¿Recibiré ejercicios para casa?", "Sí, cuando son adecuados para tu caso. Te los explicamos y comprobamos cómo los haces para asegurarnos de que los realizas correctamente."),
            ("¿Cuántas sesiones necesitaré?", "Depende de la lesión y de cómo evoluciones. Te daremos una estimación orientativa tras la valoración y la ajustaremos contigo."),
            ("¿Puedo venir con dolor agudo?", "Sí. En fase aguda adaptamos el tratamiento para aliviar sin irritar más la zona. Si detectamos algo que deba valorar un médico, te lo indicaremos."),
            ("¿Necesito una prueba de imagen previa?", "No es imprescindible. Si la tienes, tráela. Además, la ecografía en consulta nos permite observar muchas estructuras en el momento."),
        ],
    ),
    service(
        category="fisioterapia", slug="terapia-manual", title="Terapia manual",
        short="Técnicas manuales con objetivo clínico", kicker="Manos que tratan", image="reel-manual", hero="manual", reel="tecnologia",
        lead="Técnicas manuales avanzadas para mejorar la movilidad, aliviar el dolor y preparar el cuerpo para moverse mejor.",
        intro=[
            "La terapia manual reúne técnicas aplicadas con las manos —movilizaciones articulares, técnicas sobre tejido blando, estiramientos asistidos o técnicas neuromusculares— con un objetivo clínico concreto.",
            "No es un masaje genérico: se aplica tras valorar la zona y el movimiento, y casi siempre se combina con ejercicio para que la mejora se mantenga en el tiempo.",
        ],
        facts=[("Enfoque", "Individual"), ("Se combina con", "Ejercicio terapéutico"), ("Profesional", "María Conejo")],
        benefits=[("Alivio del dolor", "Modula la sensibilidad de los tejidos y reduce la tensión."), ("Movilidad articular", "Recupera recorrido en articulaciones rígidas."), ("Tejidos más libres", "Mejora la calidad del tejido muscular y fascial."), ("Prepara al movimiento", "Facilita que el ejercicio sea más cómodo y eficaz.")],
        audience=["Contracturas y tensión muscular", "Rigidez articular (cuello, hombro, espalda…)", "Dolor tras sobreesfuerzos", "Cefaleas de origen cervical", "Recuperación tras lesiones", "Personas que necesitan aliviar antes de poder ejercitarse"],
        process=[("Valoración", "Exploramos la zona, la movilidad y la respuesta al dolor."), ("Técnica", "Aplicamos las técnicas manuales indicadas para tu caso."), ("Integración", "Las combinamos con ejercicio y pautas para el día a día."), ("Revisión", "Comprobamos los cambios y ajustamos la siguiente sesión.")],
        prepare=["Ropa cómoda y fácil de retirar en la zona", "Evita comidas copiosas justo antes", "Cuéntanos si tomas anticoagulantes", "Avísanos de cualquier cirugía previa"],
        faqs=[
            ("¿Es solo un masaje?", "No. La terapia manual se utiliza con un objetivo clínico y se integra en una valoración y un plan individual."),
            ("¿Puede combinarse con ejercicio?", "Sí, y es lo recomendable. La terapia manual y el ejercicio terapéutico son recursos complementarios."),
            ("¿Duele?", "Algunas técnicas pueden ser intensas, pero siempre respetamos tu tolerancia y te avisamos antes."),
            ("¿Cuántas sesiones necesitaré?", "Depende de la valoración y de cómo evoluciones; se revisa contigo durante el proceso."),
            ("¿Es normal notar molestias después?", "Puede aparecer una ligera sensación de agujetas durante 24–48 horas. Si te preocupa algo, escríbenos."),
            ("¿Sirve para la cefalea?", "Las cefaleas de origen cervical pueden mejorar con terapia manual y ejercicio. Lo valoraremos en consulta."),
        ],
    ),
    service(
        category="fisioterapia", slug="ejercicio-terapeutico", title="Ejercicio terapéutico",
        short="Recuperación activa y personalizada", kicker="Recuperación activa", image="bandas", reel="fisiopilates-clases",
        lead="El movimiento como medicina: ejercicios adaptados para recuperar fuerza, movilidad y función tras una lesión.",
        intro=[
            "El ejercicio terapéutico es una de las herramientas con más respaldo científico en fisioterapia. Mejora la tolerancia al dolor, agiliza la recuperación y restablece la capacidad funcional del tejido afectado.",
            "Diseñamos cada programa según tu punto de partida y tus objetivos, te enseñamos a hacerlo bien y lo vamos progresando para que cada semana sumes un poco más.",
        ],
        facts=[("Modalidad", "En clínica y en casa"), ("Progresión", "Personalizada"), ("Profesional", "María Conejo")],
        benefits=[("Tolerancia al dolor", "El cuerpo se adapta y el dolor deja de mandar."), ("Fuerza y movilidad", "Mantiene e incrementa lo que la lesión quitó."), ("Recuperación de calidad", "Tejidos más fuertes y preparados."), ("Evita recaídas", "Reduce el riesgo de que la lesión se agrave o vuelva.")],
        audience=["Recuperación de una lesión o cirugía", "Pérdida de fuerza o movilidad", "Dolor persistente de espalda o articulaciones", "Deportistas que vuelven a entrenar", "Personas mayores que quieren ganar autonomía", "Quien quiere aprender a moverse con confianza"],
        process=[("Punto de partida", "Valoramos fuerza, movilidad y control."), ("Selección", "Elegimos ejercicios y dosis adecuadas para ti."), ("Técnica", "Corregimos la ejecución en la propia sesión."), ("Progresión", "Ajustamos carga y dificultad según evolucionas.")],
        prepare=["Ropa deportiva y calzado cómodo", "Una botella de agua", "Si tienes material en casa, cuéntanoslo", "Un móvil para grabar tus ejercicios, si quieres"],
        faqs=[
            ("¿Tengo que estar en forma para empezar?", "No. La propuesta se adapta al punto de partida de cada persona."),
            ("¿Podré practicar en casa?", "Sí. Te enseñamos los ejercicios y comprobamos cómo los haces para que puedas repetirlos con seguridad."),
            ("¿Necesito material?", "Normalmente basta con lo que tengas en casa; si hace falta algo sencillo, como una banda elástica, te lo indicaremos."),
            ("¿Se combina con otras técnicas?", "Sí. Puede formar parte de un plan que incluya terapia manual, diatermia u otras herramientas."),
            ("¿Y si un ejercicio me duele?", "Cuéntanoslo. Un poco de molestia controlada puede ser aceptable, pero ajustaremos siempre la dosis contigo."),
            ("¿Cuánto tiempo al día tendré que dedicar?", "Buscamos rutinas realistas, que encajen en tu día. Mejor poco y constante que mucho y esporádico."),
        ],
    ),
    service(
        category="fisioterapia", slug="fisiopilates", title="FisioPilates",
        short="Pilates clínico guiado por fisioterapeuta", kicker="Movimiento con propósito", image="pilates", reel="fisiopilates-clases",
        lead="Lo mejor del Pilates clínico y la fisioterapia para mejorar tu postura, fortalecer tu core y prevenir lesiones.",
        intro=[
            "En nuestro centro no solo ofrecemos clases de Pilates: ofrecemos un enfoque terapéutico y personalizado que prioriza tu salud, tu bienestar y tu progreso real. Cada sesión está guiada por una fisioterapeuta titulada que adapta los ejercicios a tu estado físico, tus lesiones y tus objetivos.",
            "Trabajamos en grupos reducidos o en sesiones individuales, garantizando una práctica segura, controlada y basada en criterios clínicos. Y sí: también nos reímos, disfrutamos y celebramos cada avance contigo.",
        ],
        facts=[("Formato", "Grupo reducido o individual"), ("Guiado por", "Fisioterapeuta titulada"), ("También", "Sesiones al aire libre")],
        benefits=[("Atención 100% personalizada", "Nada de rutinas genéricas: tú eres el centro."), ("Método seguro y eficaz", "Ideal con patologías, dolor crónico o en rehabilitación."), ("Técnicas actualizadas", "Pilates integrado con fisioterapia y movimiento funcional."), ("Resultados reales", "Progresos medibles: menos molestias, más fuerza y confianza.")],
        audience=["Quien quiere mejorar su postura", "Dolor de espalda crónico o recurrente", "Personas en rehabilitación o tras una lesión", "Embarazo y posparto, previa valoración", "Personas mayores que buscan equilibrio y fuerza", "Quien prefiere moverse en grupo reducido"],
        process=[("Valoración", "Partimos de tu estado físico, antecedentes y objetivos."), ("Adaptación", "Una fisioterapeuta ajusta cada ejercicio a ti."), ("Trabajo", "Control, fuerza del core, movilidad y respiración."), ("Progreso", "Revisamos tu evolución y subimos de nivel contigo.")],
        prepare=["Ropa deportiva cómoda", "Calcetines (mejor antideslizantes)", "Una botella de agua", "Cuéntanos cualquier lesión o embarazo"],
        faqs=[
            ("¿Las clases son individuales o en grupo?", "Ofrecemos sesiones individuales y grupos reducidos, para que la fisioterapeuta pueda atender a cada persona."),
            ("¿Puedo asistir si tengo una lesión?", "Sí, previa valoración. Se adapta el ejercicio a tus necesidades y limitaciones."),
            ("¿Es igual que una clase de Pilates en un gimnasio?", "No. Aquí el movimiento está guiado por una fisioterapeuta y tiene un enfoque terapéutico individualizado."),
            ("¿Hacéis FisioPilates al aire libre?", "Sí, organizamos sesiones al aire libre en grupo reducido, en contacto con la naturaleza. Pregúntanos por las próximas fechas."),
            ("¿Nunca he hecho Pilates, puedo empezar?", "Claro. Empezamos desde lo básico: respiración, control y postura, y avanzamos a tu ritmo."),
            ("¿Cómo reservo plaza?", "Escríbenos por WhatsApp: te informamos de horarios, plazas disponibles y modalidades."),
        ],
        note="Muévete, respira y reconecta contigo: también organizamos FisioPilates al aire libre, en grupo reducido, adaptado a cada persona y guiado por fisioterapeuta.",
    ),
    service(
        category="fisioterapia", slug="tecnicas-invasivas", title="Fisioterapia invasiva",
        short="Punción seca, electropunción y neuromodulación", kicker="Tratamiento preciso", image="reel-eco-pantalla", hero="consulta", reel="tecnologia",
        lead="Punción seca, electropunción y neuromodulación percutánea para tratar el dolor de manera efectiva y precisa.",
        intro=[
            "La fisioterapia invasiva utiliza agujas muy finas para actuar directamente sobre el tejido que causa el problema. María cuenta con un Máster en Fisioterapia Manual e Invasiva para el Tratamiento del Dolor y de la Disfunción por la Universidad de Granada.",
            "Con el apoyo de la ecografía, estas técnicas ganan en precisión y seguridad: podemos ver la estructura en tiempo real y dirigir el tratamiento exactamente donde se necesita.",
        ],
        facts=[("Técnicas", "Punción · EPI · NMP"), ("Guiado", "Con ecografía cuando procede"), ("Formación", "Máster UGR")],
        benefits=[("Directo al origen", "Actúa sobre puntos gatillo y tejidos concretos."), ("Alivio rápido", "Muchas personas notan mejoría en pocas sesiones."), ("Más precisión", "La ecografía permite guiar la aguja con seguridad."), ("Complementa", "Se integra con ejercicio y terapia manual.")],
        audience=["Puntos gatillo y dolor miofascial", "Tendinopatías persistentes", "Dolor de espalda o cuello que no mejora", "Cefaleas tensionales", "Dolor neuropático, previa valoración", "Deportistas con sobrecargas recurrentes"],
        process=[("Valoración", "Comprobamos si la técnica está indicada para ti."), ("Explicación", "Te contamos qué vas a notar y resolvemos tus dudas."), ("Aplicación", "Técnica estéril, guiada por ecografía cuando aporta valor."), ("Seguimiento", "Combinamos con ejercicio y revisamos la respuesta.")],
        prepare=["Come algo ligero antes de la sesión", "Avísanos si te dan miedo las agujas", "Indícanos si tomas anticoagulantes", "Cuéntanos si estás embarazada"],
        faqs=[
            ("¿Todas las personas necesitan punción seca?", "No. Es una de las opciones disponibles y solo se plantea tras la valoración individual."),
            ("¿Duele la punción seca?", "Se nota un pinchazo y, a veces, una contracción breve del músculo. Después puede quedar sensación de agujetas uno o dos días."),
            ("¿Qué es la electropunción?", "Es la aplicación de una corriente eléctrica a través de la aguja para potenciar el efecto sobre el tejido o el dolor."),
            ("¿Y la neuromodulación percutánea?", "Consiste en estimular un nervio con una aguja y corriente de baja intensidad para modular el dolor y la función muscular."),
            ("¿Por qué usar ecografía?", "Porque permite ver en tiempo real la estructura a tratar, mejorando la precisión de la punción seca y las infiltraciones."),
            ("¿Hay contraindicaciones?", "Sí, como el miedo intenso a las agujas, algunas alteraciones de la coagulación o ciertas zonas en el embarazo. Por eso siempre valoramos antes."),
        ],
    ),
    service(
        category="fisioterapia", slug="fisioterapia-pediatrica", title="Fisioterapia pediátrica",
        short="Bebés, niños y familias", kicker="Acompañamos cada etapa", image="reel-bebe", hero="recepcionista", reel="familia",
        lead="Tratamiento especializado para mejorar el desarrollo motor y cuidar a los más pequeños desde sus primeros días de vida.",
        intro=[
            "María cuenta con especialización en fisioterapia pediátrica, atención temprana, neonatología y educación. Esta formación le permite trabajar con los más pequeños desde sus primeros días de vida.",
            "Acompañamos a las familias en procesos tan importantes como el desarrollo motor, la estimulación temprana y la recuperación funcional, siempre en un ambiente tranquilo, cercano y respetuoso con los ritmos del bebé.",
        ],
        facts=[("Desde", "Los primeros días de vida"), ("Incluye", "Asesoramiento a la familia"), ("Profesional", "María Conejo")],
        benefits=[("Desarrollo motor", "Estimulamos cada etapa: control de cabeza, volteo, gateo, marcha."), ("Familias acompañadas", "Os enseñamos pautas para el día a día en casa."), ("Detección temprana", "Valoración y prevención para actuar a tiempo."), ("Trato cercano", "Sesiones adaptadas al ritmo y al juego del niño.")],
        audience=["Cólico del lactante", "Deformidades craneales (plagiocefalia, braquicefalia)", "Tortícolis del lactante", "Trastornos del desarrollo motor", "Patologías pediátricas musculoesqueléticas", "Asesoramiento y valoración de la lactancia materna"],
        process=[("Escuchamos", "A la familia: embarazo, parto, rutinas y preocupaciones."), ("Valoramos", "Al bebé o al niño según su etapa de desarrollo."), ("Tratamos", "Técnicas suaves, estimulación y juego dirigido."), ("Enseñamos", "Pautas de posicionamiento, porteo y estimulación en casa.")],
        prepare=["Ropa cómoda para el bebé o el niño", "Un pañal de repuesto y su juguete favorito", "Informes pediátricos si los hay", "Ven en un momento en que el bebé esté tranquilo"],
        faqs=[
            ("¿Desde qué edad se puede acudir?", "Desde los primeros días de vida. La formación de María en neonatología está orientada precisamente a los más pequeños."),
            ("¿Cómo ayuda la fisioterapia con el cólico del lactante?", "Con técnicas manuales suaves y pautas para la familia que pueden aliviar las molestias digestivas y favorecer el descanso."),
            ("Mi bebé tiene la cabeza aplanada, ¿qué hago?", "Las deformidades craneales posicionales responden mejor cuanto antes se actúa. Pide una valoración y te orientaremos."),
            ("¿Ofrecéis asesoramiento de lactancia?", "Sí. Incluimos asesoramiento y valoración de la lactancia materna dentro de la atención pediátrica."),
            ("¿También hacéis prevención?", "Sí. Una valoración pediátrica preventiva ayuda a seguir el desarrollo y resolver dudas de la familia."),
            ("¿Los padres están presentes en la sesión?", "Sí, siempre. La familia forma parte del tratamiento y aprende pautas para casa."),
        ],
    ),
    service(
        category="fisioterapia", slug="rehabilitacion-postquirurgica", title="Rehabilitación postquirúrgica",
        short="Recuperación tras cirugía", kicker="Volver paso a paso", image="reel-electro", hero="tratamiento", reel="tecnologia",
        lead="Acompañamiento en la recuperación tras cirugías ortopédicas o traumatológicas, con objetivos claros en cada fase.",
        intro=[
            "Después de una operación, la rehabilitación marca la diferencia en cómo y cuándo recuperas tu vida normal. Respetamos los tiempos de cicatrización y las indicaciones de tu cirujano, y trabajamos para recuperar movilidad, fuerza y función.",
            "Cada fase tiene sus objetivos: controlar el dolor y la inflamación, recuperar el movimiento, ganar fuerza y volver a tus actividades. Te acompañamos en todas.",
        ],
        facts=[("Modalidad", "En clínica o a domicilio"), ("Coordinado con", "Indicaciones médicas"), ("Profesional", "María Conejo")],
        benefits=[("Recuperación guiada", "Sabes qué toca en cada fase y por qué."), ("Menos rigidez", "Movilizamos a tiempo para evitar limitaciones."), ("Fuerza funcional", "Recuperas la capacidad para tu día a día."), ("Vuelta segura", "Progresión controlada hacia el trabajo o el deporte.")],
        audience=["Prótesis de rodilla o cadera", "Cirugía de ligamento cruzado o menisco", "Fracturas operadas", "Cirugía de hombro (manguito rotador, luxaciones)", "Cirugía de columna, según indicación médica", "Cirugía de mano, tobillo o pie"],
        process=[("Revisión", "Leemos tu informe quirúrgico y las indicaciones recibidas."), ("Fase inicial", "Control del dolor, inflamación y primeras movilizaciones."), ("Fase de fuerza", "Ejercicio terapéutico progresivo."), ("Vuelta a la actividad", "Trabajo funcional hasta recuperar tus objetivos.")],
        prepare=["Informe quirúrgico y pautas del hospital", "Ropa amplia que permita acceder a la zona", "Muletas u órtesis si las usas", "Lista de medicación actual"],
        faqs=[
            ("¿Cuándo puedo empezar?", "Depende de la cirugía y de las indicaciones de tu equipo médico. Consúltanos con tu informe y te orientamos."),
            ("¿El tratamiento incluye ejercicio?", "Sí. El ejercicio terapéutico es central en la recuperación, adaptado a cada fase."),
            ("¿Se puede realizar a domicilio?", "Sí, sobre todo en las primeras semanas, cuando desplazarse es difícil. Consulta disponibilidad para tu localidad."),
            ("¿Cuánto dura la rehabilitación?", "Varía mucho según la intervención. Te daremos una previsión orientativa al conocer tu caso."),
            ("¿Qué hago con la cicatriz?", "Te enseñaremos cómo cuidarla y, cuando esté cerrada, técnicas para mejorar su movilidad."),
            ("¿Os coordináis con el traumatólogo?", "Seguimos sus indicaciones y, si lo necesitas, te preparamos información sobre tu evolución para tus revisiones."),
        ],
    ),
    service(
        category="fisioterapia", slug="ecografia-musculoesqueletica", title="Ecografía musculoesquelética",
        short="Ver para tratar mejor", kicker="Ver más allá de los síntomas", image="ecografia", reel="tecnologia",
        lead="Imágenes en tiempo real de músculos, tendones y ligamentos para valorar mejor, personalizar el tratamiento y seguir tu evolución.",
        intro=[
            "Contamos con un ecógrafo de última generación, una herramienta que aporta imágenes claras y detalladas del sistema musculoesquelético. Esto nos permite observar estructuras como músculos, tendones y ligamentos, valorar mejor tu estado, personalizar el tratamiento y hacer un seguimiento más preciso de tu evolución.",
            "Su incorporación supone un gran avance: ofrece mayor seguridad durante las sesiones, optimiza los resultados y te ayuda a sentirte confiado en todo momento, porque puedes ver con tus propios ojos qué ocurre.",
        ],
        facts=[("Radiación", "Ninguna"), ("Sensación", "Indolora"), ("Uso", "Valoración y seguimiento")],
        benefits=[("Visualización en tiempo real", "Músculos, tendones y articulaciones en movimiento."), ("Más precisión", "En técnicas como punción seca e infiltraciones."), ("Seguimiento detallado", "Comparamos la imagen a lo largo de tu recuperación."), ("Segura e indolora", "Sin radiación, apta para casi todas las personas.")],
        audience=["Lesiones musculares (roturas fibrilares, contusiones)", "Tendinopatías de hombro, codo, rodilla o tobillo", "Esguinces y lesiones de ligamentos", "Seguimiento de la evolución de una lesión", "Apoyo a la fisioterapia invasiva", "Deportistas que quieren conocer el estado de un tejido"],
        process=[("Contexto", "Relacionamos la imagen con tu historia y la exploración."), ("Exploración", "Gel, sonda y pantalla: lo vemos juntos."), ("Decisión", "Usamos la imagen para orientar el tratamiento."), ("Seguimiento", "Repetimos cuando procede para medir los cambios.")],
        prepare=["Ropa que permita descubrir la zona", "Informes o pruebas previas", "No necesitas preparación especial", "Tus preguntas: te explicamos lo que vemos"],
        faqs=[
            ("¿La ecografía usa radiación?", "No. Utiliza ultrasonidos y no emite radiación ionizante; es segura e indolora."),
            ("¿Sustituye a la valoración clínica?", "No. Es una herramienta que complementa la historia y la exploración del paciente."),
            ("¿Es un diagnóstico médico?", "La ecografía en fisioterapia se utiliza para valorar y guiar el tratamiento fisioterapéutico. Si observamos algo que requiera estudio médico, te lo indicaremos."),
            ("¿Se utiliza con técnicas invasivas?", "Sí. Mejora la precisión en técnicas como la punción seca y las infiltraciones."),
            ("¿Puedo ver la imagen?", "Claro. Te explicamos lo que vemos en la pantalla para que entiendas tu lesión."),
            ("¿Tiene un coste adicional?", "Consulta las condiciones actuales al reservar; te informaremos sin compromiso."),
        ],
    ),
    service(
        category="fisioterapia", slug="tecarterapia-diatermia", title="Tecarterapia y diatermia Winback",
        short="Radiofrecuencia de alta, media y baja frecuencia", kicker="Terapia inteligente, resultados reales", image="winback", reel="tecnologia",
        lead="Tecnología de radiofrecuencia que actúa a nivel superficial, medio y profundo para acelerar la recuperación muscular y articular.",
        intro=[
            "La diatermia Winback es una tecnología de radiofrecuencia única que combina alta, media y baja frecuencia para actuar a distintos niveles del cuerpo: superficial, medio y profundo. Esto permite un tratamiento personalizado, potente y no invasivo.",
            "Su energía trabaja desde el interior del tejido, favoreciendo la circulación, la regeneración y la reducción del dolor. Y es compatible con técnicas manuales y ejercicios activos, por lo que se integra perfectamente en tu sesión.",
        ],
        facts=[("Tecnología", "Winback"), ("Tipo", "No invasiva"), ("Compatible con", "Terapia manual y ejercicio")],
        benefits=[("Alivio del dolor", "Desde las primeras sesiones."), ("Menos inflamación", "Efecto antiinflamatorio y analgésico."), ("Recuperación más rápida", "En lesiones musculares, tendinosas y articulares."), ("Mejor circulación", "Sanguínea y linfática, y mejor movilidad.")],
        audience=["Lesiones musculares y tendinosas", "Dolor articular (rodilla, hombro, columna)", "Contracturas y sobrecargas", "Procesos postquirúrgicos, según indicación", "Recuperación deportiva", "Personas que buscan una opción no invasiva"],
        process=[("Valoración", "Comprobamos si la diatermia está indicada."), ("Selección", "Elegimos el nivel: superficial, medio o profundo."), ("Aplicación", "Sola o combinada con técnicas manuales y movimiento."), ("Integración", "Ejercicio activo para consolidar los resultados.")],
        prepare=["Retira objetos metálicos de la zona", "Avísanos si llevas marcapasos o implantes", "Indícanos si estás embarazada", "Hidrátate bien antes y después"],
        faqs=[
            ("¿Qué siento durante la sesión?", "Un calor agradable y profundo en la zona tratada. Es un tratamiento cómodo y no invasivo."),
            ("¿Cómo actúa cada frecuencia?", "La alta estimula tejidos profundos y la regeneración celular; la media mejora la circulación y oxigenación; la baja tiene efecto analgésico y antiinflamatorio inmediato."),
            ("¿Se utiliza en todas las sesiones?", "No. La elección de herramientas depende de la valoración y del plan individual."),
            ("¿Sustituye al ejercicio?", "No. Es compatible con técnicas manuales y ejercicios activos, y funciona mejor combinada."),
            ("¿Hay contraindicaciones?", "Sí: marcapasos, embarazo, algunos implantes o procesos oncológicos activos, entre otros. Por eso siempre valoramos antes."),
            ("¿En cuántas sesiones se notan resultados?", "Muchas personas notan alivio desde las primeras sesiones, aunque depende de cada caso."),
        ],
    ),
    service(
        category="fisioterapia", slug="fisioterapia-domicilio", title="Fisioterapia a domicilio",
        short="Tratamiento en tu casa", kicker="Cuidado donde lo necesitas", image="bolsa", place="A domicilio", reel="familia",
        lead="Atención fisioterapéutica en tu hogar para quienes no pueden desplazarse o necesitan recuperarse en casa.",
        intro=[
            "Hay momentos en los que venir a la clínica no es posible: tras una cirugía, en personas mayores o con movilidad reducida, o durante una convalecencia. Para esos casos, llevamos la fisioterapia a tu casa.",
            "Además del tratamiento, adaptamos los ejercicios a tu entorno real —tu escalera, tu sillón, tu pasillo— y orientamos a la familia o cuidadores para que el día a día sea más seguro.",
        ],
        facts=[("Modalidad", "En tu domicilio"), ("Ideal para", "Movilidad reducida"), ("Cobertura", "Consultar localidad")],
        benefits=[("Comodidad", "Sin desplazamientos ni esperas."), ("Entorno real", "Ejercicios adaptados a tu casa."), ("Familia implicada", "Pautas para cuidadores."), ("Continuidad", "Evita interrumpir la recuperación.")],
        audience=["Personas mayores o con movilidad reducida", "Primeras semanas tras una cirugía", "Convalecencias y periodos de reposo", "Pacientes neurológicos, previa valoración", "Prevención de caídas", "Familias que cuidan a un ser querido"],
        process=[("Contacto", "Cuéntanos por WhatsApp la situación y tu localidad."), ("Confirmación", "Confirmamos cobertura y disponibilidad."), ("Valoración", "Primera visita en casa para conocer el caso y el entorno."), ("Plan", "Sesiones y pautas adaptadas a tu contexto.")],
        prepare=["Un espacio despejado para trabajar", "Informes médicos recientes", "Ropa cómoda", "Si es posible, que esté presente un familiar"],
        faqs=[
            ("¿Qué localidades cubre el servicio?", "Atendemos Villanueva del Rosario y alrededores. Escríbenos con tu localidad y te confirmamos disponibilidad."),
            ("¿Se pueden hacer ejercicios en casa?", "Sí. La fisioterapeuta adapta la sesión y los ejercicios a tu entorno y necesidades."),
            ("¿Lleváis el material necesario?", "Llevamos lo necesario para la sesión; si hace falta algo específico, te lo indicaremos antes."),
            ("¿Tiene un precio diferente?", "Sí, la atención a domicilio tiene su propia tarifa. Solicítala al pedir cita."),
            ("¿Puede estar un familiar presente?", "Sí, y es recomendable: así aprende pautas para ayudar en el día a día."),
            ("¿Cuándo conviene pasar a la clínica?", "Cuando puedas desplazarte con seguridad, venir a la clínica permite usar toda la tecnología disponible."),
        ],
    ),
    # ───────────────────────── NUTRICIÓN ─────────────────────────
    service(
        category="nutricion", slug="valoracion-nutricional", title="Valoración nutricional",
        short="Composición corporal y estado de salud", kicker="Conocer tu punto de partida", image="interior",
        lead="Evaluación nutricional completa y determinación del estado de salud mediante antropometría para orientar tu plan.",
        intro=[
            "Antes de cambiar nada, conviene saber de dónde partimos. La valoración nutricional reúne tus hábitos, tu historia de salud, tus objetivos y, cuando procede, la medición de tu composición corporal mediante antropometría.",
            "Con esa fotografía completa, la nutricionista puede proponer estrategias realistas y medir después los cambios de forma objetiva, más allá del número de la báscula.",
        ],
        facts=[("Incluye", "Antropometría"), ("Duración", "Consulta inicial completa"), ("Profesional", "Ana María Sancho")],
        benefits=[("Datos objetivos", "Composición corporal, no solo peso."), ("Plan con base", "Decisiones según tu situación real."), ("Detecta prioridades", "Qué cambiar primero para notar más."), ("Mide tu progreso", "Comparas tus datos en cada revisión.")],
        audience=["Quien quiere revisar sus hábitos", "Personas que buscan un plan ajustado a su caso", "Seguimiento de composición corporal", "Deportistas que quieren conocer su punto de partida", "Personas con condiciones de salud que afectan a la alimentación", "Quien no sabe por dónde empezar"],
        process=[("Entrevista", "Hábitos, horarios, gustos, salud y objetivos."), ("Mediciones", "Antropometría y composición corporal cuando procede."), ("Análisis", "Interpretamos los datos contigo."), ("Siguiente paso", "Definimos el plan y el seguimiento.")],
        prepare=["Analíticas recientes si las tienes", "Lista de medicación y suplementos", "Ropa cómoda para las mediciones", "Un registro de lo que comes en un par de días, si te es posible"],
        faqs=[
            ("¿Qué es la antropometría?", "Es un conjunto de mediciones corporales (perímetros, pliegues, peso, talla) que permite estudiar la composición corporal."),
            ("¿Tengo que tener un objetivo de peso?", "No. La consulta puede orientarse a salud, deporte o mejora de hábitos."),
            ("¿La primera visita incluye un plan?", "La valoración es la base del plan. Pregunta al reservar cómo se organiza la primera consulta."),
            ("¿Necesito una analítica?", "No es imprescindible, pero si tienes una reciente aporta información útil."),
            ("¿Cada cuánto se repiten las mediciones?", "Se acuerdan según tu objetivo, habitualmente en las revisiones de seguimiento."),
            ("¿Es para todas las edades?", "Consúltanos tu caso concreto y te orientaremos."),
        ],
    ),
    service(
        category="nutricion", slug="planes-alimentacion", title="Planes de alimentación",
        short="Pérdida, ganancia de peso y masa muscular", kicker="A tu medida", image="logo-escena",
        lead="Planes personalizados según tus objetivos: pérdida de peso, ganancia de peso o aumento de masa muscular.",
        intro=[
            "Un buen plan de alimentación no es una lista de prohibiciones: es una estructura flexible que encaja con tus horarios, tus gustos y tu forma de vivir. Por eso cada plan se diseña a partir de tu valoración.",
            "Trabajamos objetivos de pérdida de peso, ganancia de peso y aumento de masa muscular, siempre con un enfoque saludable y sostenible, y con revisiones para ajustar lo que haga falta.",
        ],
        facts=[("Objetivos", "Peso · masa muscular · salud"), ("Seguimiento", "Continuo"), ("Profesional", "Ana María Sancho")],
        benefits=[("Personalizado", "Según tu objetivo, tu rutina y tus gustos."), ("Sostenible", "Cambios que puedes mantener en el tiempo."), ("Flexible", "Opciones e intercambios, no menús rígidos."), ("Acompañado", "Revisiones y ajustes continuos.")],
        audience=["Pérdida de peso saludable", "Ganancia de peso", "Aumento de masa muscular", "Personas con poco tiempo para cocinar", "Familias que quieren comer mejor", "Quien ha probado dietas sin éxito"],
        process=[("Valoración", "Partimos de tu contexto y preferencias."), ("Diseño", "Plan adaptado a tus objetivos y horarios."), ("Aprendizaje", "Te enseñamos a organizarte y a elegir."), ("Ajuste", "Revisamos resultados y adaptamos el plan.")],
        prepare=["Tus horarios de trabajo y entrenamiento", "Alimentos que no te gustan o no toleras", "Tus objetivos, con la mayor concreción posible", "Analíticas recientes si las tienes"],
        faqs=[
            ("¿El plan se adapta a mis horarios?", "Sí. Comenta tus horarios, turnos y necesidades en la valoración y lo tendremos en cuenta."),
            ("¿Hay seguimiento?", "Sí. Ofrecemos acompañamiento continuo y seguimiento."),
            ("¿Sirve solo para perder peso?", "No. También para ganar peso, aumentar masa muscular o mejorar tu salud."),
            ("¿Tendré que pasar hambre?", "No es el objetivo. Buscamos saciedad, energía y adherencia."),
            ("¿Puedo comer fuera de casa?", "Sí. Te daremos pautas para elegir bien en restaurantes y celebraciones."),
            ("¿Necesito suplementos?", "No necesariamente. Solo se plantean si tu caso lo justifica."),
        ],
    ),
    service(
        category="nutricion", slug="nutricion-clinica", title="Tratamiento nutricional de enfermedades",
        short="Diabetes, hipertensión, colesterol y más", kicker="Cuidarte con contexto", image="salas",
        lead="Atención nutricional adaptada a diabetes, hipertensión, hipercolesterolemia, enfermedades digestivas, cáncer e intolerancias.",
        intro=[
            "La alimentación es una pieza clave en el manejo de muchas enfermedades. Nuestra nutricionista, con Máster Universitario en Nutrición Clínica, adapta la estrategia alimentaria a tu situación y a las indicaciones de tu equipo médico.",
            "El objetivo es que comas bien, con tranquilidad y sin miedo, entendiendo por qué cada cambio te ayuda.",
        ],
        facts=[("Especialidad", "Nutrición clínica"), ("Coordinado con", "Tu equipo médico"), ("Profesional", "Ana María Sancho")],
        benefits=[("Control de la enfermedad", "La alimentación como aliada del tratamiento."), ("Menos incertidumbre", "Sabes qué comer y por qué."), ("Calidad de vida", "Más energía y bienestar digestivo."), ("Seguimiento", "Ajustes según analíticas y evolución.")],
        audience=["Diabetes", "Hipertensión", "Hipercolesterolemia", "Enfermedades digestivas", "Cáncer (apoyo nutricional)", "Intolerancias alimentarias"],
        process=[("Historia clínica", "Recogemos tu situación e indicaciones médicas."), ("Estrategia", "Adaptamos la alimentación a tu condición."), ("Educación", "Aprendes a leer etiquetas y a planificar."), ("Seguimiento", "Revisamos analíticas y ajustamos.")],
        prepare=["Informes médicos y analíticas recientes", "Lista completa de medicación", "Diagnósticos de intolerancias si los tienes", "Registro de síntomas digestivos, si aplica"],
        faqs=[
            ("¿Sustituye al tratamiento médico?", "No. La consulta nutricional acompaña y complementa la atención médica que corresponda a tu situación."),
            ("¿Puedo acudir si tengo varias condiciones?", "Sí. Estudiaremos tus necesidades concretas en conjunto."),
            ("¿Se contemplan intolerancias?", "Sí. Las intolerancias están entre las condiciones que atendemos."),
            ("¿Ayudáis durante un tratamiento oncológico?", "Sí, con apoyo nutricional adaptado y siempre en coordinación con tu equipo oncológico."),
            ("¿Con diabetes puedo comer de todo?", "La clave está en el cómo, el cuánto y el cuándo. Te enseñaremos a organizarlo."),
            ("¿Necesito informe médico?", "No es obligatorio, pero sí muy recomendable para adaptar el plan con seguridad."),
        ],
    ),
    service(
        category="nutricion", slug="nutricion-deportiva", title="Nutrición deportiva",
        short="Estrategias para el rendimiento", kicker="Alimentar el movimiento", image="pilates-exterior-1",
        lead="Estrategias nutricionales ajustadas a tu deporte, tu entrenamiento y tus objetivos de rendimiento.",
        intro=[
            "Entrenar bien es la mitad del camino; la otra mitad es comer y recuperarse bien. La nutrición deportiva organiza tu alimentación alrededor del entrenamiento y la competición.",
            "Tanto si compites como si entrenas por salud, ajustamos energía, proteínas, hidratación y momentos de ingesta a tu práctica real. Y en coordinación con fisioterapia si estás recuperándote de una lesión.",
        ],
        facts=[("Para", "Todos los niveles"), ("Coordinado con", "Fisioterapia"), ("Profesional", "Ana María Sancho")],
        benefits=[("Más rendimiento", "Energía disponible cuando la necesitas."), ("Mejor recuperación", "Entre entrenamientos y tras lesiones."), ("Composición corporal", "Ganancia muscular o ajuste de grasa."), ("Hidratación", "Estrategias para entreno y competición.")],
        audience=["Deportistas habituales", "Corredores y deportes de montaña", "Deportes de equipo", "Objetivos de composición corporal", "Preparación de una competición", "Recuperación nutricional de lesiones"],
        process=[("Análisis", "Actividad, horarios, objetivos y hábitos."), ("Estrategia", "Plan alrededor de tus entrenamientos."), ("Competición", "Pautas para antes, durante y después."), ("Ajustes", "Seguimiento según temporada y resultados.")],
        prepare=["Tu calendario de entrenamientos", "Competiciones previstas", "Suplementos que tomas", "Registros de entrenamiento si los usas"],
        faqs=[
            ("¿Tengo que competir para acudir?", "No. La estrategia se adapta al nivel de actividad y al objetivo de cada persona."),
            ("¿También se aborda la masa muscular?", "Sí. Los planes incluyen el aumento de masa muscular cuando es un objetivo."),
            ("¿El plan cambia con el entrenamiento?", "Sí. El seguimiento permite adaptarlo si cambian tus cargas o tu temporada."),
            ("¿Me recomendaréis suplementos?", "Solo si tienen sentido para ti y cuentan con respaldo científico."),
            ("¿Trabajáis con clubes?", "Colaboramos con entidades deportivas locales. Pregúntanos si tu club está en convenio."),
            ("¿Qué como antes de una carrera?", "Depende de la distancia, la hora y tu tolerancia. Lo planificamos y lo probamos en entrenamientos."),
        ],
    ),
    service(
        category="nutricion", slug="educacion-nutricional", title="Educación nutricional",
        short="Recetas y hábitos que se quedan", kicker="Hábitos que te acompañan", image="tarjeta",
        lead="Ideas de recetas saludables y consejos sobre hábitos alimenticios para que comer bien sea fácil y duradero.",
        intro=[
            "El cambio que dura es el que entiendes. La educación nutricional te da herramientas: cómo organizar la compra, cómo leer etiquetas, cómo montar un plato equilibrado o cómo preparar recetas sencillas y saludables.",
            "Trabajamos a tu ritmo, con objetivos pequeños y alcanzables, para que los nuevos hábitos se integren en tu vida sin esfuerzo constante.",
        ],
        facts=[("Incluye", "Ideas de recetas"), ("Enfoque", "Cambio de hábitos"), ("Profesional", "Ana María Sancho")],
        benefits=[("Autonomía", "Aprendes a decidir sin depender de un menú."), ("Recetas fáciles", "Ideas saludables para el día a día."), ("Compra inteligente", "Etiquetas, planificación y ahorro."), ("Familia", "Hábitos que benefician a toda la casa.")],
        audience=["Personas que quieren mejorar sus hábitos", "Familias con niños", "Quien cocina poco o no sabe por dónde empezar", "Personas que necesitan mantener cambios", "Quien quiere dejar de hacer dietas", "Mayores que quieren cuidarse"],
        process=[("Identificar", "Tus hábitos actuales y dificultades."), ("Aprender", "Pautas comprensibles y aplicables."), ("Practicar", "Recetas y planificación semanal."), ("Consolidar", "Seguimiento hasta que sea automático.")],
        prepare=["Qué sueles comer en una semana normal", "Tus mayores dificultades", "Tiempo que tienes para cocinar", "Gustos de la familia, si cocinas para más personas"],
        faqs=[
            ("¿Incluye ideas de recetas?", "Sí. Compartimos ideas de recetas saludables y adaptadas a tu día a día."),
            ("¿Se trabaja con objetivos pequeños?", "Sí. La educación alimentaria se adapta a la situación y al ritmo de cada persona."),
            ("¿Hay acompañamiento después?", "Sí. El seguimiento continuo forma parte de la consulta nutricional."),
            ("¿Es útil para niños?", "Sí: aprender en familia facilita que los niños coman mejor."),
            ("¿Aprenderé a leer etiquetas?", "Sí, es una de las herramientas más útiles que trabajamos."),
            ("¿Puedo combinarlo con un plan de alimentación?", "Sí. De hecho, se complementan muy bien."),
        ],
    ),
    # ───────────────────────── PODOLOGÍA ─────────────────────────
    service(
        category="podologia", slug="estudio-pisada", title="Estudio de la pisada",
        short="Análisis biomecánico de la marcha", kicker="Entender cómo caminas", image="podologia-portada", hero="pasillo",
        lead="Análisis biomecánico para detectar y corregir problemas de postura y mejorar tu forma de caminar.",
        intro=[
            "La forma en que apoyas el pie influye en tobillos, rodillas, caderas y espalda. El estudio de la pisada analiza cómo caminas y cómo se reparten las cargas, para entender el origen de muchas molestias.",
            "Con los resultados, te explicamos qué ocurre y qué opciones hay: desde pautas de calzado y ejercicio hasta plantillas personalizadas cuando están indicadas.",
        ],
        facts=[("Tipo", "Análisis biomecánico"), ("Valora", "Pisada, marcha y postura"), ("Resultado", "Explicación y opciones")],
        benefits=[("Detecta el origen", "De dolores en pies, rodillas o espalda."), ("Mejora la marcha", "Caminar y correr con más eficiencia."), ("Previene lesiones", "Especialmente en deportistas."), ("Base para plantillas", "Si las necesitas, a partir de datos reales.")],
        audience=["Dolor de pies, rodillas, caderas o espalda al caminar", "Corredores y deportistas", "Niños con alteraciones de la marcha", "Pies planos o cavos", "Desgaste irregular del calzado", "Valoración previa a plantillas personalizadas"],
        process=[("Entrevista", "Síntomas, actividad y calzado habitual."), ("Exploración", "Estática y en movimiento."), ("Análisis", "Cómo apoyas y cómo caminas."), ("Explicación", "Hallazgos y opciones de tratamiento.")],
        prepare=["El calzado que usas a diario", "Tus zapatillas de deporte", "Pantalón corto o que se pueda remangar", "Plantillas anteriores, si las tienes"],
        faqs=[
            ("¿El estudio implica siempre llevar plantillas?", "No. El estudio sirve para valorar tu caso; la recomendación depende de los resultados."),
            ("¿Se analiza la marcha?", "Sí. Es un análisis biomecánico de la marcha y la postura."),
            ("¿Debo llevar mi calzado?", "Sí: el de diario y el deportivo. Nos aporta mucha información."),
            ("¿Es útil en niños?", "Sí, en niños con alteraciones de la marcha o molestias, siempre tras valoración."),
            ("¿Duele?", "No. Es una exploración completamente indolora."),
            ("¿Cada cuánto debo repetirlo?", "Depende de tu caso y de si llevas plantillas; te lo indicaremos."),
        ],
    ),
    service(
        category="podologia", slug="plantillas-personalizadas", title="Plantillas personalizadas",
        short="Diseñadas para tu pie", kicker="Apoyo adaptado a ti", image="podologia-portada", hero="salas",
        lead="Plantillas adaptadas a cada paciente a partir del estudio biomecánico de la pisada.",
        intro=[
            "Unas plantillas personalizadas no son un producto de estantería: se diseñan a partir de tu estudio de la pisada para corregir o compensar alteraciones del apoyo y mejorar la marcha.",
            "Tenemos en cuenta tu calzado, tu actividad y tus molestias, y revisamos la adaptación para asegurarnos de que cumplen su función con comodidad.",
        ],
        facts=[("Base", "Estudio de la pisada"), ("Fabricación", "A medida"), ("Incluye", "Revisión de adaptación")],
        benefits=[("Reparto de cargas", "Menos presión en zonas que duelen."), ("Postura", "Mejor alineación al caminar."), ("Comodidad", "Adaptadas a tu calzado y actividad."), ("Prevención", "Menos sobrecargas y lesiones.")],
        audience=["Personas a quienes se recomiendan tras el estudio", "Fascitis plantar y talalgias", "Metatarsalgias", "Pies planos o cavos sintomáticos", "Deportistas con sobrecargas", "Dolor de rodilla relacionado con la pisada"],
        process=[("Estudio", "Realizamos o revisamos el estudio de la pisada."), ("Diseño", "Definimos las características de la plantilla."), ("Entrega", "Ajustamos a tu calzado."), ("Revisión", "Comprobamos la adaptación y el seguimiento.")],
        prepare=["El calzado donde las usarás", "Plantillas anteriores, si tienes", "Información sobre tu actividad diaria", "Tus molestias, con el mayor detalle posible"],
        faqs=[
            ("¿Son iguales para todo el mundo?", "No. Son plantillas personalizadas y adaptadas a cada paciente."),
            ("¿Necesito un estudio previo?", "Sí. Las plantillas se diseñan a partir del análisis biomecánico de la pisada."),
            ("¿Cuánto tardo en acostumbrarme?", "Suele ser un periodo corto y progresivo. Te daremos pautas para la adaptación."),
            ("¿Valen para cualquier zapato?", "Depende del diseño. Te indicaremos con qué calzado funcionan mejor."),
            ("¿Cuánto duran?", "Depende del uso y del material. Recomendamos revisiones periódicas."),
            ("¿Cuánto cuestan?", "El precio depende del tipo de plantilla. Consúltalo sin compromiso por WhatsApp."),
        ],
    ),
    service(
        category="podologia", slug="ortesis-silicona", title="Órtesis de silicona",
        short="Soluciones a medida para los dedos", kicker="Soluciones para los dedos", image="podologia-portada", hero="interior",
        lead="Dispositivos personalizados para aliviar deformidades en los dedos, corregir la posición y reducir el dolor.",
        intro=[
            "Las órtesis de silicona se moldean a medida sobre tu pie para proteger, separar o corregir la posición de los dedos. Son discretas, cómodas y se adaptan al calzado.",
            "Resultan muy útiles en dedos en garra o en martillo, juanetes, roces o helomas entre dedos, aliviando la presión y el dolor al caminar.",
        ],
        facts=[("Fabricación", "A medida"), ("Material", "Silicona"), ("Objetivo", "Alivio y corrección")],
        benefits=[("Menos dolor", "Reduce la presión y los roces."), ("Protección", "De zonas con durezas o helomas."), ("Corrección", "Mejora la posición de los dedos."), ("Discretas", "Caben en tu calzado habitual.")],
        audience=["Dedos en garra o en martillo", "Juanetes (hallux valgus)", "Helomas entre dedos", "Roces y rozaduras recurrentes", "Dedos superpuestos", "Personas mayores con deformidades dolorosas"],
        process=[("Valoración", "Forma del pie y origen de la molestia."), ("Moldeado", "Diseñamos la órtesis sobre tu pie."), ("Prueba", "Comprobamos ajuste y comodidad."), ("Pautas", "Uso, limpieza y revisión.")],
        prepare=["El calzado que usas habitualmente", "Pies limpios y sin cremas", "Cuéntanos qué te molesta y cuándo", "Avísanos si tienes diabetes o problemas circulatorios"],
        faqs=[
            ("¿Se hacen a medida?", "Sí. Son dispositivos personalizados moldeados sobre tu pie."),
            ("¿Qué objetivo tienen?", "Aliviar deformidades, corregir posiciones y reducir el dolor."),
            ("¿Se lavan?", "Sí, con agua y jabón neutro. Te daremos las pautas de cuidado."),
            ("¿Cuánto duran?", "Depende del uso. Con buen cuidado, suelen durar bastante tiempo; las revisaremos contigo."),
            ("¿Corrigen un juanete?", "Alivian presión y dolor y mejoran la posición, pero no eliminan la deformidad ósea."),
            ("¿Necesito cita previa?", "Sí. Contacta para organizar la valoración podológica."),
        ],
    ),
    service(
        category="podologia", slug="quiropodia", title="Quiropodia",
        short="Durezas, callosidades y uñas encarnadas", kicker="Cuidado cotidiano del pie", image="podologia-portada", hero="recepcion",
        lead="Tratamiento especializado para eliminar callosidades, durezas, uñas encarnadas y otros problemas comunes en los pies.",
        intro=[
            "La quiropodia es el tratamiento podológico básico y más demandado: elimina durezas, callosidades y helomas, corta y trata las uñas correctamente y resuelve uñas encarnadas.",
            "Además de aliviar, buscamos el porqué: si una dureza vuelve una y otra vez, puede haber una alteración de la pisada o del calzado que conviene corregir.",
        ],
        facts=[("Duración", "Sesión única o periódica"), ("Sensación", "Alivio inmediato"), ("A domicilio", "Disponible")],
        benefits=[("Alivio inmediato", "Al eliminar la presión de durezas."), ("Uñas sanas", "Corte correcto y tratamiento de encarnadas."), ("Prevención", "Detectamos problemas a tiempo."), ("Higiene profesional", "Instrumental estéril y técnica segura.")],
        audience=["Callosidades y durezas", "Helomas (callos)", "Uñas encarnadas", "Uñas engrosadas o difíciles de cortar", "Personas mayores", "Pie diabético (cuidado preventivo)"],
        process=[("Valoración", "Estado del pie y causa de la molestia."), ("Tratamiento", "Deslaminado, enucleación y cuidado de uñas."), ("Consejos", "Hidratación, calzado y corte de uñas."), ("Seguimiento", "Revisiones periódicas si las necesitas.")],
        prepare=["Pies limpios y sin esmalte en las uñas", "El calzado que usas habitualmente", "Avísanos si tienes diabetes o tomas anticoagulantes", "Cuéntanos si alguna zona te duele especialmente"],
        faqs=[
            ("¿La quiropodia sirve para uñas encarnadas?", "Sí. Es uno de los problemas que tratamos en este servicio."),
            ("¿También se tratan durezas?", "Sí. Durezas, callosidades y helomas."),
            ("¿Duele?", "No suele doler; al contrario, la mayoría de personas sale con alivio inmediato."),
            ("¿Cada cuánto debería hacerme una quiropodia?", "Depende de cada pie. Para muchas personas, una revisión periódica cada pocos meses es suficiente."),
            ("¿Puedo pedir atención a domicilio?", "Sí. Existe servicio de podología a domicilio; consulta cobertura y disponibilidad."),
            ("¿Es recomendable si tengo diabetes?", "Sí, especialmente. El cuidado profesional reduce el riesgo de heridas y complicaciones."),
        ],
    ),
    service(
        category="podologia", slug="reconstruccion-ungueal", title="Reconstrucción ungueal",
        short="Uñas sanas y estéticas", kicker="Recuperar la uña", image="podologia-portada", hero="logo-escena",
        lead="Técnica avanzada para restaurar uñas dañadas o deformadas, mejorando su estética y su funcionalidad.",
        intro=[
            "Golpes, hongos o deformidades pueden dejar una uña dañada, rota o con mal aspecto. La reconstrucción ungueal restaura su forma con materiales específicos, protegiendo el lecho y favoreciendo un crecimiento correcto.",
            "Mejora la estética del pie —algo importante para muchas personas, sobre todo en verano— y también su función, al proteger el dedo y guiar el crecimiento de la uña natural.",
        ],
        facts=[("Objetivo", "Estético y funcional"), ("Técnica", "Avanzada"), ("Requiere", "Valoración previa")],
        benefits=[("Mejor aspecto", "Uñas con forma y apariencia natural."), ("Protección", "Del lecho ungueal y del dedo."), ("Crecimiento guiado", "Favorece que la uña crezca correctamente."), ("Confianza", "Vuelve a lucir tus pies sin complejos.")],
        audience=["Uñas dañadas por golpes", "Uñas deformadas", "Uñas rotas o con pérdida parcial", "Tras tratamientos de hongos", "Uñas con mal aspecto", "Personas que quieren mejorar la estética del pie"],
        process=[("Examen", "Valoramos la uña y su estado."), ("Indicación", "Explicamos si la reconstrucción es adecuada."), ("Procedimiento", "Reconstruimos la uña con material específico."), ("Cuidados", "Pautas para mantenerla y revisiones.")],
        prepare=["Uñas sin esmalte", "Pies limpios", "Cuéntanos el origen del daño", "Tratamientos previos que hayas hecho"],
        faqs=[
            ("¿Se puede hacer en cualquier uña?", "Es necesaria una valoración previa para decidir si la técnica está indicada."),
            ("¿Busca solo mejorar la estética?", "No. Tiene un objetivo estético y funcional."),
            ("¿Se puede hacer con hongos?", "Primero hay que tratar la infección. La reconstrucción se valora después."),
            ("¿Cuánto dura?", "Depende del crecimiento de la uña y del cuidado. Te indicaremos cuándo revisarla."),
            ("¿Puedo pintarme las uñas después?", "Te diremos cuándo y con qué productos para no dañar la reconstrucción."),
            ("¿Qué cuidados requiere después?", "La profesional te indicará los cuidados adecuados para tu caso."),
        ],
    ),
    service(
        category="podologia", slug="podologia-general", title="Podología general",
        short="Hongos, pie diabético y circulación", kicker="Salud desde los pies", image="podologia-portada", hero="fachada",
        lead="Cuidado integral de los pies para prevenir y tratar afecciones comunes, incluyendo hongos, pie diabético y problemas circulatorios.",
        intro=[
            "La podología general atiende cualquier problema del pie: infecciones por hongos, verrugas, alteraciones de la piel y las uñas, y el cuidado preventivo de pies con más riesgo, como el pie diabético.",
            "Si no sabes qué te pasa, este es el punto de partida: valoramos la molestia y te orientamos hacia el tratamiento o el servicio adecuado.",
        ],
        facts=[("Enfoque", "Prevención y tratamiento"), ("Atendemos", "Pie diabético"), ("A domicilio", "Disponible")],
        benefits=[("Diagnóstico podológico", "Sabes qué ocurre y cómo tratarlo."), ("Prevención", "Especialmente en pie diabético."), ("Tratamientos", "Hongos, verrugas y alteraciones de piel."), ("Orientación", "Derivación cuando es necesario.")],
        audience=["Hongos en uñas o piel", "Pie diabético", "Problemas circulatorios", "Verrugas plantares", "Sudoración o mal olor", "Revisión preventiva de los pies"],
        process=[("Revisión", "Estado de tus pies y antecedentes."), ("Diagnóstico", "Identificamos el problema."), ("Tratamiento", "El indicado o derivación cuando corresponda."), ("Prevención", "Pautas de cuidado y seguimiento.")],
        prepare=["Pies limpios y uñas sin esmalte", "Informes médicos si tienes diabetes", "Lista de medicación", "El calzado habitual"],
        faqs=[
            ("¿Puedo acudir sin saber qué problema tengo?", "Sí. La consulta permite valorar la molestia y orientar el siguiente paso."),
            ("¿Atendéis el pie diabético?", "Sí. Es una de las afecciones incluidas en la podología general del centro."),
            ("¿Tratáis los hongos en las uñas?", "Sí. Valoramos el caso y planteamos el tratamiento más adecuado."),
            ("¿Y las verrugas plantares?", "Sí, tras valorarlas en consulta."),
            ("¿También se ofrece prevención?", "Sí. El servicio está orientado a prevenir y tratar afecciones comunes."),
            ("¿Cada cuánto debe revisarse un pie diabético?", "Con regularidad. Te indicaremos la frecuencia según tu situación."),
        ],
    ),
    service(
        category="podologia", slug="podologia-domicilio", title="Podología a domicilio",
        short="Cuidado de los pies en casa", kicker="Cuidado en casa", image="podologia-portada", hero="bolsa", place="A domicilio",
        lead="Atención podológica en la comodidad de tu hogar, ideal para personas con movilidad reducida o necesidades especiales.",
        intro=[
            "Para muchas personas mayores o con movilidad reducida, cortarse las uñas o cuidar una dureza se convierte en un problema. Con la podología a domicilio, el cuidado profesional llega a casa.",
            "Llevamos el material necesario y aplicamos el mismo rigor e higiene que en la clínica, con la tranquilidad de estar en tu entorno.",
        ],
        facts=[("Modalidad", "En tu domicilio"), ("Ideal para", "Movilidad reducida"), ("Cobertura", "Consultar localidad")],
        benefits=[("Sin desplazamientos", "Cuidado profesional en casa."), ("Tranquilidad", "Para la persona y la familia."), ("Prevención", "Detectamos problemas a tiempo."), ("Mismo rigor", "Higiene y técnica profesional.")],
        audience=["Personas con movilidad reducida", "Personas mayores", "Pacientes encamados o convalecientes", "Pie diabético con dificultad para desplazarse", "Familias que organizan el cuidado de un ser querido", "Residencias y viviendas tuteladas, a consultar"],
        process=[("Contacto", "Explica por WhatsApp la necesidad y la localidad."), ("Confirmación", "Confirmamos cobertura, disponibilidad y tipo de atención."), ("Visita", "Atención en casa con material profesional."), ("Seguimiento", "Programamos las siguientes visitas si hace falta.")],
        prepare=["Un lugar con buena luz y una silla cómoda", "Pies limpios", "Informes médicos relevantes", "Si es posible, la presencia de un familiar"],
        faqs=[
            ("¿En qué localidades está disponible?", "Villanueva del Rosario y alrededores. Indica tu localidad al contactar y te confirmamos."),
            ("¿Qué tratamientos se pueden hacer en casa?", "La mayoría de cuidados de quiropodia: uñas, durezas, callos. El resto, según el caso."),
            ("¿Es igual de higiénico que en la clínica?", "Sí. Usamos instrumental esterilizado y material desechable."),
            ("¿La tarifa es distinta?", "Sí, el domicilio tiene su propia tarifa. Consúltala al pedir cita."),
            ("¿Atendéis pie diabético a domicilio?", "Sí, con especial cuidado y pautas de prevención."),
            ("¿Cada cuánto conviene la visita?", "Depende de cada persona; muchas necesitan una revisión periódica cada pocos meses."),
        ],
    ),
]
