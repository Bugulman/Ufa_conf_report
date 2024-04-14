#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="wells_from_filter",
      variables=[])


wells_from_filter_variables = {

}

def wells_from_filter (variables = wells_from_filter_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    end_user_imports ()

    begin_wf_item (index = 1, is_custom_code = True, name = "Перетаскиваем скважины из проекта в базу")
    import pandas as pd
    from sqlalchemy import create_engine
    from datetime import datetime


    def well_filter_to_base(name):
    	filter = get_well_filter_by_name (name=name)
    	well_list = [[x.name, name] for x in filter.get_wells()]
    	df = pd.DataFrame(well_list, columns = ['well', 'well_filter'])
    	df['export_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    	post_con = create_engine('postgresql://test:test@localhost:5434/ungkm')
    	df.to_sql('well_filters', con=post_con, if_exists='replace')

    filters = ['east', 'west', 'middle', 'ps_unmatched']

    for fill in filters:
    	well_filter_to_base(fill)

    end_wf_item (index = 1)


