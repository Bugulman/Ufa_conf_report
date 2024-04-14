#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="drilling_analitic",
      variables=[])


drilling_analitic_variables = {

}

def drilling_analitic (variables = drilling_analitic_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    import getpass
    import os
    import calendar
    from datetime import datetime
    import pandas as pd
    from pathlib import Path
    import numpy as np
    from sqlalchemy import create_engine
    end_user_imports ()

    begin_wf_item (index = 1, name = "Создание таблиц по таблице добычи")
    workflow_folder ()
    if True:
        pass



        begin_wf_item (index = 2)
        prod = pd.DataFrame()
        set_var_type (n = "prod", t = "PY_EXPR", it = "PY_EXPR", val = prod)
        drilling_pivot = pd.DataFrame()
        set_var_type (n = "drilling_pivot", t = "PY_EXPR", it = "PY_EXPR", val = drilling_pivot)

        end_wf_item (index = 2)


        if False:
            begin_wf_item (index = 3)
            wells_production_table_calculate_wef_by_operation_time (table=find_object (name="hist",
                  type="gt_wells_production_data"))
            end_wf_item (index = 3)


        begin_wf_item (index = 4, is_custom_code = True, name = "Функции")
        def df_from_histtab(paramert_list: list, start='01.01.1950', **kwarg):
            df = []
            coll_name = ['well', 'date']+paramert_list
            start_date = datetime.strptime(start, '%d.%m.%Y')
            for w in kwarg['wells']:
                print(w.name)
                for t in kwarg['mod'].get_records(well=w):
                    if t.get_date().date() >= start_date.date():
                        row = []
                        row.append(w.name)
                        row.append(t.get_date().date())
                        row = row+[t.get_value(type=parametr)
                                   for parametr in paramert_list]
                        df.append(row)
                    else:
                        continue
            print(coll_name)
            result = pd.DataFrame(df, columns=coll_name)
            result.set_index('date', inplace=True)
            result.sort_values(by=['well', 'date'], ascending=True, inplace=True)
            return result


        def create_report_dir(path):
            path = Path(path)
            path = path.joinpath('reports')
            path.mkdir(parents=True, exist_ok=True)
            os.chdir(path)


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
        end_wf_item (index = 4)


        begin_wf_item (index = 5, is_custom_code = True, name = "Функции анализа бурения")
        def drill_year (df):
            df['Year']=df['date'].dt.year
            df['Start_date'] = df['date'].min()
            df['Start_year'] = df['Year'].min()
            return df


        def work_day (df):
            df['Day'] = df['date']-df['date'].min()
            return df


        def work_month (df):
            df['Month'] = np.linspace(1, len(df), len(df))
            return df

        def first_deb (df, x=5):
            df['qo'] = df['oil_prod'].head(x).sum()/df['work_day'].head(x).sum()*24
            df['ql'] = df['liq_prod'].head(x).sum()/df['work_day'].head(x).sum()*24
            df['qg'] = df['gas_prod'].head(x).sum()/df['work_day'].head(x).sum()*24
            df['qw'] = df['wat_prod'].head(x).sum()/df['work_day'].head(x).sum()*24
            return df

        def cummulitive (df):
            df['tot_oil'] = df['oil_prod'].cumsum()
            df['tot_liq'] = df['liq_prod'].cumsum()
            df['tot_gas'] = df['gas_prod'].cumsum()
            return df
            
        def Kpad (df):
            df['kpad'] = df['oil']/df['oil'].shift(1)
            return df

        def first(df):
        	return df.head(1)
        end_wf_item (index = 5)


        begin_wf_item (index = 6, is_custom_code = True, name = "Парсим таблицу добычи")

        keyword = {'wells': get_all_wells (),
        #           'wells': get_well_filter_by_name (name='target').get_wells (),
                   'mod': get_wells_production_table_by_name (name='UNGKM_prod_from_VAR'),
                   'step': get_all_timesteps()}

        paramert_list= ['oil', 'water', 'gas', 'wefac']

        prod = df_from_histtab(paramert_list=paramert_list, start='01.01.1950', **keyword)
        prod.reset_index(inplace=True)
        end_wf_item (index = 6)


        begin_wf_item (index = 7, is_custom_code = True, name = "Применяем функции")
        prod['day_in_month'] = prod['date'].apply(lambda x: calendar.monthrange(x.year, x.month)[1])
        prod['work_day'] = prod['day_in_month']*prod['wefac']

        prod['oil_prod']=prod['oil']*prod['day_in_month']*prod['wefac']
        prod['wat_prod']=prod['water']*prod['day_in_month']*prod['wefac']
        prod['liq_prod']=prod['oil_prod']+prod['wat_prod']
        prod['gas_prod']=prod['gas']*prod['day_in_month']*prod['wefac']
        prod['wct']=prod['wat_prod']/prod['liq_prod']*100
        prod['date'] = pd.to_datetime(prod['date'])
        prod = prod[prod.oil>0]

        prod.reset_index(drop=True, inplace = True) 
        functions = [drill_year, work_month, work_day, first_deb, cummulitive, Kpad]

        for f in functions:
            prod=pd.DataFrame(prod.groupby(by='well').apply(f))
            prod.reset_index(drop=True, inplace = True) 

        end_wf_item (index = 7)


        begin_wf_item (index = 8, is_custom_code = True, name = "Экспорт основной таблицы в навигатор")
        df_to_table(prod, 'drilling_analitic')
        end_wf_item (index = 8)


        begin_wf_item (index = 9, is_custom_code = True, name = "Экспорт сводной таблицы в навигатор")
        convert = ['oil','gas','water', 'Start_year']
        for c in convert:
            prod[c]=pd.to_numeric(prod[c])

        drilling_pivot = prod.groupby('well').agg({'oil':'mean',
        'gas':'mean', 'water':'mean', 'Start_year':'mean',
        'Start_date':'first'})
        post_con = create_engine('postgresql://test:test@localhost:5434/ungkm')
        drilling_pivot.to_sql('first_debits', con=post_con, if_exists='append')
        df_to_table(drilling_pivot.reset_index(), 'drilling_pivot')
        end_wf_item (index = 9)


        begin_wf_item (index = 10, is_custom_code = True, name = "Экспорт файлов в папочку")
        create_report_dir(get_project_folder ())

        drilling_pivot.to_csv('drilling_pivot.csv')
        end_wf_item (index = 10)


        if False:
            begin_wf_item (index = 11)
            table_import (splitter=True,
                  file_names=["reports/press_prod.csv"],
                  splitter2=True,
                  delimiter="comma",
                  import_header=False)
            end_wf_item (index = 11)


        if False:
            begin_wf_item (index = 12)
            wells_history_import_simple_table_format (wells=find_object (name="Wells",
                  type="gt_wells_entity"),
                  well_searcher="name",
                  well_production=find_object (name="merged_table",
                  type="gt_wells_production_data"),
                  reload_all=False,
                  splitter=True,
                  file_names=["reports/press_prod.csv"],
                  tabulator=TableFormat (separator="comma",
                  comment="",
                  skip_lines=1,
                  columns=["skip", "Date", "Well", "Oil Rate", "Water Rate", "Gas rate", "Tubing Head Pressure", "WEF", "Bottom Hole Pressure"]),
                  placeholder="-",
                  zero_missing_columns=True,
                  efficiency_factor_units="Relative",
                  date_format="YYYY-MM-DD",
                  use_start_date=False,
                  start_date=datetime (year=2022,
                  month=10,
                  day=6,
                  hour=0,
                  minute=0,
                  second=0),
                  time_format="HH:MM:SS",
                  date_filter=False,
                  first_date=datetime (year=2022,
                  month=10,
                  day=6,
                  hour=0,
                  minute=0,
                  second=0),
                  last_date=datetime (year=2022,
                  month=10,
                  day=6,
                  hour=0,
                  minute=0,
                  second=0),
                  liquid_rate_units="sm3/day",
                  gas_rate_units="sm3/day",
                  reservoir_rate_units="rm3/day",
                  liquid_volume_units="sm3",
                  gas_volume_units="sm3",
                  reservoir_volume_units="rm3",
                  pressure_absolute_units="bara",
                  pressure_units="bara",
                  enthalpy_units="kJ/kg-M",
                  temperature_units="C",
                  mass_concentration_units="kg/sm3",
                  molar_rate_units="kg-m/day",
                  reaction_energy_units="kJ/day",
                  liquid_liquid_units="sm3_div_sm3",
                  fraction_units="fraction",
                  liquid_gas_units="sm3_div_sm3",
                  gas_liquid_units="sm3_div_sm3")
            end_wf_item (index = 12)



    end_wf_item (index = 1)


