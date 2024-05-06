from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Словарь для хранения текста на разных языках
texts = {
    'ru': {
        'title': 'Главная страница',
        'header': 'Медицинская справочная информация',
        'jumbotron_header': 'Мигрень — что делать и к кому обращаться?',
        'whatis_header': 'Что такое мигрень?',
        'whatis_text': 'Мигрень - это серьезное неврологическое заболевание, характеризующееся рецидивирующими приступами интенсивной головной боли. Это состояние может сильно нарушать обычный образ жизни человека, ограничивая его в повседневных занятиях и работе.',
        'characteristics_header': 'Характер боли',
        'characteristics_text': 'Основным симптомом мигрени является сильная, пульсирующая головная боль, часто сосредотачивающаяся в одной стороне головы. Боль чаще всего усиливается при физических нагрузках или при воздействии света и шума. У многих пациентов также могут наблюдаться тошнота, рвота, чувство слабости и чувствительность к свету и звуку.',
        'symptoms_header': 'Симптомы',
        'symptoms_text': 'Симптомы мигрени могут включать:',
        'symptoms_list': [
            'Интенсивную головную боль, часто локализующуюся в одной половине головы',
            'Тошноту и рвоту, особенно во время приступа мигрени',
            'Чувствительность к свету и звуку, которая может усугубиться во время приступа',
            'Ауры, такие как зрительные или сенсорные изменения'
        ],
        'when_to_see_doctor_header': 'Когда обращаться к врачу',
        'when_to_see_doctor_text': 'Обращение к врачу рекомендуется в следующих случаях:',
        'when_to_see_doctor_list': [
            'Если частота и интенсивность приступов мигрени значительно увеличивается',
            'Если мигрень начинается впервые после 50 лет',
            'Если мигрень сопровождается изменениями в зрении, слухе или сенсорных ощущениях',
            'Если мигрень значительно влияет на повседневную жизнь и работу'
        ],
        'specialists_header': 'Какие врачи лечат мигрень',
        'specialists_text': 'Лечение мигрени может включать консультации и сотрудничество с различными специалистами, в зависимости от индивидуальных потребностей пациента и тяжести его состояния. Вот несколько специалистов, которые могут быть вовлечены в лечение мигрени:',
        'specialists_list': [
            'Невролог или неврологический специалист',
            'Терапевт',
            'Неврологический аллерголог',
            'Психиатр или психотерапевт',
            'Физиотерапевт',
            'Офтальмолог'
        ],
        'clinic_header': 'Университетская клиника КФУ:',
        'clinic_text': 'Адрес: 420043, Республика Татарстан, г. Казань, ул. Чехова, 1A',
        'polyclinic_header': 'Поликлиника по прописке:',
        'polyclinic_text': 'Студенты также могут обратиться в местную поликлинику, указанную в их медицинской карте по месту жительства или прописке. В этих поликлиниках оказываются широкий спектр медицинских услуг, включая профилактику, диагностику и лечение различных заболеваний.',
        'contact_form_label': 'Форма связи',
        'send_button': 'Отправить',
        'thanks_message': 'Спасибо за ваше сообщение!',
        'change_language': 'Изменить язык на английский',
        'current_language': 'en',
    },
    'en': {
        'title': 'Homepage',
        'header': 'Medical Reference Information',
        'jumbotron_header': 'Migraine - What to do and where to go?',
        'whatis_header': 'What is migraine?',
        'whatis_text': 'Migraine is a serious neurological condition characterized by recurrent episodes of intense headache. This condition can significantly disrupt a person\'s normal lifestyle, limiting them in everyday activities and work.',
        'characteristics_header': 'Characteristics of pain',
        'characteristics_text': 'The main symptom of migraine is a severe, pulsating headache, often focused on one side of the head. The pain is most often intensified during physical exertion or exposure to light and noise. Many patients may also experience nausea, vomiting, weakness, and sensitivity to light and sound.',
        'symptoms_header': 'Symptoms',
        'symptoms_text': 'Symptoms of migraine may include:',
        'symptoms_list': [
            'Intense headache, often localized on one side of the head',
            'Nausea and vomiting, especially during a migraine attack',
            'Sensitivity to light and sound, which can worsen during an attack',
            'Auras, such as visual or sensory changes'
        ],
        'when_to_see_doctor_header': 'When to see a doctor',
        'when_to_see_doctor_text': 'Seeking medical attention is recommended in the following cases:',
        'when_to_see_doctor_list': [
            'If the frequency and intensity of migraine attacks significantly increase',
            'If migraine starts for the first time after age 50',
            'If migraine is accompanied by changes in vision, hearing, or sensory perceptions',
            'If migraine significantly affects daily life and work'
        ],
        'specialists_header': 'What doctors treat migraine',
        'specialists_text': 'Migraine treatment may involve consultations and collaboration with various specialists, depending on the individual needs of the patient and the severity of their condition. Here are a few specialists who may be involved in migraine treatment:',
        'specialists_list': [
            'Neurologist or neurological specialist',
            'General practitioner',
            'Neurological allergist',
            'Psychiatrist or psychotherapist',
            'Physiotherapist',
            'Ophthalmologist'
        ],
        'clinic_header': 'KFU University Clinic:',
        'clinic_text': 'Address: 420043, Republic of Tatarstan, Kazan, Chekhova St., 1A',
        'polyclinic_header': 'Residence-based polyclinic:',
        'polyclinic_text': 'Students can also contact the local polyclinic indicated in their medical card by place of residence or registration. These polyclinics provide a wide range of medical services, including prevention, diagnosis, and treatment of various diseases.',
        'contact_form_label': 'Contact Form',
        'send_button': 'Send',
        'thanks_message': 'Thank you for your message!',
        'change_language': 'Change language to Russian',
        'current_language': 'ru',
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
