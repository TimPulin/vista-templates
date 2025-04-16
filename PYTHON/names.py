templateNameList = ['№ школы', 'класс', 'Перенесенные детские инфекционные заболевания', 'Проведенные профилактические прививки', 'Врачебное описание диагноза', 'Шифр МКБ', 'Аллергические заболевания, реакции', 'Назначенный лечащим врачом режим лечения', 'Рост (см)', 'Масса тела (кг)', 'Оценка физического развития', 'Группа здоровья', 'Медицинская группа для занятий физической культурой', 'Нуждаемость в условиях доступной среды', 'Необходимость сопровождения пациента', 'Контакт с инфекционными больными', 'Осмотр на педикулез и чесотку', 'Обследование на гельминтозы', 'Отсутствие медицинских противопоказаний для пребывания в организации отдыха детей и их оздоровления']
actionNameList = ['№ школы', 'класс', 'Перенесенные детские инфекционные заболевания', 'Проведенные профилактические прививки', 'Назначенный лечащим врачом режим лечения', 'Рост (см)', 'Масса тела (кг)', 'Оценка физического развития', 'Группа здоровья', 'Медицинская группа для занятий физической культурой', 'Нуждаемость в условиях доступной среды', 'Необходимость сопровождения пациента', 'Контакт с инфекционными больными', 'Осмотр на педикулез и чесотку', 'Отсутствие медицинских противопоказаний для пребывания в организации отдыха детей и их оздоровления', 'Обследование на гельминтозы (энтеробиоз, гименолепидоз)', 'Комментарий']

uniqTemplateNameList = set(templateNameList) - set(actionNameList)
uniqActionNameList = set(actionNameList) - set(templateNameList)

print('uniqTemplateNameList:', uniqTemplateNameList)
print('uniqActionNameList:', uniqActionNameList)

