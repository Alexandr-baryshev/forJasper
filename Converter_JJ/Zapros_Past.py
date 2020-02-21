zapros_past = '''
{
    "columns": [$$],
    "condition": {
        "conditions": [
            {
                "conditions": [
                    {
                        "action": "IS_NULL",
                        "caption": "Источник информации происшествия",
                        "description": null,
                        "dictionary": "dic_src_et",
                        "id": "id_ce_ID_SRC_TYPE_37c4799e-1f34-4fc6-a0f5-2792931a6691",
                        "idField": "id_ce_ID_SRC_TYPE",
                        "property": null,
                        "type": "dictionary",
                        "value": []
                    },
                    {
                        "action": "NOT_IN",
                        "caption": "Источник информации происшествия",
                        "description": null,
                        "dictionary": "dic_src_et",
                        "id": "id_ce_ID_SRC_TYPE_115be5eb-043f-4e6a-9eaf-2e046a4c3128",
                        "idField": "id_ce_ID_SRC_TYPE",
                        "property": null,
                        "type": "dictionary",
                        "value": [
                            {
                                "dic_src_et_caption": "Системный",
                                "dic_src_et_id": 8
                            },
                            {
                                "dic_src_et_caption": "Информационная область",
                                "dic_src_et_id": 9
                            }
                        ]
                    }
                ],
                "description": null,
                "id": "logic_a3a13eab-2183-4510-82bd-4a22ccaf96b9",
                "property": null,
                "type": "logic_or"
            },
            {
                "conditions": [
                    {
                        "action": null,
                        "caption": "Признак ложного звонка",
                        "description": null,
                        "dictionary": null,
                        "id": "id_ce_WRONG_CALL_c570c1fe-1cfb-494f-a6c2-c7946b24f8ab",
                        "idField": "id_ce_WRONG_CALL",
                        "property": null,
                        "type": "boolean",
                        "value": [
                            {
                                "value": -1
                            }
                        ]
                    },
                    {
                        "action": null,
                        "caption": "Признак ложного звонка",
                        "description": null,
                        "dictionary": null,
                        "id": "id_ce_WRONG_CALL_644a0441-9aaf-4162-9fce-6a1947427876",
                        "idField": "id_ce_WRONG_CALL",
                        "property": null,
                        "type": "boolean",
                        "value": [
                            {
                                "value": 0
                            }
                        ]
                    }
                ],
                "description": null,
                "id": "logic_f3baace7-832b-4799-860b-19289c042ac6",
                "property": null,
                "type": "logic_or"
            }
        ],
        "description": null,
        "id": "logic_6d21d490-5f83-4d7a-ab66-f488bd3f2188",
        "property": null,
        "type": "logic_and"
    },
    "distinct": false,
    "fieldConditions": [
        {
            "action": null,
            "caption": "Время регистрации",
            "description": null,
            "dictionary": null,
            "id": "id_ce_TIME_REG_87dd4a83-2cde-481d-9e11-f42c82bf9327",
            "idField": "id_ce_TIME_REG",
            "property": null,
            "type": "dateTime",
            "value": [
                {
                    "value": "2020-02-01T00:00:00",
                    "value1": "2020-02-02T00:00:00"
                }
            ]
        }
    ],
    "limit": null,
    "name": null,
    "property": null,
    "type": "simple"
}
'''