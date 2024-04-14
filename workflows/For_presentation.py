#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="For_presentation",
      variables=[])


For_presentation_variables = {

}

def For_presentation (variables = For_presentation_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    end_user_imports ()

    begin_wf_item (index = 1)
    groups = []
    set_var_type (n = "groups", t = "PY_EXPR", it = "PY_EXPR", val = groups)

    end_wf_item (index = 1)


    if False:
        begin_wf_item (index = 2, is_custom_code = True)
        from pathlib import Path
        import os

        path = Path(get_project_folder ())

        path = path.joinpath('reports')

        with open(path.joinpath('sep.inc'), 'w+') as f:
        	for w in get_all_wells ():
        		if w.name.startswith('1A'):
        			f.write(f'{w.name} SEP1 \n')
        		else:
        			f.write(f'{w.name} SEP2 \n')

        print(path)
        end_wf_item (index = 2)


    if False:
        begin_wf_item (index = 3, name = "Сохранить график")
        create_screenshot (window_name="ОТЧЕТ",
              extension="jpg",
              filename="/cluster3/home/albert.vafin/UNGKM/Designer/UNGKM_RES_ENG2.snf/Screenshots/Участок4_вода.JPG",
              pagesize="A3",
              orientation="Landscape",
              layout_type="Best Fit",
              units="pixels",
              width=1920,
              height=1200,
              add_date_to_filename=True,
              add_date_to_filename_method="add_current_calendar_date",
              create_screenshots_pack=False,
              first_step_number=0,
              last_step_number=190,
              add_step_number_to_filename=True,
              date_format="DD-MM-YYYY",
              font="Arial,24,-1,5,50,0,0,0,0,0",
              caption_position="Above",
              caption_alignment="Left",
              use_default_name=False,
              default_name=None,
              caption=None)
        end_wf_item (index = 3)


    if False:
        begin_wf_item (index = 4, name = "Сохранить карту")
        create_screenshot (window_name="2D 3",
              extension="jpg",
              filename="/cluster3/home/albert.vafin/UNGKM/Designer/UNGKM_RES_ENG2.snf/Screenshots/Участок1_карта.JPG",
              pagesize="A3",
              orientation="Landscape",
              layout_type="Best Fit",
              units="pixels",
              width=1920,
              height=1200,
              add_date_to_filename=True,
              add_date_to_filename_method="add_current_calendar_date",
              create_screenshots_pack=False,
              first_step_number=0,
              last_step_number=190,
              add_step_number_to_filename=True,
              date_format="DD-MM-YYYY",
              font="Arial,24,-1,5,50,0,0,0,0,0",
              caption_position="Above",
              caption_alignment="Left",
              use_default_name=False,
              default_name=None,
              caption=None)
        end_wf_item (index = 4)


    begin_wf_item (index = 5, name = "Получаем и сохраняем группы")
    run_graph_calculator (gc_code="groups = []\n\nfor g in get_all_groups():\n	groups.append(g.name)\n\nfrom pathlib import Path\nimport os\nimport pickle\n\npath = Path(get_project_folder ())\n\npath = path.joinpath(\'reports\')\n\nwith open(path.joinpath(\'group.pickle\'), \'wb\') as f:\n	pickle.dump(groups,f)",
          font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
          models=["SHORT_AREA:UNGKM_13_big"],
          variables=variables)
    end_wf_item (index = 5)


    begin_wf_item (index = 6, is_custom_code = True, name = "Вытаскиваем группы как внутренюю переменную")
    from pathlib import Path
    import os
    import pickle

    path = Path(get_project_folder ())

    path = path.joinpath('reports')

    with open(path.joinpath('group.pickle'), 'rb') as f:
    	groups = pickle.load(f)
    end_wf_item (index = 6)


    begin_wf_item (index = 7)
    for group in groups:
        pass
        set_var_type (n = "group", t = "PY_EXPR", it = "PY_EXPR", val = group)
        begin_loop_iteration (info = "group = " + str (group))



        begin_wf_item (index = 8, is_custom_code = True, name = "Переключаем графики")
        graph_template_object (window_type="Graph Templates",
              window_name="ОТЧЕТ",
              objects_table=[{"object_type" : "Group", "object_name" : group}],
              clear_selection=True)
        end_wf_item (index = 8)


        begin_wf_item (index = 9, is_custom_code = True, name = "Сохраняем графики")
        from pathlib import Path
        import os
        import pickle

        path = Path(get_project_folder ())

        path = path.joinpath('reports', group+'.JPG')

        print(path)


        create_screenshot (window_name="ОТЧЕТ",
              extension="jpg",
              filename=str(path),
              pagesize="A3",
              orientation="Landscape",
              layout_type="Best Fit",
              units="pixels",
              width=1920,
              height=1300,
              add_date_to_filename=True,
              add_date_to_filename_method="add_current_calendar_date",
              create_screenshots_pack=False,
              first_step_number=0,
              last_step_number=190,
              add_step_number_to_filename=True,
              date_format="DD-MM-YYYY",
              font="Arial,24,-1,5,50,0,0,0,0,0",
              caption_position="Above",
              caption_alignment="Left",
              use_default_name=False,
              default_name=None,
              caption=None)
        end_wf_item (index = 9)


        end_loop_iteration ()

    end_wf_item (index = 7)


