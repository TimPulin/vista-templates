import pymysql

SCHEMA_NAME = 's11vm'


def connect_db(schema_name):
    connection = pymysql.connect(
        host='192.168.1.3',
        port=2401,
        user='dbuser',
        password='dbpassword',
        database=schema_name
    )
    return connection


def close_db(connection):
    cursor = connection.cursor()
    cursor.close()


def format_query(schema_name, action_type_id):

    return [
        f"""
            INSERT INTO {schema_name}.actionpropertytype (deleted, actionType_id, idx, template_id, name, shortName, descr, unit_id,
                                                  typeName, valueDomain, defaultValue, isVector, norm, sex, age, penalty,
                                                  penaltyUserProfile, penaltyDiagnosis, visibleInJobTicket, visibleInTableRedactor,
                                                  isAssignable, test_id, defaultEvaluation, canChangeOnlyOwner,
                                                  isActionNameSpecifier, laboratoryCalculator, inActionsSelectionTable,
                                                  redactorSizeFactor, isFrozen, typeEditable, visibleInDR, userProfile_id,
                                                  userProfileBehaviour, copyModifier, isVitalParam, vitalParamId, isODIIParam,
                                                  customSelect, autoFieldUserProfile, formulaAlias, incrementOnSave, orientation,
                                                  ticketsNeeded, autoFillAutoField, color, parent_id, propHiddeOrgStructure)
            VALUES (0, {action_type_id}, 0, null, 'Номерок', '', '', null, 'JobTicket', 'gosp6;a+', '', 0, '', 0, '', 0, null, null, 0, 0, 0,
                    27532, 0, 0, 0, null, 0, 0, 0, 1, 0, 1, 1, 1, 0, null, 0, null, null, null, 0, 'v', null, 0, '', null, null);        
        """,

        f"""
            INSERT INTO {schema_name}.actionpropertytype (deleted, actionType_id, idx, template_id, name, shortName, descr, unit_id,
                                                  typeName, valueDomain, defaultValue, isVector, norm, sex, age, penalty,
                                                  penaltyUserProfile, penaltyDiagnosis, visibleInJobTicket, visibleInTableRedactor,
                                                  isAssignable, test_id, defaultEvaluation, canChangeOnlyOwner,
                                                  isActionNameSpecifier, laboratoryCalculator, inActionsSelectionTable,
                                                  redactorSizeFactor, isFrozen, typeEditable, visibleInDR, userProfile_id,
                                                  userProfileBehaviour, copyModifier, isVitalParam, vitalParamId, isODIIParam,
                                                  customSelect, autoFieldUserProfile, formulaAlias, incrementOnSave, orientation,
                                                  ticketsNeeded, autoFillAutoField, color, parent_id, propHiddeOrgStructure)
            VALUES (0, {action_type_id}, 1, null, 'Коментарии', '', '', null, 'Text', '', '', 0, '', 0, '', 0, null, null, 0, 0, 0, null, 0, 0,
                    0, null, 0, 0, 0, 1, 0, null, 0, 1, 0, null, 0, null, null, null, 0, 'v', null, 0, '', null, null);        
        """,

        f"""
            INSERT INTO {schema_name}.actionpropertytype (deleted, actionType_id, idx, template_id, name, shortName, descr, unit_id,
                                                  typeName, valueDomain, defaultValue, isVector, norm, sex, age, penalty,
                                                  penaltyUserProfile, penaltyDiagnosis, visibleInJobTicket, visibleInTableRedactor,
                                                  isAssignable, test_id, defaultEvaluation, canChangeOnlyOwner,
                                                  isActionNameSpecifier, laboratoryCalculator, inActionsSelectionTable,
                                                  redactorSizeFactor, isFrozen, typeEditable, visibleInDR, userProfile_id,
                                                  userProfileBehaviour, copyModifier, isVitalParam, vitalParamId, isODIIParam,
                                                  customSelect, autoFieldUserProfile, formulaAlias, incrementOnSave, orientation,
                                                  ticketsNeeded, autoFillAutoField, color, parent_id, propHiddeOrgStructure)
            VALUES (0, {action_type_id}, 2, null, 'Изображение', '', '', null, 'Image', '', '', 0, '', 0, '', 0, null, null, 1, 0, 0, null, 0,
                    0, 0, null, 0, 0, 0, 1, 0, null, 0, 1, 0, null, 0, null, null, null, 0, 'v', null, 0, '', null, null);        
        """,

        f"""
            INSERT INTO {schema_name}.actionpropertytype (deleted, actionType_id, idx, template_id, name, shortName, descr, unit_id,
                                                  typeName, valueDomain, defaultValue, isVector, norm, sex, age, penalty,
                                                  penaltyUserProfile, penaltyDiagnosis, visibleInJobTicket, visibleInTableRedactor,
                                                  isAssignable, test_id, defaultEvaluation, canChangeOnlyOwner,
                                                  isActionNameSpecifier, laboratoryCalculator, inActionsSelectionTable,
                                                  redactorSizeFactor, isFrozen, typeEditable, visibleInDR, userProfile_id,
                                                  userProfileBehaviour, copyModifier, isVitalParam, vitalParamId, isODIIParam,
                                                  customSelect, autoFieldUserProfile, formulaAlias, incrementOnSave, orientation,
                                                  ticketsNeeded, autoFillAutoField, color, parent_id, propHiddeOrgStructure)
            VALUES (0, {action_type_id}, 3, null, 'Результат', '', '', null, 'Text', '', '', 0, '', 0, '', 0, null, null, 1, 1, 0, null, 0, 0,
                    0, null, 0, 0, 0, 1, 0, null, 0, 1, 0, null, 1, null, null, null, 0, 'v', null, 0, '', null, null);        
        """,

        f"""
            INSERT INTO {schema_name}.actionpropertytype (deleted, actionType_id, idx, template_id, name, shortName, descr, unit_id,
                                                  typeName, valueDomain, defaultValue, isVector, norm, sex, age, penalty,
                                                  penaltyUserProfile, penaltyDiagnosis, visibleInJobTicket, visibleInTableRedactor,
                                                  isAssignable, test_id, defaultEvaluation, canChangeOnlyOwner,
                                                  isActionNameSpecifier, laboratoryCalculator, inActionsSelectionTable,
                                                  redactorSizeFactor, isFrozen, typeEditable, visibleInDR, userProfile_id,
                                                  userProfileBehaviour, copyModifier, isVitalParam, vitalParamId, isODIIParam,
                                                  customSelect, autoFieldUserProfile, formulaAlias, incrementOnSave, orientation,
                                                  ticketsNeeded, autoFillAutoField, color, parent_id, propHiddeOrgStructure)
            VALUES (0, {action_type_id}, 4, null, 'Описание', '', '', null, 'Text', '', '', 0, '', 0, '', 0, null, null, 1, 1, 0, null, 0, 0,
                    0, null, 0, 0, 0, 1, 0, null, 0, 1, 0, null, 1, null, null, null, 0, 'v', null, 0, '', null, null);        
        """,

        f"""
            INSERT INTO {schema_name}.actionpropertytype (deleted, actionType_id, idx, template_id, name, shortName, descr, unit_id,
                                                  typeName, valueDomain, defaultValue, isVector, norm, sex, age, penalty,
                                                  penaltyUserProfile, penaltyDiagnosis, visibleInJobTicket, visibleInTableRedactor,
                                                  isAssignable, test_id, defaultEvaluation, canChangeOnlyOwner,
                                                  isActionNameSpecifier, laboratoryCalculator, inActionsSelectionTable,
                                                  redactorSizeFactor, isFrozen, typeEditable, visibleInDR, userProfile_id,
                                                  userProfileBehaviour, copyModifier, isVitalParam, vitalParamId, isODIIParam,
                                                  customSelect, autoFieldUserProfile, formulaAlias, incrementOnSave, orientation,
                                                  ticketsNeeded, autoFillAutoField, color, parent_id, propHiddeOrgStructure)
            VALUES (0, {action_type_id}, 5, null, 'Заключение', '', '', null, 'Text', '', '', 0, '', 0, '', 0, null, null, 1, 1, 0, null, 0, 0,
                    0, null, 0, 0, 0, 1, 0, null, 0, 1, 0, null, 1, null, null, null, 0, 'v', null, 0, '', null, null);        
        """,

    ]


def execute_query(connection, query_list):
    try:
        with connection.cursor() as loc_cursor:
            for query in query_list:
                loc_cursor.execute(query)
        connection.commit()
        print('запросы выполнен')
    except Exception as e:
        print('провален запрос', e)
        connection.rollback()


def get_action_type_id(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
            select at.id
            from actiontype at
            where
                at.deleted =  0
                and at.name regexp '^ультразвуковое'
                and at.id != 34835;    
        """
    )
    result = cursor.fetchall()
    return list(map(lambda x: x[0], result))


if __name__ == '__main__':
    conn = connect_db(SCHEMA_NAME)
    action_type_id_list = get_action_type_id(conn)

    for action_type_id in action_type_id_list:
        new_query = format_query(SCHEMA_NAME, action_type_id)
        execute_query(conn, new_query)

    close_db(conn)
    print('работа с БД завершена')

