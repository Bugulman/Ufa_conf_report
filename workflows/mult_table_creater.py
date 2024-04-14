#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="mult_table_creater",
      variables=[])


mult_table_creater_variables = {

}

def mult_table_creater (variables = mult_table_creater_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    end_user_imports ()

    if False:
        begin_wf_item (index = 1)
        log_statistics_table (result_table=find_object (name="Wells",
              type="Table"),
              use_append_table=False,
              append_table="rows",
              source_log=find_object (name="MD",
              type="WellLog"),
              statistics_type="weighted_by_length",
              use_lower_probability=False,
              lower_probability=10,
              use_upper_probability=False,
              upper_probability=90,
              use_well_filter=False,
              well_filter=find_object (name="All Wells",
              type="WellFilter"),
              wells=find_object (name="Wells",
              type="gt_wells_entity"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              use_current_marker_set=False,
              current_marker_set=find_object (name="",
              type="MarkerSet"),
              intervals_table=[{"top_marker" : find_object (name="MULT_ZONE_2",
              type="WellMarker"), "bottom_marker" : find_object (name="MULT_ZONE_3",
              type="WellMarker"), "interval_name" : "1"}])
        end_wf_item (index = 1)


    begin_wf_item (index = 2, name = "Описание")
    comment_text ("""
Воркфлоу для создания пользовательской таблицы для формирования куба с мультипликаторами.
Для работы необходимо задать
ZONECUB - название куба с пластами, по которым необходимо проводить интерполяцию. ВАЖНО! Куб должен представлять последовательность пластов от 1 до n! 
MUTL_TABLE_NAME - название таблицы, которая в итоге будет сформирована

Данное название таблицы нужно будет передать в воркфлоу mutl_creater для формирования куба множителей.

В ТАБЛИЦУ В СООТВЕТСТВУЮЩИЙ СТОЛБЕЦ \"MULT\" ВВОДИМ ЗНАЧЕНИЯ РУКАМИ ДЛЯ ЗАДАЧ АДАПТАЦИИ!
""")
    end_wf_item (index = 2)


    begin_wf_item (index = 3, name = "Переменные от пользователя")
    ZONECUB = 'ZONE'
    set_var_type (n = "ZONECUB", t = "STRING", it = "PY_EXPR", val = ZONECUB)
    variables["ZONECUB"] = ZONECUB
    MUTL_TABLE_NAME = 'MULT_OFP'
    set_var_type (n = "MUTL_TABLE_NAME", t = "STRING", it = "PY_EXPR", val = MUTL_TABLE_NAME)
    variables["MUTL_TABLE_NAME"] = MUTL_TABLE_NAME

    end_wf_item (index = 3)


    begin_wf_item (index = 4, name = "Переменные(не трогать!)")
    HOR = []
    set_var_type (n = "HOR", t = "PY_EXPR", it = "PY_EXPR", val = HOR)
    PARAMS = []
    set_var_type (n = "PARAMS", t = "PY_EXPR", it = "PY_EXPR", val = PARAMS)
    COUNTER = 2
    set_var_type (n = "COUNTER", t = "INTEGER", it = "PY_EXPR", val = COUNTER)
    variables["COUNTER"] = COUNTER
    gis = []
    set_var_type (n = "gis", t = "PY_EXPR", it = "PY_EXPR", val = gis)
    LOG_NAME = "MD"
    set_var_type (n = "LOG_NAME", t = "STRING", it = "PY_EXPR", val = LOG_NAME)
    variables["LOG_NAME"] = LOG_NAME
    AVG_LOG = "Avg. " + LOG_NAME
    set_var_type (n = "AVG_LOG", t = "STRING", it = "PY_EXPR", val = AVG_LOG)
    variables["AVG_LOG"] = AVG_LOG

    end_wf_item (index = 4)


    if False:
        begin_wf_item (index = 5)
        object_template_mapping (folder=find_object (name="3D-Grids",
              type="TypedFolder"),
              use_grid=True,
              grid=find_object (name="BLACK_OIL_DEMO",
              type="Grid3d"),
              object_template_table=[{"object" : "PSEVDO", "template_data" : "Discrete (Auto Generated)", "use_local_palette" : False, "object_type" : ""}])
        end_wf_item (index = 5)


    if False:
        begin_wf_item (index = 6, is_custom_code = True, name = "Костыль_продление траеторий")
        grid = get_all_grids ()[0]
        print(grid.get_max_z ())


        wells_elongate_traj (wells=find_object (name="Wells",
              type="gt_wells_entity"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              use_well_filter=False,
              well_filter=find_object (name="Import Model Well Filter(BLACK_OIL_DEMO)",
              type="WellFilter"),
              elongate_mode_method="by_set_value",
              by_markers=True,
              by_logs=True,
              use_add_extra_traj=True,
              add_extra_traj=1,
              set_extra_traj_length=1,
              set_depth_traj=grid.get_max_z ())
        end_wf_item (index = 6)


    if False:
        begin_wf_item (index = 7)
        wells_log_create_by_grid_property (mesh=find_object (name="Cuted",
              type="Grid3d"),
              grid_property=find_object (name=resolve_variables_in_string (string_with_variables="@ZONECUB@",
              variables=variables),
              type="Grid3dProperty"),
              log_step_type="use_grid_step",
              log_step_val=1,
              source_log=find_object (name=resolve_variables_in_string (string_with_variables="@AVG_LOG@",
              variables=variables),
              type="WellLog"),
              result_log=find_object (name="ZONES",
              type="WellLog"),
              wells=find_object (name="Wells",
              type="gt_wells_entity"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              use_well_filter=True,
              well_filter=find_object (name="target_area",
              type="WellFilter"))
        end_wf_item (index = 7)


    if False:
        begin_wf_item (index = 8)
        wells_log_calculator (result_well_log=find_object (name="MD",
              type="WellLog"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              wells_log_grid_mode="well_log",
              well_log=find_object (name="ZONES",
              type="WellLog"),
              use_log_domain=True,
              add_point_for_md_null=False,
              uniform_grid_step=0.1,
              use_interpolation_mode=True,
              interpolation_mode="discrete",
              use_interpolation_mode_from_grid_log=True,
              use_well_filter=True,
              well_filter=find_object (name="target_area",
              type="WellFilter"),
              use_current_marker_set=False,
              current_marker_set=find_object (name="",
              type="MarkerSet"),
              formula="MD",
              variables=variables)
        end_wf_item (index = 8)


    if False:
        begin_wf_item (index = 9)
        marker_create_by_zone_log (marker_name="MULT_ZONE",
              create_top_marker=True,
              create_bottom_marker=True,
              discrete_log=find_object (name="ZONES",
              type="WellLog"),
              use_well_filter=True,
              well_filter=find_object (name="target_area",
              type="WellFilter"),
              wells=find_object (name="Wells",
              type="gt_wells_entity"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"))
        end_wf_item (index = 9)


    begin_wf_item (index = 10, is_custom_code = True, name = "Add_markers")
    for part in get_all_markers ():
    	if part.name.count('MULT')>=1 and part.name[-1]!='_':
    		HOR.append(part)

    HOR.append(get_all_markers ()[-1])

    for part in range(1,len(HOR)):
    	if marker_exists (name=f"MULT_ZONE_{part-1}_"):
    		print(part)
    		marker_calculator (result_well_marker=find_object (name=f"MULT_ZONE_{part}",
          type="WellMarker"),
          use_well_filter=False,
          well_filter=find_object (name="Import Model Well Filter(BLACK_OIL_DEMO)",
          type="WellFilter"),
          trajectories=find_object (name="Trajectories",
          type="Trajectories"),
          formula=f"if (MULT_ZONE_{part}==U,MULT_ZONE_{part-1}_,MULT_ZONE_{part})",
          variables=variables)
    end_wf_item (index = 10)


    begin_wf_item (index = 11, is_custom_code = True, name = "Create mult table")
    create_table (name=MUTL_TABLE_NAME, overwrite_existing=True)
    get_table_by_name (name=MUTL_TABLE_NAME).set_size (r_count=len (get_all_wells ())*(len(HOR)-1) + 1, c_count=4)

    end_wf_item (index = 11)


    begin_wf_item (index = 12)
    for A in range(len(HOR)-1):
        pass
        set_var_type (n = "A", t = "INTEGER", it = "PY_EXPR", val = A)
        variables["A"] = A
        TOP = HOR[A]
        set_var_type (n = "TOP", t = "PY_EXPR", it = "PY_EXPR", val = TOP)
        BOT = HOR[A+1]
        set_var_type (n = "BOT", t = "PY_EXPR", it = "PY_EXPR", val = BOT)
        begin_loop_iteration (info = "A = " + str (A))



        begin_wf_item (index = 13, is_custom_code = True, name = "Create dict")
        PARAMS.append({"top_marker" : find_object (name=TOP.name, type="WellMarker"), 
        "bottom_marker" : find_object (name=BOT.name, type="WellMarker"),
        "interval_name" : TOP.name},
        )

        end_wf_item (index = 13)


        end_loop_iteration ()

    end_wf_item (index = 12)


    begin_wf_item (index = 15, is_custom_code = True, name = "Create table")
    log_statistics_table (result_table=find_object (name="Wells",
                  type="Table"),
                  use_append_table=False,
                  append_table="rows",
                  source_log=find_object (name="MD",
                  type="WellLog"),
                  statistics_type="weighted_by_length",
                  use_well_filter=False,
                  well_filter=find_object (name="All Wells",
                  type="WellFilter"),
                  wells=find_object (name="Wells",
                  type="gt_wells_entity"),
                  trajectories=find_object (name="Trajectories",
                  type="Trajectories"),
                  intervals_table=PARAMS)

    end_wf_item (index = 15)


    begin_wf_item (index = 16)
    fill_table (data_table=[{"filled_table" : find_object (name=resolve_variables_in_string (string_with_variables="@MUTL_TABLE_NAME@",
          variables=variables),
          type="Table"), "row" : 1, "column" : 1, "data" : "WELL"}, {"filled_table" : find_object (name=resolve_variables_in_string (string_with_variables="@MUTL_TABLE_NAME@",
          variables=variables),
          type="Table"), "row" : 1, "column" : 2, "data" : "ZONE"}, {"filled_table" : find_object (name=resolve_variables_in_string (string_with_variables="@MUTL_TABLE_NAME@",
          variables=variables),
          type="Table"), "row" : 1, "column" : 3, "data" : "MD_TOP"}, {"filled_table" : find_object (name=resolve_variables_in_string (string_with_variables="@MUTL_TABLE_NAME@",
          variables=variables),
          type="Table"), "row" : 1, "column" : 4, "data" : "MD_BOT"}, {"filled_table" : find_object (name=resolve_variables_in_string (string_with_variables="@MUTL_TABLE_NAME@",
          variables=variables),
          type="Table"), "row" : 1, "column" : 5, "data" : "MULT"}])
    end_wf_item (index = 16)


    begin_wf_item (index = 17)
    for B in range(1,get_table_by_name (name="Wells").get_row_count ()+1,1):
        pass
        set_var_type (n = "B", t = "INTEGER", it = "PY_EXPR", val = B)
        variables["B"] = B
        begin_loop_iteration (info = "B = " + str (B))



        if get_table_by_name (name="Wells").get_data (row=B, column=2) != "Интегрально":
            if_statement_contents ()
            begin_wf_item (index = 18)


            begin_wf_item (index = 19, is_custom_code = True, name = "Populate table")
            exec ("""
WELL_NAME = str(get_table_by_name (name=\"Wells\").get_data (row=B, column=1))
ZONE_NAME = get_table_by_name (name=\"Wells\").get_data (row=B, column=2)
TOP = get_table_by_name (name=\"Wells\").get_data (row=B, column=4)
BOT = get_table_by_name (name=\"Wells\").get_data (row=B, column=5)

get_table_by_name (name=MUTL_TABLE_NAME).set_data (row=COUNTER, column=1, data=WELL_NAME)
get_table_by_name (name=MUTL_TABLE_NAME).set_data (row=COUNTER, column=2, data=ZONE_NAME)
get_table_by_name (name=MUTL_TABLE_NAME).set_data (row=COUNTER, column=3, data=TOP)
get_table_by_name (name=MUTL_TABLE_NAME).set_data (row=COUNTER, column=4, data=BOT)
get_table_by_name (name=MUTL_TABLE_NAME).set_data (row=COUNTER, column=5, data=\'1\')


COUNTER += 1 vw
""")
            end_wf_item (index = 19)


            end_wf_item (index = 18)


        end_loop_iteration ()

    end_wf_item (index = 17)


    begin_wf_item (index = 22, name = "Блок для формирования куба мультов")
    comment_text ("""



""")
    end_wf_item (index = 22)


    if False:
        begin_wf_item (index = 23)
        marker_calculator (use_current_marker_set=False,
              current_marker_set=find_object (name="",
              type="MarkerSet"),
              result_well_marker=find_object (name="MULT_ZONE_3",
              type="WellMarker"),
              use_well_filter=False,
              well_filter=find_object (name="Import Model Well Filter(BLACK_OIL_DEMO)",
              type="WellFilter"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              formula="if (MULT_ZONE_3==U,MULT_ZONE_2_,MULT_ZONE_3)",
              variables=variables)
        end_wf_item (index = 23)


