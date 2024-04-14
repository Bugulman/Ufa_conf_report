#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="Import_csv_into_tnav_table",
      variables=[])


Import_csv_into_tnav_table_variables = {

}

def Import_csv_into_tnav_table (variables = Import_csv_into_tnav_table_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    end_user_imports ()

    begin_wf_item (index = 1)
    comment_text ("""
Скрипт позволяет загружать в \"Таблицы\" дизайнера моделей таблицы в формате csv
""")
    end_wf_item (index = 1)


    begin_wf_item (index = 2, name = "Можно часть переменных задать тут а не в диалоге")
    file = 'paht'
    set_var_type (n = "file", t = "STRING", it = "PY_EXPR", val = file)
    variables["FILE"] = file
    table_name = 'KVD_interp'
    set_var_type (n = "table_name", t = "STRING", it = "PY_EXPR", val = table_name)
    variables["TABLE_NAME"] = table_name
    delimert = ';'
    set_var_type (n = "delimert", t = "STRING", it = "PY_EXPR", val = delimert)
    variables["DELIMERT"] = delimert

    end_wf_item (index = 2)


    begin_wf_item (index = 3, is_custom_code = True, name = "Пользовательский диалог")
    import pandas as pd

    window = create_dialog()
    window.set_title(text = 'Загрузка таблицы из CSV файла')
    window.add_ok_button (text= 'Ok')

    layout = window.get_layout ()
    layout.create_label (text='Выберите файл для загрузки')
    path = layout.create_filepath_widget(default_value=get_project_folder (), mode='open')
    layout.create_label (text='Введите название таблицы')
    name = layout.create_lineedit (default_value=table_name)
    layout.create_label (text='Введите разделяющий символ')
    delimetr = layout.create_lineedit (default_value = delimert)

    #sheets = layout.create_combobox (values=['1','2'], default_value='1')


    window.exec ()
    file = path.get_value ()
    table_name = name.get_value()
    delimetr = delimetr.get_value()

    # Get the sheet names
    print(delimetr)
    end_wf_item (index = 3)


    begin_wf_item (index = 4, is_custom_code = True, name = "Обработка таблицы")
    import pandas as pd

    #file = '/cluster3/public/2023/UNGKM/for_GDM/МЭРЫ/Добыча_для_ДМ.csv'

    def df_to_table(df, name='from_df'):
        create_table(name=name, overwrite_existing=True)
        rows, cols = df.shape
        get_table_by_name(name=name).set_size(
            r_count=rows, c_count=cols)
        for col_name in df.columns:
            df[col_name] = df[col_name].astype('str')
        get_table_by_name(name=name).set_all_data (values=df)
        for n, col_name in enumerate(df.columns):
            get_table_by_name(name=name).set_column_header (column=n+1, text=col_name)

    df = pd.read_csv(file, delimiter=delimetr)
    df_to_table(df, name = table_name)


    end_wf_item (index = 4)


