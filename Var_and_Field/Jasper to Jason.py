jason = [
    '''
{
    "agg": null,
    "alias": null,
    "caption": "Идентификатор происшествия",
    "columnSwitch": null,
    "id": "id_ce_ID_d7ed8869-b757-4256-9c50-b46ad30f8d84",
    "idField": "id_ce_ID"
},
'''
    ,
    '''
{
  "agg": null,
  "alias": null,
  "caption": "ФИО пациента",
  "columnSwitch": null,
  "id": "card03_p_50140766-dda0-45b6-a430-da36db4adcb5",
  "idField": "card03_p"
}
 '''
]

jasper = ["Идентификатор происшествия", "ФИО пациента"]

a = 0
b = 0

if  jason[a].__contains__(jasper[b]):

    print("yes")
else:
    print("no")
