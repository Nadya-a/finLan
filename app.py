from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Словарь для хранения текста на разных языках
texts = {
    'ru': {
        'title': 'Главная страница',
        'header': 'Медицинская справочная информация',
        'jumbotron_header': 'Мигрень — что делать и к кому обращаться?',
        'whatis_header': 'Что такое мигрень?',
        'whatis_text1': 'Мигрень - это серьезное неврологическое заболевание, характеризующееся рецидивирующими приступами интенсивной головной боли. '
                        'Это состояние может сильно нарушать обычный образ жизни человека, ограничивая его в повседневных занятиях и работе.',
        'whatis_text2': 'На развитие мигрени влияет наследственная предрасположенность, а также множество причин и провокаторов. Все они приводят к локальному расширению сосудов малого калибра и раздражению окончаний ветвей тройничного нерва медиаторами боли.',
        'whatis_reasons': 'Причины мигрени могут включать генетические факторы, изменения в мозге и окружающей среде, такие как стресс, изменения в погоде, неправильное питание, недостаток сна и другие. Мигрень может значительно повлиять на качество жизни, поэтому важно обращаться к врачу для диагностики и лечения.',
        'characteristics_header': 'Характер боли',
        'characteristics_text': 'Основным симптомом мигрени является сильная, пульсирующая головная боль, часто сосредотачивающаяся в одной стороне головы. Боль чаще всего усиливается при физических нагрузках или при воздействии света и шума. У многих пациентов также могут наблюдаться тошнота, рвота, чувство слабости и чувствительность к свету и звуку.',
        'characteristics_end': 'Боли при мигрени могут быть настолько интенсивными, что они могут ограничивать повседневные активности и требовать от пациента принятия мер по смягчению симптомов, включая прием лекарств и отдых в темной, тихой комнате.',
        'symptoms_header': 'Симптомы',
        'symptoms_text': 'Мигрень - это серьезное неврологическое заболевание, характеризующееся пароксизмальными приступами головной боли, которая часто сопровождается различными симптомами. Вот некоторые из типичных симптомов мигрени:',
        'symptoms_list': [
            {
                'name': 'Интенсивная головная боль',
                'description': 'Головная боль при мигрени обычно является сильной и может быть локализована в одной стороне головы. Это может быть пульсирующая боль, чувствуемая в висках, лбу или вокруг глаз. Интенсивность боли может быть настолько высокой, что она мешает выполнению повседневных задач.'
            },
            {
                'name': 'Тошнота и рвота',
                'description': 'Многие люди, страдающие от мигрени, также испытывают тошноту и рвоту во время приступа. Это связано с активацией чувствительных участков в мозге, которые контролируют тошноту и рвоту. Эти симптомы могут усугубить дискомфорт во время приступа мигрени.'
            },
            {
                'name': 'Чувствительность к свету и звуку',
                'description': 'Многие люди с мигренью становятся чрезмерно чувствительными к яркому свету и громким звукам во время приступа. Это может ухудшить уже сильную головную боль и вызвать дополнительный дискомфорт.'
            },
            {
                'name': 'Ауры',
                'description': 'Ауры - это временные изменения в ощущениях, зрении или других чувствах, которые могут предшествовать приступу мигрени или сопровождать его. Зрительные ауры могут включать мерцающие световые пятна, искажения или потерю зрения на некоторое время. Сенсорные ауры могут включать покалывание или онемение в определенных частях тела.'
            }
        ],
        'symptoms_end': 'Это лишь некоторые из возможных симптомов мигрени, и они могут варьироваться от человека к человеку и от приступа к приступу. Если у вас есть подозрение на мигрень или вы столкнулись с подобными симптомами, важно обратиться к врачу для точного диагноза и лечения.',
        'when_to_see_doctor_header': 'Когда обращаться к врачу',
        'when_to_see_doctor_text': 'Обращение к врачу рекомендуется в следующих случаях:',
        'when_to_see_doctor_list': [
            '1. Если частота и интенсивность приступов мигрени значительно увеличивается',
            '2. Если мигрень начинается впервые после 50 лет',
            '3. Если мигрень сопровождается изменениями в зрении, слухе или сенсорных ощущениях',
            '4. Если мигрень значительно влияет на повседневную жизнь и работу'
        ],
        'specialists_header': 'Какие врачи лечат мигрень',
        'specialists_text': 'Лечение мигрени может включать консультации и сотрудничество с различными специалистами, в зависимости от индивидуальных потребностей пациента и тяжести его состояния. Вот несколько специалистов, которые могут быть вовлечены в лечение мигрени:',
        'specialists_list': [
            '1. Невролог или неврологический специалист',
            '2. Терапевт',
            '3. Неврологический аллерголог',
            '4. Психиатр или психотерапевт',
            '5. Физиотерапевт',
            '6. Офтальмолог'
        ],
        'clinic_av': 'Доступные студентам клиники',
        'clinic_header': 'Университетская клиника КФУ',
        'clinic_text': 'Адрес: 420043, Республика Татарстан, г. Казань, ул. Чехова, 1A',
        'clinic_phone': 'Телефон для связи: +7 (843) 233-30-00',
        'polyclinic_header': 'Поликлиника по прописке',
        'polyclinic_text': 'Студенты также могут обратиться в местную поликлинику, указанную в их медицинской карте по месту жительства или прописке. В этих поликлиниках оказываются широкий спектр медицинских услуг, включая профилактику, диагностику и лечение различных заболеваний.',
        'form_info': 'Если у Вас остались вопросы, вы можете обратиться в наше справочное бюро для более подробной консультации. Для этого заполните форму ниже:',
        'contact_form_label': 'Форма связи',
        'send_button': 'Отправить',
        'thanks_message': 'Спасибо за ваше сообщение!',
        'change_language': 'Switch to English',
        'current_language': 'en',
        'contact_me': 'Связаться со мной',
        'name': 'Имя:',
        'email': 'Адрес электронной почты:',
        'message': 'Сообщение:',
        'send': 'Отправить',
    },
    'en': {
        'title': 'Home Page',
        'header': 'Medical Reference Information',
        'jumbotron_header': 'Migraine - What to Do and Where to GO?',
        'whatis_header': 'What is Migraine?',
        'whatis_text1': 'Migraine is a serious neurological condition characterized by recurrent episodes of intense headaches. This condition can significantly disrupt a person\'s normal lifestyle, limiting them in their daily activities and work.',
        'whatis_text2': 'The development of migraines is influenced by genetic predisposition, as well as numerous causes and triggers. All of these lead to localized dilation of small-caliber vessels and irritation of the endings of the trigeminal nerve branches by pain mediators.',
        'whatis_reasons': 'Causes of migraines may include genetic factors, changes in the brain and the environment, such as stress, weather changes, improper diet, lack of sleep, and others. Migraine can significantly impact quality of life, so it is important to consult a doctor for diagnosis and treatment.',
        'characteristics_header': 'Pain Characteristics',
        'characteristics_text': 'The primary symptom of migraine is a severe, throbbing headache, often concentrated on one side of the head. The pain is usually exacerbated by physical exertion or exposure to light and noise. Many patients also experience nausea, vomiting, weakness, and sensitivity to light and sound.',
        'characteristics_end': 'Migraine pain can be so intense that it can limit daily activities and require the patient to take measures to alleviate symptoms, including taking medication and resting in a dark, quiet room.',
        'symptoms_header': 'Symptoms',
        'symptoms_text': 'Migraine is a serious neurological condition characterized by paroxysmal episodes of headache, which are often accompanied by various symptoms. Here are some of the typical symptoms of migraines:',
        'symptoms_list': [
            {
                'name': 'Intense Headache',
                'description': 'Headache during a migraine is usually severe and can be localized on one side of the head. It can be a throbbing pain felt in the temples, forehead, or around the eyes. The intensity of the pain can be so high that it interferes with daily tasks.'
            },
            {
                'name': 'Nausea and Vomiting',
                'description': 'Many people suffering from migraines also experience nausea and vomiting during an attack. This is associated with the activation of sensitive areas in the brain that control nausea and vomiting. These symptoms can exacerbate discomfort during a migraine attack.'
            },
            {
                'name': 'Sensitivity to Light and Sound',
                'description': 'Many people with migraines become excessively sensitive to bright light and loud noises during an attack. This can worsen already severe headaches and cause additional discomfort.'
            },
            {
                'name': 'Auras',
                'description': 'Auras are temporary changes in sensations, vision, or other feelings that may precede or accompany a migraine attack. Visual auras may include flickering lights, distortions, or temporary loss of vision. Sensory auras may include tingling or numbness in certain parts of the body.'
            }
        ],
        'symptoms_end': 'These are just some of the possible symptoms of migraines, and they can vary from person to person and from attack to attack. If you suspect migraine or experience similar symptoms, it is important to consult a doctor for an accurate diagnosis and treatment.',
        'when_to_see_doctor_header': 'When to See a Doctor',
        'when_to_see_doctor_text': 'Seeing a doctor is recommended in the following cases:',
        'when_to_see_doctor_list': [
            '1. If the frequency and intensity of migraine attacks significantly increase',
            '2. If migraines begin for the first time after the age of 50',
            '3. If migraines are accompanied by changes in vision, hearing, or sensory sensations',
            '4. If migraines significantly affect daily life and work'
        ],
        'specialists_header': 'Which Doctors Treat Migraine',
        'specialists_text': 'Migraine treatment may involve consultations and collaboration with various specialists, depending on the individual needs of the patient and the severity of their condition. Here are several specialists who may be involved in migraine treatment:',
        'specialists_list': [
            '1. Neurologist or neurological specialist',
            '2. General practitioner',
            '3. Neurological allergist',
            '4. Psychiatrist or psychotherapist',
            '5. Physiotherapist',
            '6. Ophthalmologist'
        ],
        'clinic_av': 'Available Clinics for Students',
        'clinic_header': 'KFU University Clinic',
        'clinic_text': 'Address: 420043, Republic of Tatarstan, Kazan, Chekhova St., 1A',
        'clinic_phone': 'Contact Phone: +7 (843) 233-30-00',
        'polyclinic_header': 'Local Polyclinic',
        'polyclinic_text': 'Students can also visit the local polyclinic indicated in their medical record by place of residence or registration. These polyclinics provide a wide range of medical services, including prevention, diagnosis, and treatment of various diseases.',
        'form_info': 'If you have any questions, you can contact our information desk for more detailed consultation. To do this, fill out the form below:',
        'contact_form_label': 'Contact Form',
        'send_button': 'Send',
        'thanks_message': 'Thank you for your message!',
        'change_language': 'Switch to Russian',
        'current_language': 'ru',
        'contact_me': 'Contact me',
        'name': 'Name:',
        'email': 'Email address:',
        'message': 'Message:',
        'send': 'Send',
    }
}


@app.route('/')
def index():
    # Определяем язык на основе параметра языка в URL
    lang = request.args.get('lang', 'ru')
    text = texts.get(lang, texts['ru'])
    return render_template('index.html', **text)

@app.route('/contact', methods=['POST'])
def contact():
    # Обработка формы связи
    # Действия по обработке отправленной формы
    return 'Спасибо за ваше сообщение!'

@app.route('/<lang>')
def change_language(lang):
    # Перенаправляем на главную страницу с новым языком
    return redirect(url_for('index', lang=lang))

if __name__ == '__main__':
    app.run(debug=True)
