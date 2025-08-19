INSERT INTO s12.rbprinttemplate (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, code, name, context,
                                 fileName, `default`, dpdAgreement, type, inAmbCard, banUnkeptDate, counter_id, deleted,
                                 isPatientAgreed, hideParam, documentType_id, groupName, isEditableInWeb, chkProfiles,
                                 chkPersons, pageOrientation, sendMail, leftMargin, printTemplateType_id)
VALUES ('2023-06-21 12:06:04', null, '2023-06-21 12:06:09', null, 'pay_q_cont', 'Контроль качества', 'pay_q_control',
        ' ',
'<!-- изменил Пулин дата 21.07.2025 задача  -->
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Контроль качества</title>
  <style>
    .main {
        font-family: ''Arial'';
        font-size: 11pt;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    .center {
        text-align: center;
    }
    .header {
        text-align: center;
        font-weight: bold;
    }
    .white-wrap {
      white-space: nowrap;
    }
  </style>
</head>
<body>

<div class="main">
  <div class="header">
    {{ context.client_fio }}<br>
    № амб.карты {{ context.client_id }}
  </div>
  <br>

  <!-- Первичный осмотр -->
  <section>
    <div class="header">Первичный осмотр</div>
    <div class="header">Дата {{ context.first_act.beg_date }}</div>

    <div>Перенесенные и сопутствующие заболевания: {{ context.first_act.accompDiseases or ''не указаны'' }}</div>
    <div>Данные объективного исследования:</div>
    <div>Внешний осмотр: {{ context.first_act.apsInpection or ''не указано'' }}</div>

    <div align="center">
      {% if context.is_deciduous %}
          Молочные зубы
      {% else %}
          Постоянные зубы
      {% endif %}
    </div>


    <h2>{{context.first_act.top}}</h2>
    <!-- Таблица зубов -->
    <table width="100%" cellpadding="2" cellspacing="0">
      <!-- Верхние зубы -->
      <tr>
        <td class="center">Статус</td>
        {% for tooth in context.first_act.top %}
          <td class="center">{{ tooth.status or '''' }}</td>
        {% endfor %}
      </tr>
      <tr>
        <td class="center">Пародонтит, подвижность</td>
        {% for tooth in context.first_act.top %}
          <td class="center">{{ tooth.move or '''' }}</td>
        {% endfor %}
      </tr>
      <tr>
        <td class="center">Состояние</td>
        {% for tooth in context.first_act.top %}
          <td class="center">{{ tooth.condition or '''' }}</td>
        {% endfor %}
      </tr>
      <tr>
        <td class="center">Верх</td>
        {% for tooth in context.first_act.top %}
          <td class="center">{{ tooth.number or '''' }}</td>
        {% endfor %}
      </tr>

      <!-- Нижние зубы -->
      <tr>
        <td class="center">Низ</td>
        {% for tooth in context.first_act.bottom %}
          <td class="center">{{ tooth.number or '''' }}</td>
        {% endfor %}
      </tr>
      <tr>
        <td class="center">Состояние</td>
        {% for tooth in context.first_act.bottom %}
          <td class="center">{{ tooth.condition or '''' }}</td>
        {% endfor %}
      </tr>
      <tr>
        <td class="center">Статус</td>
        {% for tooth in context.first_act.bottom %}
          <td class="center">{{ tooth.status or '''' }}</td>
        {% endfor %}
      </tr>
      <tr>
        <td class="center">Пародонтит, подвижность</td>
        {% for tooth in context.first_act.bottom %}
          <td class="center">{{ tooth.move or '''' }}</td>
        {% endfor %}
      </tr>
    </table>

    <br>

    <div>Прикус: {{ context.first_act.beet or ''не указан'' }}</div>
    <div>Состояние слизистой оболочки полости рта, десен, альвеолярных отростков и неба: {{ context.first_act.oralCondition or ''не указано'' }}</div>
    <div>Состояние слюнных желез: {{ context.first_act.glandCondition or ''не указано'' }}</div>
    <div>Состояние лимфоузлов: {{ context.first_act.lymphNodes or ''не указано'' }}</div>
    <div>Данные рентгеновских, лабораторных исследований: {{ context.first_act.researchData or ''нет данных'' }}</div>
    <div>Развитие настоящего заболевания: {{ context.first_act.diseaseDevelopment or ''не указано'' }}</div>
  </section>

  <br>

  <!-- Вторичный осмотр -->
  <section>
    <div class="header">Дата {{ context.second_act.beg_date }}</div>

    {% if context.second_act.toothNumber %}
      <div><b>Зуб №:</b> {{ context.second_act.toothNumber }}</div>
    {% endif %}

    {% if context.second_act.cleaningList %}
      <div><b>Список зубов для чистки:</b> {{ context.second_act.cleaningList }}</div>
    {% endif %}

    {% if context.second_act.headAreas %}
      <div><b>Области головы, для которых проводится лечение:</b> {{ context.second_act.headAreas }}</div>
    {% endif %}

    {% if context.second_act.oralMucosa %}
      <div><b>Области слизистой полости рта:</b> {{ context.second_act.oralMucosa }}</div>
    {% endif %}

    {% if context.second_act.complaints %}
      <div><b>Жалобы:</b> {{ context.second_act.complaints }}</div>
    {% endif %}

    {% if context.second_act.anamnesis %}
      <div><b>Анамнез:</b> {{ context.second_act.anamnesis }}</div>
    {% endif %}

    {% if context.second_act.objectiveData %}
      <div><b>Объективные данные:</b> {{ context.second_act.objectiveData }}</div>
    {% endif %}

    {% if context.second_act.clinicalDiagnosis %}
      <div><b>Диагноз:</b> {{ context.second_act.clinicalDiagnosis }}</div>
    {% endif %}

    <div><b>МКБ-10:</b> {{ context.second_act.mkb }} {{ context.second_act.nameDiag or '''' }}</div>

    {% if context.second_act.treatment %}
      <div><b>Лечение:</b> {{ context.second_act.treatment }}</div>
    {% endif %}

    {% if context.second_act.recommendations %}
      <div><b>Рекомендации:</b> {{ context.second_act.recommendations }}</div>
    {% endif %}
  </section>

  <br>

  <!-- Таблица услуг -->
  <table width="100%" cellpadding="3" cellspacing="0" border="1">
    <tr>
      <th width="1%" class="white-wrap">Код услуги</th>
      <th>Наименование услуги</th>
      <th width="1%" class="white-wrap">Цена</th>
      <th width="1%" class="white-wrap">Кол-во</th>
      <th width="1%" class="white-wrap">Сумма, руб</th>
    </tr>

    {% for service in context.services %}
      <tr>
        <td class="white-wrap center">{{ service.code or '''' }}</td>
        <td>{{ service.name or '''' }}</td>
        <td class="white-wrap center">{{ service.price or '''' }}</td>
        <td class="white-wrap center">{{ service.amount or '''' }}</td>
        <td class="white-wrap center">{{ service.sum or '''' }}</td>
      </tr>
    {% endfor %}

    <tr>
      <td colspan="4" class="center"><b>Итого</b></td>
      <td class="center"><b>{{ context.total_sum or ''0'' }}</b></td>
    </tr>
  </table>
</div>
</body>
</html>

', 0, 0, 0, 0, null, 0, 0, 0, null, null, 1, 0, 0, 'P', 0, null, null);

