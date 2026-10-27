# -*- coding: utf-8 -*-
"""Genera la web bilingüe de Aqua Beauty & Spa (Boston -> Colombia).
Editar los textos aquí y correr:  python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------- Datos de contacto (pendientes de confirmar) ----------
WHATSAPP = ""          # ej. "573001234567" -> activa los botones de WhatsApp
EMAIL = ""             # ej. "info@aquabeautyspa.com"
PRECIO_VALORACION = "200 USD"


def T(es, en):
    """Texto en línea bilingüe."""
    return f'<span data-l="es">{es}</span><span data-l="en">{en}</span>'


def B(es, en, tag="div", cls=""):
    """Bloque bilingüe."""
    c = f' class="{cls}"' if cls else ""
    return f'<{tag} data-l="es"{c}>{es}</{tag}><{tag} data-l="en"{c}>{en}</{tag}>'


def foto(slug):
    return os.path.exists(os.path.join(ROOT, "img", slug + ".jpg"))


def media(slug, cls="media"):
    if foto(slug):
        return f'<div class="{cls}"><img src="img/{slug}.jpg" srcset="img/{slug}-sm.jpg 700w, img/{slug}.jpg 1400w" sizes="(max-width: 820px) 92vw, 45vw" alt="" loading="lazy" decoding="async"></div>'
    return f'<div class="{cls} ph">{icon(slug, 44)}</div>'


NUBES = """<div class="sky" aria-hidden="true">
  <span class="cl cl1"></span><span class="cl cl2"></span><span class="cl cl3"></span><span class="cl cl4"></span><span class="cl cl5"></span>
  <svg class="mnt" viewBox="0 0 1440 260" preserveAspectRatio="none"><path class="m1" d="M0 190 C 120 150 200 120 300 135 C 400 150 460 80 580 95 C 700 110 760 160 880 140 C 1000 120 1060 70 1180 90 C 1300 110 1380 150 1440 140 L1440 260 L0 260Z"/><path class="m2" d="M0 225 C 160 180 280 205 420 185 C 560 165 640 215 800 200 C 960 185 1040 160 1200 190 C 1320 212 1400 200 1440 205 L1440 260 L0 260Z"/></svg>
  <span class="cl fog1"></span><span class="cl fog2"></span>
</div>"""


def cta_href():
    return "#contacto"


# ---------- Servicios ----------
SERVICIOS = [
    {
        "slug": "obesidad",
        "es": "Obesidad", "en": "Weight Loss",
        "kicker_es": "Programa médico de 4 meses", "kicker_en": "4-month medical program",
        "resumen_es": "Tirzepatida y un equipo de 5 especialistas para bajar de peso de forma segura y sostenible.",
        "resumen_en": "Tirzepatide and a team of 5 specialists for safe, lasting weight loss.",
        "intro_es": "Un programa médico integral para bajar de peso con acompañamiento real. Combinamos tratamiento inyectable, formulado y vigilado por médicos, con un equipo multidisciplinario que trabaja contigo durante cuatro meses.",
        "intro_en": "A comprehensive medical weight-loss program with real support. We combine physician-prescribed and monitored injectable treatment with a multidisciplinary team that works with you for four months.",
        "destacado": [("4", "meses de programa", "month program"),
                      ("5", "especialistas", "specialists"),
                      ("10", "citas incluidas", "visits included")],
        "bloques": [
            {
                "t_es": "Tratamiento con inyectables", "t_en": "Injectable treatment",
                "p_es": "Trabajamos con <strong>tirzepatida</strong>, un medicamento inyectable de aplicación semanal que actúa sobre dos hormonas del intestino (GIP y GLP-1). Ayuda a reducir el apetito, a sentir saciedad más rápido y a mejorar el control del azúcar en la sangre. La dosis se ajusta de forma progresiva y siempre bajo prescripción y control médico.",
                "p_en": "We work with <strong>tirzepatide</strong>, a once-weekly injectable medication that acts on two gut hormones (GIP and GLP-1). It helps reduce appetite, makes you feel full sooner and improves blood sugar control. The dose is increased gradually and always under medical prescription and supervision.",
            },
        ],
        "pasos_t_es": "Tus 4 meses, mes a mes", "pasos_t_en": "Your 4 months, month by month",
        "pasos": [
            ("Mes 1 · Arranque", "Month 1 · Start", "Primera cita con los 5 especialistas, exámenes y tu plan: tratamiento, alimentación y ejercicio.", "First visit with all 5 specialists, lab work and your plan: treatment, nutrition and exercise."),
            ("Mes 2 · Ajuste", "Month 2 · Adjust", "Ajustamos la dosis y el plan según cómo responde tu cuerpo.", "We adjust dose and plan based on how your body responds."),
            ("Mes 3 · Seguimiento", "Month 3 · Follow-up", "Segunda cita con cada especialista y revisión de tu progreso.", "Second visit with each specialist and progress review."),
            ("Mes 4 · Hábitos", "Month 4 · Habits", "Consolidamos lo aprendido y te dejamos un plan para mantener tus resultados.", "We lock in your new habits and give you a plan to keep your results."),
        ],
        "cards_t_es": "Tu equipo multidisciplinario", "cards_t_en": "Your multidisciplinary team",
        "cards_sub_es": "Dentro del paquete tienes <strong>2 citas con cada especialista</strong>.",
        "cards_sub_en": "Your package includes <strong>2 visits with each specialist</strong>.",
        "cards": [
            ("Nutrióloga", "Medical Nutrition Specialist", "Médica especialista que diseña el manejo médico del peso y formula el tratamiento.", "Physician who designs your medical weight plan and prescribes treatment."),
            ("Deportólogo", "Sports Medicine", "Crea un plan de actividad física seguro y a tu medida.", "Builds a safe exercise plan tailored to you."),
            ("Nutricionista", "Dietitian", "Plan de alimentación práctico que puedas sostener en el tiempo.", "A practical eating plan you can keep for the long term."),
            ("Medicina interna", "Internal Medicine", "Revisa tu salud general, exámenes y enfermedades asociadas.", "Reviews your overall health, lab work and related conditions."),
            ("Psicología", "Psychology", "Acompaña la relación con la comida, los hábitos y la motivación.", "Supports your relationship with food, habits and motivation."),
        ],
        "incluye_es": ["Programa de 4 meses", "2 citas con cada uno de los 5 especialistas (10 en total)", "Tratamiento con tirzepatida si el médico lo indica", "Plan de alimentación y de actividad física", "Seguimiento de tu progreso"],
        "incluye_en": ["4-month program", "2 visits with each of the 5 specialists (10 total)", "Tirzepatide treatment when medically indicated", "Nutrition and exercise plan", "Progress follow-up"],
        "nota_es": "El tratamiento inyectable solo se indica si el médico lo considera adecuado después de tu valoración.",
        "nota_en": "Injectable treatment is only prescribed if the physician considers it appropriate after your consultation.",
        "faq": [
            ("¿Qué es la tirzepatida?", "What is tirzepatide?", "Es un medicamento inyectable semanal que ayuda a controlar el apetito y el azúcar en la sangre. Se usa bajo prescripción médica.", "A once-weekly injectable medication that helps control appetite and blood sugar. It is used under medical prescription."),
            ("¿Cuánto dura el programa?", "How long is the program?", "Cuatro meses, con dos citas con cada uno de los cinco especialistas.", "Four months, with two visits with each of the five specialists."),
        ],
    },
    {
        "slug": "cirugia-plastica",
        "es": "Cirugía plástica", "en": "Plastic Surgery",
        "kicker_es": "Cirujanos plásticos certificados", "kicker_en": "Board-certified plastic surgeons",
        "resumen_es": "Cirugía facial, mamaria y corporal con cirujanos certificados y acompañamiento de principio a fin.",
        "resumen_en": "Facial, breast and body surgery with certified surgeons and support from start to finish.",
        "intro_es": "Colombia es un referente mundial en cirugía plástica. Te acompañamos desde la valoración hasta tu recuperación, con cirujanos plásticos certificados y un plan claro de estadía.",
        "intro_en": "Colombia is a world leader in plastic surgery. We support you from your consultation through recovery, with certified plastic surgeons and a clear stay plan.",
        "destacado": [("3", "áreas: rostro, senos y cuerpo", "areas: face, breasts, body"),
                      ("18", "procedimientos", "procedures"),
                      ("100%", "cirujanos certificados", "certified surgeons")],
        "pasos_t_es": "Tu viaje, paso a paso", "pasos_t_en": "Your journey, step by step",
        "pasos": [
            ("Antes de viajar", "Before you travel", "Nos cuentas qué quieres, revisamos tu caso y te decimos qué exámenes traer y cuántos días quedarte.", "Tell us your goals; we review your case and tell you which tests to bring and how long to stay."),
            ("Valoración", "Consultation", f"Te reúnes con el cirujano plástico en nuestra sede de Colombia ({PRECIO_VALORACION}).", f"Meet your plastic surgeon at our Colombia location ({PRECIO_VALORACION})."),
            ("Exámenes y anestesia", "Pre-op & anesthesia", "Exámenes prequirúrgicos y valoración con anestesiología para operarte con seguridad.", "Pre-op labs and anesthesia evaluation so your surgery is safe."),
            ("Tu cirugía", "Your surgery", "Cirujanos certificados, en un entorno seguro y con todo el acompañamiento.", "Certified surgeons, a safe setting and full support."),
            ("Recuperación en Colombia", "Recovery in Colombia", "Controles postoperatorios con tu cirujano hasta que estés lista para volar.", "Post-op check-ups with your surgeon until you're ready to fly."),
            ("De vuelta en casa", "Back home", "Seguimos pendientes de tu evolución desde Boston.", "We keep following your progress from Boston."),
        ],
        "bloques": [],
        "grupos": [
            ("Rostro", "Face", [("Rinoplastia", "Rhinoplasty"), ("Blefaroplastia (párpados)", "Blepharoplasty (eyelids)"), ("Lifting facial y de cuello", "Face & neck lift"), ("Otoplastia (orejas)", "Otoplasty (ears)"), ("Bichectomía", "Buccal fat removal"), ("Mentoplastia", "Chin surgery")]),
            ("Senos", "Breasts", [("Aumento mamario", "Breast augmentation"), ("Levantamiento (mastopexia)", "Breast lift"), ("Reducción mamaria", "Breast reduction"), ("Retiro de implantes (explante)", "Implant removal"), ("Ginecomastia", "Gynecomastia")]),
            ("Cuerpo", "Body", [("Liposucción / lipoescultura", "Liposuction / lipo sculpting"), ("Abdominoplastia", "Tummy tuck"), ("Lipotransferencia glútea", "Buttock fat transfer (BBL)"), ("Braquioplastia (brazos)", "Arm lift"), ("Cruroplastia (muslos)", "Thigh lift"), ("Mommy makeover", "Mommy makeover"), ("Contorno después de bajar de peso", "Post weight-loss contouring")]),
        ],
        "cards_t_es": "", "cards_t_en": "", "cards_sub_es": "", "cards_sub_en": "", "cards": [],
        "incluye_es": ["Valoración con cirujano plástico certificado", "Exámenes prequirúrgicos y valoración de anestesia", "Plan de estadía y recuperación en Colombia", "Controles postoperatorios", "Acompañamiento durante todo el proceso"],
        "incluye_en": ["Consultation with a certified plastic surgeon", "Pre-op labs and anesthesia evaluation", "Stay and recovery plan in Colombia", "Post-op follow-up visits", "Support throughout the whole process"],
        "nota_es": "El tiempo de estadía en Colombia depende del procedimiento; en la valoración te decimos cuántos días quedarte para una recuperación segura.",
        "nota_en": "Your length of stay in Colombia depends on the procedure; at your consultation we tell you how many days to stay for a safe recovery.",
        "faq": [
            ("¿Puedo combinar procedimientos?", "Can I combine procedures?", "En muchos casos sí. El cirujano define qué combinaciones son seguras para ti.", "In many cases, yes. The surgeon decides which combinations are safe for you."),
        ],
    },
    {
        "slug": "medicina-vascular",
        "es": "Medicina vascular", "en": "Vascular Medicine",
        "kicker_es": "Endoláser para várices", "kicker_en": "Endovenous laser for varicose veins",
        "resumen_es": "Endoláser: tratamiento de várices sin cirugía abierta, ambulatorio y con recuperación rápida.",
        "resumen_en": "Endovenous laser: varicose vein treatment without open surgery, outpatient and with quick recovery.",
        "intro_es": "Tratamos las várices y la insuficiencia venosa con <strong>endoláser</strong>, una técnica mínimamente invasiva que reemplaza la cirugía tradicional. Sin grandes cortes, sin hospitalización y con regreso rápido a tu vida diaria.",
        "intro_en": "We treat varicose veins and venous insufficiency with <strong>endovenous laser (EVLA)</strong>, a minimally invasive technique that replaces traditional surgery. No large incisions, no hospital stay and a quick return to daily life.",
        "destacado": [("~1 h", "de procedimiento", "procedure"),
                      ("0", "hospitalización", "hospital stay"),
                      ("24–72 h", "para volver a tu rutina", "back to routine")],
        "bloques": [
            {
                "t_es": "¿Qué es el endoláser?", "t_en": "What is endovenous laser?",
                "p_es": "Es un tratamiento en el que se introduce una fibra láser muy delgada dentro de la vena enferma, guiada por ecografía. La energía del láser calienta y cierra la vena desde adentro; la sangre se redirige de forma natural por venas sanas y, con el tiempo, el cuerpo absorbe la vena tratada.",
                "p_en": "A very thin laser fiber is inserted into the diseased vein under ultrasound guidance. The laser energy heats and seals the vein from the inside; blood naturally reroutes through healthy veins and, over time, the body absorbs the treated vein.",
            },
            {
                "t_es": "¿Para quién es?", "t_en": "Who is it for?",
                "p_es": "Para personas con várices, piernas pesadas o cansadas, hinchazón, calambres, dolor al final del día o cambios en la piel por insuficiencia venosa. El especialista confirma la indicación con una <strong>ecografía Doppler venosa</strong>.",
                "p_en": "For people with varicose veins, heavy or tired legs, swelling, cramps, end-of-day pain or skin changes caused by venous insufficiency. The specialist confirms the indication with a <strong>venous Doppler ultrasound</strong>.",
            },
        ],
        "cards_t_es": "Cómo es el tratamiento", "cards_t_en": "What treatment looks like",
        "cards_sub_es": "", "cards_sub_en": "",
        "cards": [
            ("1. Valoración y Doppler", "1. Consultation & Doppler", "El especialista revisa tus piernas y mapea las venas con ecografía.", "The specialist examines your legs and maps your veins with ultrasound."),
            ("2. Anestesia local", "2. Local anesthesia", "Se usa anestesia local; estás despierto y cómodo.", "Local anesthesia is used; you stay awake and comfortable."),
            ("3. Láser guiado", "3. Guided laser", "Se cierra la vena desde adentro a través de una pequeña punción.", "The vein is sealed from the inside through a tiny puncture."),
            ("4. Caminas el mismo día", "4. Walk the same day", "Sales caminando, con media de compresión y recomendaciones.", "You walk out with a compression stocking and instructions."),
        ],
        "incluye_es": ["Tratamiento ambulatorio, sin hospitalización", "Sin cicatrices visibles: solo una pequeña punción", "Menos dolor y hematomas que la cirugía tradicional", "Regreso a actividades suaves en 24 a 72 horas", "Controles con el especialista"],
        "incluye_en": ["Outpatient, no hospital stay", "No visible scars: just a tiny puncture", "Less pain and bruising than traditional surgery", "Back to light activity within 24–72 hours", "Follow-up visits with the specialist"],
        "nota_es": "Te indicaremos cuántos días quedarte en Colombia para tus controles después del procedimiento.",
        "nota_en": "We will tell you how many days to stay in Colombia for your post-procedure follow-up.",
        "faq": [
            ("¿Duele?", "Does it hurt?", "Se hace con anestesia local. La mayoría de pacientes siente molestias leves que se controlan con analgésicos comunes.", "It is done under local anesthesia. Most patients feel mild discomfort, managed with common pain relievers."),
            ("¿Las várices pueden volver?", "Can varicose veins come back?", "La vena tratada no vuelve, pero pueden aparecer várices nuevas con el tiempo. Por eso hacemos seguimiento.", "The treated vein does not come back, but new ones can appear over time. That is why we do follow-up."),
        ],
    },
    {
        "slug": "odontologia",
        "es": "Odontología", "en": "Dentistry",
        "kicker_es": "Tu sonrisa, completa", "kicker_en": "Your complete smile",
        "resumen_es": "Diseño de sonrisa, implantes, ortodoncia y todo lo que tu boca necesita, en un solo lugar.",
        "resumen_en": "Smile design, implants, orthodontics and everything your mouth needs, in one place.",
        "intro_es": "Odontología general y especializada para que llegues a Colombia y te vayas con la sonrisa que quieres. Planeamos todo tu tratamiento desde antes del viaje para aprovechar al máximo tu tiempo con nosotros.",
        "intro_en": "General and specialized dentistry so you can come to Colombia and leave with the smile you want. We plan your entire treatment before your trip to make the most of your time with us.",
        "destacado": [],
        "aviso_es": "<strong>Importante:</strong> antes de tu cita de valoración necesitas una <strong>radiografía panorámica</strong> reciente. Nos permite planear tu tratamiento con precisión.",
        "aviso_en": "<strong>Important:</strong> before your consultation you need a recent <strong>panoramic X-ray</strong>. It allows us to plan your treatment precisely.",
        "bloques": [],
        "cards_t_es": "Nuestros servicios", "cards_t_en": "Our services",
        "cards_sub_es": "", "cards_sub_en": "",
        "cards": [
            ("Diseño de sonrisa", "Smile design", "Carillas en porcelana o resina para cambiar forma, color y tamaño de los dientes.", "Porcelain or composite veneers to change tooth shape, color and size."),
            ("Implantes dentales", "Dental implants", "Reemplazo fijo de dientes perdidos con implantes de titanio y corona.", "Fixed replacement of missing teeth with titanium implants and crowns."),
            ("Rehabilitación oral", "Full-mouth rehabilitation", "Coronas, puentes y prótesis para recuperar función y estética.", "Crowns, bridges and dentures to restore function and looks."),
            ("Blanqueamiento", "Teeth whitening", "Aclara varios tonos tus dientes de forma segura en consultorio.", "Safely whitens your teeth several shades in-office."),
            ("Ortodoncia", "Orthodontics", "Brackets o alineadores invisibles para corregir la posición de los dientes.", "Braces or clear aligners to straighten your teeth."),
            ("Endodoncia", "Root canals", "Tratamiento de conductos para salvar dientes con daño profundo.", "Root canal therapy to save deeply damaged teeth."),
            ("Periodoncia", "Periodontics", "Cuidado de encías: tratamiento de sangrado, retracción e infección.", "Gum care: treatment of bleeding, recession and infection."),
            ("Cirugía oral", "Oral surgery", "Extracción de cordales y cirugías de preparación para implantes.", "Wisdom tooth removal and implant preparation surgery."),
            ("Limpieza y prevención", "Cleaning & prevention", "Profilaxis, control de placa y revisión general.", "Professional cleaning, plaque control and checkup."),
        ],
        "incluye_es": [], "incluye_en": [],
        "nota_es": "", "nota_en": "",
        "faq": [
            ("¿Qué es una radiografía panorámica?", "What is a panoramic X-ray?", "Es una radiografía que muestra toda la boca en una sola imagen: dientes, raíces, maxilares y articulaciones. Puedes tomarla en tu ciudad y enviárnosla.", "An X-ray that shows your whole mouth in one image: teeth, roots, jaws and joints. You can take it in your city and send it to us."),
            ("¿Cuántos días debo quedarme?", "How many days should I stay?", "Depende del tratamiento. Con tu panorámica y la valoración te damos un plan con los días exactos.", "It depends on the treatment. With your panoramic X-ray and consultation we give you a plan with exact days."),
        ],
    },
    {
        "slug": "celulas-madre",
        "es": "Células madre", "en": "Stem Cells",
        "kicker_es": "Medicina regenerativa", "kicker_en": "Regenerative medicine",
        "resumen_es": "Terapias regenerativas que aprovechan la capacidad de tu cuerpo para reparar tejidos.",
        "resumen_en": "Regenerative therapies that harness your body's ability to repair tissue.",
        "intro_es": "La medicina regenerativa busca ayudar al cuerpo a reparar tejidos dañados usando sus propios recursos. Las células madre son células capaces de transformarse en otros tipos de células y de liberar sustancias que favorecen la reparación y disminuyen la inflamación.",
        "intro_en": "Regenerative medicine aims to help the body repair damaged tissue using its own resources. Stem cells are cells able to become other cell types and to release substances that support repair and reduce inflammation.",
        "destacado": [],
        "bloques": [
            {
                "t_es": "¿De dónde se obtienen?", "t_en": "Where do they come from?",
                "p_es": "Según el caso, pueden obtenerse de tu propio <strong>tejido graso</strong> o de la <strong>médula ósea</strong>. Se procesan y se aplican en la zona a tratar, en un procedimiento ambulatorio.",
                "p_en": "Depending on the case, they may be obtained from your own <strong>fat tissue</strong> or <strong>bone marrow</strong>. They are processed and applied to the treatment area in an outpatient procedure.",
            },
        ],
        "cards_t_es": "Áreas en las que se usa", "cards_t_en": "Areas where it is used",
        "cards_sub_es": "", "cards_sub_en": "",
        "cards": [
            ("Articulaciones", "Joints", "Desgaste de rodilla, cadera u hombro.", "Knee, hip or shoulder wear."),
            ("Tendones y ligamentos", "Tendons & ligaments", "Lesiones deportivas y de uso repetido.", "Sports and overuse injuries."),
            ("Piel y rejuvenecimiento", "Skin & rejuvenation", "Calidad de la piel, cicatrices y envejecimiento.", "Skin quality, scars and aging."),
            ("Bienestar general", "Overall wellness", "Protocolos de apoyo definidos por el médico.", "Physician-defined support protocols."),
        ],
        "incluye_es": [], "incluye_en": [],
        "nota_es": "Cada caso se evalúa de forma individual. Los resultados varían de una persona a otra y estas terapias no reemplazan los tratamientos convencionales. Se realizan bajo protocolos médicos y la normativa colombiana vigente.",
        "nota_en": "Each case is evaluated individually. Results vary from person to person and these therapies do not replace conventional treatment. They are performed under medical protocols and current Colombian regulations.",
        "faq": [
            ("¿Soy candidato?", "Am I a candidate?", "Lo define el médico en la valoración, según tu diagnóstico, tus exámenes y tu historia clínica.", "The physician decides at your consultation based on your diagnosis, tests and medical history."),
        ],
    },
    {
        "slug": "neurologia",
        "es": "Neurología", "en": "Neurology",
        "kicker_es": "Cerebro, nervios y músculos", "kicker_en": "Brain, nerves and muscles",
        "resumen_es": "Diagnóstico y tratamiento de enfermedades del cerebro, la médula, los nervios y los músculos.",
        "resumen_en": "Diagnosis and treatment of conditions of the brain, spinal cord, nerves and muscles.",
        "intro_es": "La neurología se encarga del sistema nervioso: el cerebro, la médula espinal, los nervios y los músculos. Nuestros neurólogos te ayudan a encontrar la causa de tus síntomas y a construir un plan de tratamiento claro.",
        "intro_en": "Neurology deals with the nervous system: the brain, spinal cord, nerves and muscles. Our neurologists help you find the cause of your symptoms and build a clear treatment plan.",
        "destacado": [],
        "bloques": [],
        "cards_t_es": "Qué tratamos", "cards_t_en": "What we treat",
        "cards_sub_es": "", "cards_sub_en": "",
        "cards": [
            ("Migraña y dolor de cabeza", "Migraine & headache", "Diagnóstico del tipo de cefalea y tratamiento preventivo.", "Headache diagnosis and preventive treatment."),
            ("Epilepsia", "Epilepsy", "Estudio de convulsiones y ajuste de medicamentos.", "Seizure workup and medication management."),
            ("Parkinson y temblor", "Parkinson's & tremor", "Manejo de los trastornos del movimiento.", "Management of movement disorders."),
            ("Memoria y demencias", "Memory & dementia", "Evaluación de olvidos, Alzheimer y deterioro cognitivo.", "Assessment of memory loss, Alzheimer's and cognitive decline."),
            ("Neuropatías", "Neuropathy", "Hormigueo, adormecimiento o dolor en manos y pies.", "Tingling, numbness or pain in hands and feet."),
            ("Esclerosis múltiple", "Multiple sclerosis", "Diagnóstico y seguimiento de enfermedades desmielinizantes.", "Diagnosis and follow-up of demyelinating diseases."),
            ("Mareo y vértigo", "Dizziness & vertigo", "Búsqueda de la causa y tratamiento.", "Finding the cause and treating it."),
            ("Sueño", "Sleep", "Insomnio y otros trastornos del sueño.", "Insomnia and other sleep disorders."),
            ("Después de un ACV", "After a stroke", "Prevención y seguimiento de enfermedad cerebrovascular.", "Stroke prevention and follow-up."),
        ],
        "cards2_t_es": "Estudios y procedimientos", "cards2_t_en": "Tests and procedures",
        "cards2": [
            ("Electroencefalograma", "EEG", "Registra la actividad eléctrica del cerebro.", "Records the brain's electrical activity."),
            ("Electromiografía y neuroconducción", "EMG & nerve conduction", "Evalúa el funcionamiento de nervios y músculos.", "Evaluates how nerves and muscles work."),
            ("Toxina botulínica terapéutica", "Therapeutic botulinum toxin", "Para migraña crónica y espasticidad.", "For chronic migraine and spasticity."),
            ("Orden de imágenes", "Imaging orders", "Resonancia o tomografía cuando se necesiten.", "MRI or CT scans when needed."),
        ],
        "incluye_es": [], "incluye_en": [],
        "nota_es": "Trae (o envíanos antes) tus exámenes, imágenes e historia clínica previa: así aprovechamos mejor tu valoración.",
        "nota_en": "Bring (or send us beforehand) your previous tests, imaging and medical records so we can make the most of your consultation.",
        "faq": [],
    },
    {
        "slug": "medicina-estetica",
        "es": "Medicina estética", "en": "Aesthetic Medicine",
        "kicker_es": "Resultados naturales, sin cirugía", "kicker_en": "Natural results, no surgery",
        "resumen_es": "Toxina, rellenos, bioestimuladores y tratamientos de piel para verte descansada y natural.",
        "resumen_en": "Toxin, fillers, biostimulators and skin treatments to look rested and natural.",
        "intro_es": "La medicina estética mejora tu apariencia con procedimientos mínimamente invasivos, sin cirugía y con poco o ningún tiempo de recuperación. Nuestra filosofía: que te veas como tú, en tu mejor versión.",
        "intro_en": "Aesthetic medicine improves your appearance with minimally invasive procedures, no surgery and little to no downtime. Our philosophy: you, at your best.",
        "destacado": [],
        "bloques": [],
        "cards_t_es": "Procedimientos", "cards_t_en": "Procedures",
        "cards_sub_es": "", "cards_sub_en": "",
        "cards": [
            ("Toxina botulínica", "Botulinum toxin", "Suaviza líneas de expresión de frente, entrecejo y patas de gallo.", "Softens forehead, frown and crow's-feet lines."),
            ("Ácido hialurónico", "Hyaluronic acid fillers", "Labios, ojeras, pómulos, mentón y mandíbula.", "Lips, under-eyes, cheeks, chin and jawline."),
            ("Armonización facial", "Facial harmonization", "Plan integral para equilibrar las proporciones del rostro.", "A full plan to balance facial proportions."),
            ("Bioestimuladores", "Biostimulators", "Estimulan tu propio colágeno para dar firmeza.", "Stimulate your own collagen for firmness."),
            ("Hilos tensores", "Thread lift", "Efecto lifting sin cirugía.", "A lifting effect without surgery."),
            ("Skinboosters y mesoterapia", "Skin boosters & mesotherapy", "Hidratación profunda y luminosidad.", "Deep hydration and glow."),
            ("Plasma rico en plaquetas", "Platelet-rich plasma", "Rejuvenecimiento de piel y tratamiento capilar.", "Skin rejuvenation and hair treatment."),
            ("Peelings químicos", "Chemical peels", "Manchas, textura y marcas de acné.", "Dark spots, texture and acne marks."),
            ("Láser y tecnología", "Laser & devices", "Rejuvenecimiento, manchas y depilación.", "Rejuvenation, pigmentation and hair removal."),
            ("Tratamientos corporales", "Body treatments", "Celulitis, flacidez y grasa localizada.", "Cellulite, laxity and stubborn fat."),
        ],
        "incluye_es": [], "incluye_en": [],
        "nota_es": "", "nota_en": "",
        "faq": [
            ("¿Cuánto duran los resultados?", "How long do results last?", "Depende del procedimiento: la toxina dura de 4 a 6 meses; los rellenos y bioestimuladores, de 12 a 24 meses aproximadamente.", "It depends on the procedure: toxin lasts 4–6 months; fillers and biostimulators roughly 12–24 months."),
        ],
    },
]

ICONOS = {
    "obesidad": '<path d="M12 3a4 4 0 0 1 4 4c0 3-4 5-4 5s-4-2-4-5a4 4 0 0 1 4-4Z"/><path d="M5 21c0-4 3-7 7-7s7 3 7 7"/>',
    "medicina-vascular": '<path d="M12 21s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 5.5-7 10-7 10Z"/><path d="M8 12h2l1-2 2 4 1-2h2"/>',
    "odontologia": '<path d="M7 3c-2 0-3.5 1.6-3.5 4 0 3 1.5 4.5 2 7 .4 2.3.8 7 2.5 7s1.5-5 4-5 2.3 5 4 5 2.1-4.7 2.5-7c.5-2.5 2-4 2-7 0-2.4-1.5-4-3.5-4-2.1 0-3 1.2-5 1.2S9.1 3 7 3Z"/>',
    "celulas-madre": '<circle cx="12" cy="12" r="3"/><circle cx="12" cy="12" r="8"/><circle cx="18" cy="6" r="1.2"/><circle cx="5.5" cy="16" r="1.2"/>',
    "neurologia": '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-1Z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
    "medicina-estetica": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8Z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8Z"/>',
    "cirugia-plastica": '<path d="M8 3c2 3 2 6 0 9s-2 6 0 9"/><path d="M16 3c-2 3-2 6 0 9s2 6 0 9"/>',
}


def icon(slug, size=26):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONOS[slug]}</svg>'


# ---------- Partes comunes ----------
def head(title_es, desc_es, body_cls=""):
    return f"""<!doctype html>
<html lang="es" data-lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#DCEEFB">
<title>{title_es}</title>
<meta name="description" content="{desc_es}">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500&family=Cormorant+Garamond:ital,wght@1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/estilos.css">
<script>try{{var q=new URLSearchParams(location.search).get('lang');if(q==='es'||q==='en')localStorage.setItem('aqua-lang',q);var l=localStorage.getItem('aqua-lang');if(l){{document.documentElement.dataset.lang=l;document.documentElement.lang=l;document.documentElement.classList.add('lang-chosen')}}}}catch(e){{}}</script>
</head>
<body class="{body_cls}">"""


SWITCH = """<div class="lang-switch" role="group" aria-label="Idioma / Language">
  <button type="button" data-set="es"><span class="flag">ES</span> Español</button>
  <button type="button" data-set="en"><span class="flag">EN</span> English</button>
</div>"""


def langbar():
    # franja superior: lo PRIMERO que se ve
    return f"""<div class="langbar">
  <div class="wrap langbar-in">
    <p class="langbar-q">{T("Elige tu idioma", "Choose your language")}</p>
    {SWITCH}
  </div>
</div>"""


def splash():
    return f"""<div class="splash" id="splash">
  <div class="splash-card">
    <img src="img/logo-aqua-900.png" alt="Aqua Beauty &amp; Spa" class="splash-logo">
    <p class="splash-t">Bienvenida · Welcome</p>
    <div class="splash-btns">
      <button type="button" data-set="es" data-close><small>ES</small>Español</button>
      <button type="button" data-set="en" data-close><small>EN</small>English</button>
    </div>
    <p class="splash-sub">Boston · Colombia</p>
  </div>
</div>"""


def header(activo=""):
    PRIO = ("obesidad", "cirugia-plastica")

    def cls(x):
        c = (["on"] if x["slug"] == activo else []) + (["prio"] if x["slug"] in PRIO else [])
        return f' class="{" ".join(c)}"' if c else ""
    items = "".join(f'<a href="{x["slug"]}.html"{cls(x)}>{T(x["es"], x["en"])}</a>' for x in SERVICIOS)
    return f"""{splash()}
{langbar()}
<header class="nav">
  <div class="wrap nav-in">
    <a href="index.html" class="brand"><img src="img/logo-aqua-900.png" alt="Aqua Beauty &amp; Spa"></a>
    <button class="burger" aria-label="Menú" onclick="document.body.classList.toggle('menu-open')"><i></i><i></i></button>
    <nav class="links">{items}<a href="{cta_href()}" class="btn btn-sm">{T("Agendar valoración", "Book consultation")}</a></nav>
  </div>
</header>"""


def valoracion_band():
    return f"""<section class="val">
  <div class="wrap val-in">
    <div>
      <p class="kicker">{T("Cita de valoración", "Consultation")}</p>
      <p class="val-precio">{PRECIO_VALORACION}</p>
    </div>
    <p class="val-txt">{T("Tu valoración es en nuestra sede de <strong>Colombia</strong>. Allí el especialista revisa tu caso y te entrega un plan claro con tiempos y costos.", "Your consultation takes place at our <strong>Colombia</strong> location, where the specialist reviews your case and gives you a clear plan with timing and costs.")}</p>
    <a href="{cta_href()}" class="btn">{T("Agendar valoración", "Book consultation")}</a>
  </div>
</section>"""


def footer():
    serv = "".join(f'<a href="{s["slug"]}.html">{T(s["es"], s["en"])}</a>' for s in SERVICIOS)
    contacto = []
    if WHATSAPP:
        contacto.append(f'<a href="https://wa.me/{WHATSAPP}">WhatsApp</a>')
    if EMAIL:
        contacto.append(f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    return f"""<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-brand">
      <img src="img/logo-aqua-900.png" alt="Aqua Beauty &amp; Spa">
      <p>{T("Sede en Boston · Procedimientos en Colombia", "Based in Boston · Procedures in Colombia")}</p>
    </div>
    <div class="foot-col"><p class="foot-h">{T("Servicios", "Services")}</p>{serv}</div>
    <div class="foot-col"><p class="foot-h">{T("Contacto", "Contact")}</p>{"".join(contacto) or T("Boston, MA · Colombia", "Boston, MA · Colombia")}
      <p class="foot-h" style="margin-top:18px">{T("Idioma", "Language")}</p>{SWITCH}</div>
  </div>
  <div class="wrap foot-legal">© 2026 Aqua Beauty &amp; Spa · {T("La información de este sitio es orientativa y no reemplaza la valoración médica.", "The information on this site is for guidance and does not replace a medical consultation.")}<span style="display:block;margin-top:8px">{T("Web y SEO:", "Website &amp; SEO:")} <a href="https://posicion-seo.com/">Visibla</a></span></div>
</footer>
<a href="{cta_href()}" class="mcta">{T("Agendar valoración", "Book consultation")} · {PRECIO_VALORACION}</a>
<script src="js/main.js"></script>
</body></html>"""


def contacto():
    ops = "".join(f'<option value="{x["es"]}" data-en="{x["en"]}">{x["es"]} / {x["en"]}</option>' for x in SERVICIOS)
    return f"""<section class="contacto{' con-foto' if foto('nubes') else ''}" id="contacto">
  {NUBES}
  <form class="glass" id="form-contacto" data-wa="{WHATSAPP}" data-mail="{EMAIL}">
    <h2>{T("Empieza tu viaje hoy", "Begin your journey today")}</h2>
    <p>{T("Elige tu idioma y habla con nuestros especialistas desde cualquier lugar del mundo.", "Choose your language and connect with our specialists from anywhere in the world.")}</p>
    <input name="nombre" required placeholder="Nombre · Name">
    <input name="tel" required type="tel" placeholder="Teléfono · Phone">
    <select name="idioma"><option value="Español">Español</option><option value="English">English</option></select>
    <select name="servicio"><option value="">{'Servicio de interés · Service'}</option>{ops}</select>
    <button class="btn" type="submit">{T("Agendar valoración", "Book consultation")} · {PRECIO_VALORACION}</button>
    <p class="form-pend form-msg" hidden>{T("Muy pronto habilitamos el agendamiento en línea. Gracias por tu paciencia.", "Online booking opens very soon. Thank you for your patience.")}</p>
    <p class="form-ok form-msg" hidden>{T("¡Gracias! Te contactaremos muy pronto.", "Thank you! We'll contact you shortly.")}</p>
  </form>
</section>"""


SEDE = [
    ("s-entrada", "Recepción", "Reception", "wide"),
    ("recepcion-1", "Recepción", "Reception", ""),
    ("s-consultorio", "Consultorio con vista a la ciudad", "Doctor's office with city views", "wide"),
    ("consultorio", "Consultorio", "Doctor's office", ""),
    ("cabina-2", "Sala de procedimientos", "Treatment room", ""),
    ("s-cabina", "Sala de tratamientos corporales", "Body treatment room", "wide"),
    ("sala-espera", "Sala de espera", "Waiting room", ""),
    ("s-recepcion", "Recepción", "Reception", "wide"),
    ("vista-1", "La vista desde nuestra sede", "The view from our clinic", ""),
    ("cabina-1", "Sala de procedimientos", "Treatment room", ""),
    ("recepcion-2", "Recepción", "Reception", ""),
    ("pasillo", "Consultorios privados", "Private rooms", ""),
    ("vista-2", "Rodeados de verde y montañas", "Surrounded by green and mountains", ""),
]


def galeria():
    fotos = "".join(f'''<figure class="g-item bw {w}"><img src="img/sede/{f}-sm.jpg" alt="" loading="lazy" decoding="async"><figcaption>{T(a, b)}</figcaption></figure>''' for f, a, b, w in SEDE)
    puntos = [("Consultorios privados", "Private doctor's offices"), ("Salas de procedimientos equipadas", "Fully equipped treatment rooms"),
              ("Tecnología de última generación", "State-of-the-art technology"), ("Espacios luminosos con vista a la ciudad", "Bright spaces with city views")]
    return f"""<section class="sede" id="instalaciones">
  <div class="wrap sede-intro">
    <div>
      <p class="kicker">{T("Instalaciones en Colombia", "Our facilities in Colombia")}</p>
      <h2>{T("Así es el lugar<br>donde te vamos a cuidar", "This is where<br>we'll take care of you")}</h2>
    </div>
    <div class="sede-txt">
      <p>{T("Nuestras instalaciones en Colombia fueron pensadas para que te sientas en casa desde que llegas: espacios modernos, limpios y tranquilos, con todo lo necesario para tu valoración, tus procedimientos y tu recuperación.", "Our facilities in Colombia were designed so you feel at home from the moment you arrive: modern, clean and calm spaces with everything you need for your consultation, procedures and recovery.")}</p>
      <ul class="sede-pts">{"".join(f"<li>{T(x, y)}</li>" for x, y in puntos)}</ul>
    </div>
  </div>
  <div class="wrap g-bar">
    <p class="g-hint">{T("Pasa el mouse para verlas a color", "Hover to see them in color")}</p>
    <div class="g-nav">
      <button type="button" class="g-btn" data-dir="-1" aria-label="Anterior">←</button>
      <button type="button" class="g-btn" data-dir="1" aria-label="Siguiente">→</button>
    </div>
  </div>
  <div class="g-track">{fotos}</div>
</section>"""


# ---------- Portada ----------
def index():
    top = [x for x in SERVICIOS if x["slug"] in ("obesidad", "cirugia-plastica")]
    otros = [x for x in SERVICIOS if x not in top]
    puntos = {
        "obesidad": [("Tirzepatida bajo control médico", "Physician-supervised tirzepatide"), ("5 especialistas, 2 citas con cada uno", "5 specialists, 2 visits each"), ("Programa completo de 4 meses", "Complete 4-month program")],
        "cirugia-plastica": [("Rostro, senos y cuerpo", "Face, breasts and body"), ("Cirujanos plásticos certificados", "Certified plastic surgeons"), ("Recuperación acompañada en Colombia", "Supported recovery in Colombia")],
    }
    feat = "".join(f"""<article class="feat">
      {media(x['slug'], 'feat-media bw')}
      <div class="feat-body">
        <span class="badge">{T("Más solicitado", "Most requested")}</span>
        <h3>{T(x['es'], x['en'])}</h3>
        <p>{T(x['resumen_es'], x['resumen_en'])}</p>
        <ul class="feat-list">{"".join(f"<li>{T(a, b)}</li>" for a, b in puntos[x['slug']])}</ul>
        <div class="feat-cta">
          <a href="{x['slug']}.html" class="btn">{T("Ver todo", "See details")}</a>
          <a href="{cta_href()}" class="btn btn-ghost">{T("Agendar valoración", "Book consultation")}</a>
        </div>
      </div>
    </article>""" for x in top)

    cards = "".join(f"""<a class="scard" href="{s['slug']}.html">
      {media(s['slug'], 'scard-media')}
      <div class="scard-body">
        <h3>{T(s['es'], s['en'])}</h3>
        <p>{T(s['resumen_es'], s['resumen_en'])}</p>
        <span class="more">{T("Ver más", "Learn more")} <i>↗</i></span>
      </div>
    </a>""" for s in otros)

    pasos = [
        ("Escríbenos desde Estados Unidos", "Reach out from the U.S.", "Te atendemos en español o inglés y resolvemos tus dudas antes de viajar.", "We assist you in English or Spanish and answer your questions before you travel."),
        ("Planeamos tu viaje médico", "We plan your medical trip", "Te decimos qué exámenes traer y cuántos días quedarte en Colombia.", "We tell you which tests to bring and how many days to stay in Colombia."),
        ("Valoración en Colombia", "Consultation in Colombia", f"Tu cita de valoración cuesta {PRECIO_VALORACION}. El especialista define tu plan.", f"Your consultation costs {PRECIO_VALORACION}. The specialist defines your plan."),
        ("Tratamiento y seguimiento", "Treatment & follow-up", "Te acompañamos durante el procedimiento y después, cuando regresas a casa.", "We support you during treatment and after you return home."),
    ]
    pasos_html = "".join(f"""<li><span class="n">{i+1}</span><h3>{T(a, b)}</h3><p>{T(c, d)}</p></li>""" for i, (a, b, c, d) in enumerate(pasos))

    return head("Aqua Beauty & Spa · Boston – Colombia", "Clínica con sede en Boston y procedimientos en Colombia: obesidad, medicina vascular, odontología, células madre, neurología, medicina estética y cirugía plástica.") + header() + f"""
<main>
<section class="hero">
  {NUBES}
  <div class="wrap hero-in">
    <div class="hero-txt">
      <p class="kicker">{T("Boston · Colombia", "Boston · Colombia")}</p>
      <h1>{T("<span class='thin'>Desde Boston,</span><br>ven a cuidarte<br><span class='thin'>en</span> <span class='acc'>Colombia</span>", "<span class='thin'>From Boston,</span><br>come heal<br><span class='thin'>in</span> <span class='acc'>Colombia</span>")}</h1>
      <p class="lead">{T("Somos una clínica con sede en Boston y procedimientos en nuestra sede de Colombia. Especialistas certificados, atención en tu idioma y acompañamiento en cada paso.", "We are a Boston-based clinic with procedures at our Colombia location. Certified specialists, care in your language and support at every step.")}</p>
      <div class="hero-cta">
        <a href="{cta_href()}" class="btn">{T("Agendar valoración", "Book consultation")}</a>
        <a href="#servicios" class="btn btn-ghost">{T("Ver servicios", "See services")}</a>
      </div>
      <div class="hero-quick">
        <span>{T("Lo más buscado:", "Most popular:")}</span>
        <a href="obesidad.html">{T("Programa de obesidad", "Weight-loss program")}</a>
        <a href="cirugia-plastica.html">{T("Cirugía plástica", "Plastic surgery")}</a>
      </div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <div class="arch">{('<img class="arch-photo" src="img/hero.jpg" srcset="img/hero-sm.jpg 700w, img/hero.jpg 1100w" sizes="(max-width: 820px) 60vw, 30vw" alt="" fetchpriority="high">' if foto("hero") else '<img class="arch-logo" src="img/logo-aqua-900.png" alt="">')}</div>
      <div class="chip c1">{T("Valoración", "Consultation")} · {PRECIO_VALORACION}</div>
      <div class="chip c2">{T("7 especialidades", "7 specialties")}</div>
    </div>
  </div>
</section>

<section class="top" id="destacados">
  <div class="wrap">
    <p class="kicker center">{T("Lo más elegido", "Our most chosen")}</p>
    <h2 class="center">{T("Nuestros programas estrella", "Our signature programs")}</h2>
    <div class="feat-grid">{feat}</div>
  </div>
</section>

<section class="alianza" id="alianza">
  <div class="wrap alianza-in">
    <div>
      <p class="kicker">{T("Nuestra alianza", "Our partnership")}</p>
      <h2>{T("Una clínica en Boston.<br>Tu tratamiento en Colombia.", "A clinic in Boston.<br>Your treatment in Colombia.")}</h2>
      <div class="alianza-foto bw"><img src="img/sede/recepcion-2.jpg" alt="" loading="lazy"></div>
    </div>
    <div class="alianza-txt">
      {B("<p>Nuestra sede principal está en <strong>Boston</strong>. Desde allí te orientamos, resolvemos tus dudas y organizamos tu viaje. Los procedimientos los realizamos en nuestra <strong>sede de Colombia</strong>, con especialistas certificados y tecnología de primer nivel.</p><p>Así tienes lo mejor de los dos lados: la cercanía y la confianza de una clínica en Estados Unidos, y la calidad médica, la calidez y los costos de Colombia.</p>",
         "<p>Our main office is in <strong>Boston</strong>. From there we guide you, answer your questions and organize your trip. Procedures are performed at our <strong>Colombia location</strong>, with certified specialists and first-class technology.</p><p>You get the best of both worlds: the closeness and trust of a U.S. clinic, and the medical quality, warmth and pricing of Colombia.</p>")}
      <ul class="pros">
        <li>{T("Atención en español e inglés", "Care in English and Spanish")}</li>
        <li>{T("Especialistas certificados", "Certified specialists")}</li>
        <li>{T("Costos más accesibles", "More affordable pricing")}</li>
        <li>{T("Acompañamiento antes, durante y después", "Support before, during and after")}</li>
      </ul>
    </div>
  </div>
</section>

{galeria()}

<section class="servicios" id="servicios">
  <div class="wrap">
    <p class="kicker center">{T("Más especialidades", "More specialties")}</p>
    <h2 class="center">{T("Ven a nuestra sede de Colombia", "Come to our Colombia location")}</h2>
    <div class="sgrid">{cards}</div>
  </div>
</section>

<section class="pasos">
  <div class="wrap">
    <p class="kicker center">{T("Cómo funciona", "How it works")}</p>
    <h2 class="center">{T("Cuatro pasos, de Boston a Colombia", "Four steps, from Boston to Colombia")}</h2>
    <ol class="plist">{pasos_html}</ol>
  </div>
</section>

{valoracion_band()}

{contacto()}
</main>""" + footer()


# ---------- Página de servicio ----------
def servicio(s):
    dest = ""
    if s.get("destacado"):
        dest = '<div class="stats">' + "".join(
            f'<div><b>{n}</b><span>{T(a, b)}</span></div>' for n, a, b in s["destacado"]) + "</div>"

    aviso = ""
    if s.get("aviso_es"):
        aviso = f'<div class="aviso wrap"><span class="aviso-ic">!</span>{B("<p>" + s["aviso_es"] + "</p>", "<p>" + s["aviso_en"] + "</p>")}</div>'

    bloques = "".join(f"""<div class="bloque">
      <h2>{T(b['t_es'], b['t_en'])}</h2>
      {B('<p>' + b['p_es'] + '</p>', '<p>' + b['p_en'] + '</p>')}
    </div>""" for b in s["bloques"])

    def grid(titulo_es, titulo_en, sub_es, sub_en, items):
        if not items:
            return ""
        sub = f'<p class="sub center">{T(sub_es, sub_en)}</p>' if sub_es else ""
        cs = "".join(f'<div class="card"><h3>{T(a, b)}</h3><p>{T(c, d)}</p></div>' for a, b, c, d in items)
        return f'<section class="cards"><div class="wrap"><h2 class="center">{T(titulo_es, titulo_en)}</h2>{sub}<div class="cgrid">{cs}</div></div></section>'

    cards = grid(s["cards_t_es"], s["cards_t_en"], s["cards_sub_es"], s["cards_sub_en"], s["cards"])
    cards2 = grid(s.get("cards2_t_es", ""), s.get("cards2_t_en", ""), "", "", s.get("cards2", []))

    pasos = ""
    if s.get("pasos"):
        li = "".join(f'<li><span class="n">{i+1}</span><div><h3>{T(a, b)}</h3><p>{T(c, d)}</p></div></li>' for i, (a, b, c, d) in enumerate(s["pasos"]))
        pasos = f'<section class="timeline"><div class="wrap"><h2 class="center">{T(s["pasos_t_es"], s["pasos_t_en"])}</h2><ol class="tl">{li}</ol><div class="center tl-cta"><a href="{cta_href()}" class="btn">{T("Agendar valoración", "Book consultation")} · {PRECIO_VALORACION}</a></div></div></section>'

    grupos = ""
    if s.get("grupos"):
        cols = "".join(f"""<div class="grupo"><h3>{T(ge, gn)}</h3><ul>{"".join(f"<li>{T(a, b)}</li>" for a, b in items)}</ul></div>""" for ge, gn, items in s["grupos"])
        grupos = f'<section class="cards"><div class="wrap"><h2 class="center">{T("Procedimientos", "Procedures")}</h2><div class="ggrid">{cols}</div></div></section>'

    incluye = ""
    if s["incluye_es"]:
        li_es = "".join(f"<li>{x}</li>" for x in s["incluye_es"])
        li_en = "".join(f"<li>{x}</li>" for x in s["incluye_en"])
        incluye = f"""<section class="incluye"><div class="wrap incluye-in">
      <h2>{T("Qué incluye", "What's included")}</h2>
      {B(li_es, li_en, tag="ul", cls="check")}
    </div></section>"""

    nota = f'<div class="wrap"><p class="nota">{T(s["nota_es"], s["nota_en"])}</p></div>' if s["nota_es"] else ""

    faq = ""
    if s["faq"]:
        qs = "".join(f"<details><summary>{T(a, b)}</summary><p>{T(c, d)}</p></details>" for a, b, c, d in s["faq"])
        faq = f'<section class="faq"><div class="wrap faq-in"><h2>{T("Preguntas frecuentes", "FAQ")}</h2>{qs}</div></section>'

    return head(f"{s['es']} · Aqua Beauty & Spa", s["resumen_es"], "prio" if s["slug"] in ("obesidad", "cirugia-plastica") else "") + header(s["slug"]) + f"""
<main>
<section class="shero">
  {NUBES}
  <div class="wrap shero-in">
   <div class="shero-txt">
    <a href="index.html#servicios" class="back">← {T("Todos los servicios", "All services")}</a>
    <span class="shero-ic">{icon(s['slug'], 34)}</span>
    <p class="kicker">{T(s['kicker_es'], s['kicker_en'])}</p>
    <h1>{T(s['es'], s['en'])}</h1>
    {B('<p class="lead">' + s['intro_es'] + '</p>', '<p class="lead">' + s['intro_en'] + '</p>')}
    <p class="pill-loc">{T("En nuestra sede de Colombia", "At our Colombia location")} · {T("Valoración", "Consultation")} {PRECIO_VALORACION}</p>
    {dest}
   </div>
   {media(s['slug'], 'arch arch-s')}
  </div>
</section>
{aviso}
{('<section class="bloques"><div class="wrap bloques-in">' + bloques + '</div></section>') if bloques else ''}
{cards}
{grupos}
{cards2}
{pasos}
{incluye}
{nota}
{faq}
{valoracion_band()}
{contacto()}
</main>""" + footer()


def main():
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index())
    for s in SERVICIOS:
        with open(os.path.join(ROOT, s["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(servicio(s))
    print("OK:", 1 + len(SERVICIOS), "páginas")


if __name__ == "__main__":
    main()
