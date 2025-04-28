-- НЕ ЗАПУСКАТЬ ВСЕ ЗАПРОСЫ СРАЗУ. СНАЧАЛА ПРОВЕРИТЬ НАЛИЧИЕ ИНДЕКСОВ

-- ПРОВЕРКА НА СУЩЕСТВОВАНИЕ ИНДЕКСА
SELECT CONSTRAINT_NAME
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'Referral'
  AND CONSTRAINT_TYPE = 'FOREIGN KEY'
  AND CONSTRAINT_NAME = 'Referral_ibfk_2';

SELECT CONSTRAINT_NAME
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'ClientExaminationPlan_SPB'
  AND CONSTRAINT_TYPE = 'FOREIGN KEY'
  AND CONSTRAINT_NAME = 'ClientExaminationPlan_SPB_ibfk_2';

SELECT CONSTRAINT_NAME
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'ClientExaminationPlan_SPB'
  AND CONSTRAINT_TYPE = 'FOREIGN KEY'
  AND CONSTRAINT_NAME = 'ClientExaminationPlan_SPB_ibfk_3';

-- UPDATES

alter table OrgStructure_Address
add column if not exists deleted tinyint NOT NULL default 0;


-- auto-generated definition
create table if not exists rbReferralTypeUO
(
    id             int auto_increment
        primary key,
    createDatetime datetime default current_timestamp() null comment 'Дата добавления',
    modifyDatetime datetime                             null comment 'Дата редактирования',
    code           varchar(32)                          not null comment 'Код',
    name           varchar(64)                          not null comment 'Наименование',
    netrica_Code   varchar(6)                           null comment 'Код в справочнике Нетрики',
    EGISZ_code     varchar(16)                          null
)
    comment 'Справочник - Типы направлений: 1.2.643.2.69.1.1.1.55';

INSERT INTO s11.rbReferralTypeUO (id, createDatetime, modifyDatetime, code, name, netrica_Code, EGISZ_code)
VALUES (1, '2024-08-21 13:26:17', null, 'hospitalisation', 'На госпитализацию', '1', '1');

INSERT INTO s11.rbReferralTypeUO (id, createDatetime, modifyDatetime, code, name, netrica_Code, EGISZ_code)
VALUES (2, '2024-08-21 13:26:17', null, 'rehabilitation', 'На восстановительное лечение', '2', '8');

INSERT INTO s11.rbReferralTypeUO (id, createDatetime, modifyDatetime, code, name, netrica_Code, EGISZ_code)
VALUES (3, '2024-08-21 13:26:17', null, 'diagnostic', 'На обследование', '3', '4');

INSERT INTO s11.rbReferralTypeUO (id, createDatetime, modifyDatetime, code, name, netrica_Code, EGISZ_code)
VALUES (4, '2024-08-21 13:26:18', null, 'consultation', 'На консультацию', '4', '7');


ALTER TABLE EventType
    ADD COLUMN IF NOT EXISTS filterOrgstructure TINYINT(1) NULL;

ALTER TABLE EventType
    ADD COLUMN IF NOT EXISTS filterPersons TINYINT(1) NULL;

ALTER TABLE Referral
    ADD COLUMN IF NOT EXISTS PersonFromLPU tinyint(1) default 0 null comment 'Врач из ЛПУ';


ALTER TABLE Referral
    ADD COLUMN IF NOT EXISTS person_id int null comment 'Врач';

ALTER TABLE Referral
    ADD CONSTRAINT Referral_ibfk_2
        FOREIGN KEY (person_id)
            REFERENCES Person (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE;

ALTER TABLE Referral
    ADD COLUMN IF NOT EXISTS date_get date null;

alter table ClientExaminationPlan_SPB
    add column if not exists event_id_stage1  int null comment 'Обращение, соответсвующее I этапу текущего проф. мероприятия {Event}';

alter table ClientExaminationPlan_SPB
    add constraint
        ClientExaminationPlan_SPB_ibfk_2
        foreign key (event_id_stage1)
            references Event (id)
            ON DELETE CASCADE;

alter table ClientExaminationPlan_SPB
    add column if not exists event_id_stage2 int null comment 'Обращение, соответсвующее II второму этапу текущего проф. мероприятия {Event}';

alter table ClientExaminationPlan_SPB
    add constraint ClientExaminationPlan_SPB_ibfk_3
        foreign key (event_id_stage2) references Event (id)
            on delete cascade;

create index event_id_stage1
    on ClientExaminationPlan_SPB (event_id_stage1);

create index event_id_stage2
    on ClientExaminationPlan_SPB (event_id_stage2);

