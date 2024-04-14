#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="POST",
      variables=[])


POST_variables = {

}

def POST (variables = POST_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    import getpass
    import os
    from datetime import datetime
    import pandas as pd
    from pathlib import Path
    end_user_imports ()

    begin_wf_item (index = 1)
    create_blocked_well_log_by_connection (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
          type="gt_tnav_grid_3d_data"),
          wells=find_object (name="Wells",
          type="gt_wells_entity"),
          blocked_wells_table=[{"param_id" : "CONN_CALC_WATER_RATE", "blocked_wells" : find_object (name="QWAT",
          type="BlockedWells")}, {"param_id" : "CONN_CALC_GAS_FLOW_RATE", "blocked_wells" : find_object (name="Qgas",
          type="BlockedWells")}])
    end_wf_item (index = 1)


    begin_wf_item (index = 2)
    create_blocked_well_log_by_property (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
          type="gt_tnav_grid_3d_data"),
          result_grid_property=find_object (name="SGAS",
          type="gt_tnav_cube_3d_data"),
          BlockedWells=find_object (name="Sg",
          type="BlockedWells"),
          use_well_filter=False,
          well_filter=find_object (name="Well Filter 1",
          type="WellFilter"),
          wells=find_object (name="Wells",
          type="gt_wells_entity"),
          clear_all_values=True)
    end_wf_item (index = 2)


    begin_wf_item (index = 3)
    wells_log_create_by_blocked_wells (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
          type="gt_tnav_grid_3d_data"),
          blocked_wells=find_object (name="QWAT",
          type="BlockedWells"),
          log_step_type="use_bw_step",
          log_step_val=1,
          source_log=find_object (name="AHF10",
          type="WellLog"),
          result_log=find_object (name="RFT_model",
          type="WellLog"),
          wells=find_object (name="Wells",
          type="gt_wells_entity"),
          trajectories=find_object (name="Trajectories",
          type="Trajectories"),
          use_well_filter=False,
          well_filter=find_object (name="AchDev",
          type="WellFilter"),
          use_filter=False,
          user_cut=find_object (name="Depths of all blocks (INIT)",
          type="gt_ecl_cube_3d_data"),
          comparator=Comparator (rule="not_equals",
          value=0),
          clear_existing_data=False)
    end_wf_item (index = 3)


    begin_wf_item (index = 4)
    wells_log_create_by_blocked_wells (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
          type="gt_tnav_grid_3d_data"),
          blocked_wells=find_object (name="Qgas",
          type="BlockedWells"),
          log_step_type="use_bw_step",
          log_step_val=1,
          source_log=find_object (name="AHF10",
          type="WellLog"),
          result_log=find_object (name="Qgas_model",
          type="WellLog"),
          wells=find_object (name="Wells",
          type="gt_wells_entity"),
          trajectories=find_object (name="Trajectories",
          type="Trajectories"),
          use_well_filter=False,
          well_filter=find_object (name="AchDev",
          type="WellFilter"),
          use_filter=False,
          user_cut=find_object (name="Depths of all blocks (INIT)",
          type="gt_ecl_cube_3d_data"),
          comparator=Comparator (rule="not_equals",
          value=0),
          clear_existing_data=False)
    end_wf_item (index = 4)


    begin_wf_item (index = 5)
    wells_log_create_by_blocked_wells (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
          type="gt_tnav_grid_3d_data"),
          blocked_wells=find_object (name="Sg",
          type="BlockedWells"),
          log_step_type="use_bw_step",
          log_step_val=1,
          source_log=find_object (name="AHF10",
          type="WellLog"),
          result_log=find_object (name="Sg_gdm",
          type="WellLog"),
          wells=find_object (name="Wells",
          type="gt_wells_entity"),
          trajectories=find_object (name="Trajectories",
          type="Trajectories"),
          use_well_filter=False,
          well_filter=find_object (name="AchDev",
          type="WellFilter"),
          use_filter=False,
          user_cut=find_object (name="Depths of all blocks (INIT)",
          type="gt_ecl_cube_3d_data"),
          comparator=Comparator (rule="not_equals",
          value=0),
          clear_existing_data=False)
    end_wf_item (index = 5)


    begin_wf_item (index = 6, name = "Анализ по С5+")
    workflow_folder ()
    if True:
        pass



        begin_wf_item (index = 7, name = "Скрипт импорта данных C5+")
        run_graph_calculator (gc_code="from datetime import datetime\nimport getpass\nimport os\nfrom datetime import datetime\nimport pandas as pd\nfrom pathlib import Path\n\nfile_name = \'PS_C5+.txt\'\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\nfile=open(file_name,\"r\")\nevent=graph(type = \'well\', default_value = 0)\n\nfor line in file:\n	column=line.split()\n	try:\n		w = get_well_by_name(str(column[0]))\n		t=get_timestep_from_datetime (datetime.strptime(str(column[1]), \'%Y-%m-%d\'), mode = \'nearest\')\n		event[w, t]=float(column[2])\n		print(f\'{line}\')\n	except:\n		print(f\'wrong value {line}\')\n\nexport(event, name = \'PS_C5_hist\')",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 7)


        begin_wf_item (index = 8, name = "Скрипт графика с потенциальным содержанием C5+")
        run_graph_calculator (gc_code="#пишите здесь ваш код\n \nPS_C5=graph (type = \'well\', default_value =0)\n \ncomp_vector = {\'C1\': wzmf_1,\n\'C2\':wzmf_2,\n\'C3\':wzmf_3,\n\'C4\':wzmf_4,\n\'C5\':wzmf_5,\n\'C6C9\':wzmf_6,\n\'C10C17\':wzmf_7,\n\'C18C26\':wzmf_8,\n\'C27C35\':wzmf_9,\n\'C36+\':wzmf_10}\n \n \nmolar_mass = {\'C1\':16.07206,\n\'C2\':31.25047,\n\'C3\':44.1,\n\'C4\':58.123,\n\'C5\':72.15,\n\'C6C9\':97.1868805753736,\n\'C10C17\':169.378770746473,\n\'C18C26\':292.498542960907,\n\'C27C35\':440.291109266961,\n\'C36+\':596.424190205972}\n \nc5=[n for n in comp_vector.keys()]\nprint(c5[4:])\n \nfor w in get_all_wells ():\n	for c in c5[4:]:\n		PS_C5[w]=PS_C5[w]+(comp_vector[c][w]*molar_mass[c])\n	PS_C5[w] = PS_C5[w]/0.02404\n \nexport(PS_C5,name=\'PS_C5_model\',units=\"no\")",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 8)


        begin_wf_item (index = 9, name = "Скрипт графика с расчетом дельты C5+")
        run_graph_calculator (gc_code="#пишите здесь ваш код\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\n\nps_model = get_global_graph (name = \'PS_C5_model\')\nps_hist = get_global_graph (name = \'PS_C5_hist\')\n\ndelta_PS=graph (type = \'well\', default_value =0)\ndelta_PS_avg=graph (type = \'well\', default_value =0)\ndelta_PS_otn=graph (type = \'well\', default_value =0)\n\n\nfor w in get_all_wells ():\n	deltas_abs=[]\n	deltas_otn=[]\n	for t in get_all_timesteps():\n		if ps_model[w,t]>0 and ps_hist[w,t]>0:\n			delta_PS[w,t]=ps_hist[w,t]-ps_model[w,t]\n			deltas_abs.append(ps_hist[w,t]-ps_model[w,t])\n			deltas_otn.append((ps_hist[w,t]-ps_model[w,t])/ps_hist[w,t])\n		if len(deltas_abs)>0:\n			delta_PS_avg[w]=sum(deltas_abs)/len(deltas_abs)\n			delta_PS_otn[w]=sum(deltas_otn)/len(deltas_abs)*100\n\n \nexport(delta_PS,name=\'PS_delta\',units=\"no\")\nexport(delta_PS_avg,name=\'PS_delta_avg\',units=\"no\")\nexport(delta_PS_otn,name=\'PS_delta_otn\',units=\"no\")\n\nfor graph in [\'PS_delta_avg\', \'PS_delta_otn\']:\n	ps = get_global_graph (name = graph)\n	df = ps.to_dataframe ()\n	df = df.groupby(\'Скважины\')[\'Значение\'].agg(\'mean\')\n	df.to_csv(f\'{graph}.txt\', sep=\'\\t\')",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 9)


        begin_wf_item (index = 10, is_custom_code = True, name = "Переносим в атрибуты для карты")
        from datetime import datetime
        from pathlib import Path


        def create_report_dir(path):
            path = Path(path)
            path = path.joinpath('reports')
            path.mkdir(parents=True, exist_ok=True)
            os.chdir(path)


        create_report_dir(get_project_folder ( ))


        def create_attr_from_file(file_name, attr_name, marker_name, create_attr=False):
        	if create_attr==True:
        		create_well_attribute (name=attr_name, overwrite_existing=True)
        	else:
        		pass
        	attr=get_well_attribute_by_name (name=attr_name)
        	marker = get_marker_by_name (name=marker_name)
        	with open(file_name,"r") as f:
        		for line in f:
        			column=line.split()
        			try:
        				w = get_well_by_name(name = str(column[0]))
        				if float(column[1])!=0:
        					attr.set_value(md=float(marker.get_points(well=w)[0]), value=float(column[1]), wellbore=w.get_wellbores ()[0], overwrite_existing=True)
        			except:
        				continue
        				
        				
        for graph in ['PS_delta_avg', 'PS_delta_otn']:
        	create_attr_from_file(f'{graph}.txt', graph, 'Ach3_top')
        	
        #create_attr_from_file(r'/home/albert.vafin/Documents/UNGKM/test/CUSTOM/PS_C5_for_map.csv', 'PC_GKI', 'Ach3_top', create_attr=True)
        end_wf_item (index = 10)


        begin_wf_item (index = 11)
        map_2d_interpolate (result_map_2d=find_object (name="PS_delta_abs",
              type="Map2d"),
              use_source_pointset=False,
              source_pointset=find_object (name="Source_Points",
              type="PointSet3d"),
              use_residual_attribute=False,
              residual_attribute=find_object (name="Residual",
              type="PointsetAttribute"),
              overwrite_pointset=True,
              attributes_group_box=True,
              well_atributes_table=[{"use" : True, "well_attribute" : find_object (name="PS_delta_avg",
              type="WellAttribute")}],
              use_well_filter=False,
              well_filter=find_object (name="ExpWells",
              type="WellFilter"),
              pointset_attributes_group_box=False,
              pointset_attributes_table=[],
              maps_group_box=True,
              maps_table=[{"use" : False, "map" : find_object (name="Old_petro",
              type="Map2d")}],
              polygons_group_box=True,
              polygons_table=[],
              fault_polygons_group_box=False,
              fault_polygons_table=[],
              seam_with_LS=False,
              simplify_faults_geometry=True,
              simplify_extension=False,
              wells=find_object (name="Wells",
              type="gt_wells_entity"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              use_trend_map=False,
              trend_map=find_object (name="distance",
              type="Map2d"),
              grid_2d_settings=Grid2DSettings (grid_2d_settings_shown=True,
              autodetect_box=True,
              min_x=573648.5762539159,
              min_y=7351627.100932668,
              length_x=29176.221745807212,
              length_y=61342.29204871226,
              margin_x=0,
              margin_y=0,
              consider_blank_nodes=False,
              autodetect_angle=True,
              angle=6.696227728206645,
              autodetect_grid=False,
              grid_adjust_mode="step",
              step_x=50,
              step_y=50,
              counts_x=0,
              counts_y=0,
              sample_object=absolute_object_name (name=None,
              typed_names=[typed_object_name (obj_name="2km_area",
              obj_type="Curve3d")]),
              autodetect_during_wf_calculation=True),
              target_func_resampling=True,
              use_polygon=False,
              polygon=find_object (name="1A_4A_5A",
              type="Curve3d"),
              interpolation_type="idw",
              power_parameter=3,
              idw_azimuth=0,
              idw_axis_ratio=1,
              kriging_mode="simple",
              use_kriging_global_mean=False,
              kriging_global_mean=0,
              kriging_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=2000,
              range_normal=2000,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type="Map2d"),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              use_kriging_points_count=False,
              kriging_points_count=50,
              first_derivative_coefficient=0.2,
              second_derivative_coefficient=0.02,
              use_advanced=False,
              do_grid_refinement=True,
              refinement_steps=20,
              start_nx=10,
              start_ny=10,
              do_drag=True,
              drag_iterations=8,
              drag_coefficient=0.4,
              sgs_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=1,
              range_normal=1,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type=""),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              kriging_radius=0,
              kriging_points=10,
              random_seed=0,
              sgs_transform_distribution=True,
              sgs_distribution_type="source_data",
              sgs_mean=0,
              sgs_stdev=1,
              sgs_alpha=1,
              sgs_beta=1,
              sgs_beta_use_shift_stretch_from_input=True,
              sgs_shift=0,
              sgs_stretch=1,
              sgs_uniform_min=0,
              sgs_uniform_max=0,
              grfs_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=1,
              range_normal=1,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type=""),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              use_kriging_points_grfs=False,
              kriging_points_grfs=50,
              random_seed_grfs=0,
              grfs_transform_distribution=True,
              grfs_distribution_type="source_data",
              grfs_mean=0,
              grfs_stdev=1,
              grfs_alpha=1,
              grfs_beta=1,
              grfs_beta_use_shift_stretch_from_input=True,
              grfs_shift=0,
              grfs_stretch=1,
              grfs_uniform_min=0,
              grfs_uniform_max=0,
              amazonas_params=AmazonasParameters (major_axis_src_type="value",
              major_semi_axis=250,
              major_semi_axis_blocks=5,
              major_semi_axis_map=find_object (name="",
              type=""),
              lateral_anizotropy=False,
              major_minor_src_type="value",
              major_minor_ratio=1,
              major_minor_ratio_map=find_object (name="",
              type=""),
              azimuth_src_type="value",
              azimuth=0,
              azimuth_map=find_object (name="",
              type=""),
              vertical_axis_src_type="map",
              vertical_semi_axis=5,
              vertical_semi_axis_blocks=2,
              dip=0,
              random_seed=0,
              aposteriori_drift_src_type="value",
              aposteriori_drift=0.0001,
              noise_map=find_object (name="",
              type=""),
              advanced_params=False,
              axis_units_src_type="length",
              use_apriori_drift=False,
              apriori_drift=0,
              min_threshold=5,
              src_points_weight=5,
              amazonas_stat_type="median",
              kernel_bandwidth=0.5),
              refinement_ratio=1.5,
              convergent_use_advanced=False,
              convergent_initial_approx_degree=0,
              convergent_initial_grid_size=2,
              accuracy=95,
              use_filter=False,
              filter=500,
              smooth_power=0.5,
              use_les_smoothing=True,
              linear_tensioning_deg=1,
              faster_convergence=True,
              use_max_iterations_num=False,
              max_iterations_num=100,
              pre_defined_params="normal",
              polynom_degree=1,
              use_local_diagram_update=False,
              global_splines_alpha=0.1,
              global_splines_solver_accuracy=1e-10,
              rbf_type="inverse_multiquadric",
              rbf_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=1,
              range_normal=1,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type=""),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              use_rbf_points=False,
              rbf_points=50,
              use_min_z=False,
              min_z=0,
              use_max_z=False,
              max_z=0.93)
        end_wf_item (index = 11)


        begin_wf_item (index = 12)
        map_2d_interpolate (result_map_2d=find_object (name="PS_delta_otn",
              type="Map2d"),
              use_source_pointset=False,
              source_pointset=find_object (name="Source_Points",
              type="PointSet3d"),
              use_residual_attribute=False,
              residual_attribute=find_object (name="Residual",
              type="PointsetAttribute"),
              overwrite_pointset=True,
              attributes_group_box=True,
              well_atributes_table=[{"use" : True, "well_attribute" : find_object (name="PS_delta_otn",
              type="WellAttribute")}],
              use_well_filter=False,
              well_filter=find_object (name="ExpWells",
              type="WellFilter"),
              pointset_attributes_group_box=False,
              pointset_attributes_table=[],
              maps_group_box=True,
              maps_table=[{"use" : False, "map" : find_object (name="Old_petro",
              type="Map2d")}],
              polygons_group_box=True,
              polygons_table=[],
              fault_polygons_group_box=False,
              fault_polygons_table=[],
              seam_with_LS=False,
              simplify_faults_geometry=True,
              simplify_extension=False,
              wells=find_object (name="Wells",
              type="gt_wells_entity"),
              trajectories=find_object (name="Trajectories",
              type="Trajectories"),
              use_trend_map=False,
              trend_map=find_object (name="distance",
              type="Map2d"),
              grid_2d_settings=Grid2DSettings (grid_2d_settings_shown=True,
              autodetect_box=True,
              min_x=573648.5762539159,
              min_y=7351627.100932668,
              length_x=29176.221745807212,
              length_y=61342.29204871226,
              margin_x=0,
              margin_y=0,
              consider_blank_nodes=False,
              autodetect_angle=True,
              angle=6.696227728206645,
              autodetect_grid=False,
              grid_adjust_mode="step",
              step_x=50,
              step_y=50,
              counts_x=0,
              counts_y=0,
              sample_object=absolute_object_name (name=None,
              typed_names=[typed_object_name (obj_name="2km_area",
              obj_type="Curve3d")]),
              autodetect_during_wf_calculation=True),
              target_func_resampling=True,
              use_polygon=False,
              polygon=find_object (name="1A_4A_5A",
              type="Curve3d"),
              interpolation_type="idw",
              power_parameter=3,
              idw_azimuth=0,
              idw_axis_ratio=1,
              kriging_mode="simple",
              use_kriging_global_mean=False,
              kriging_global_mean=0,
              kriging_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=2000,
              range_normal=2000,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type="Map2d"),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              use_kriging_points_count=False,
              kriging_points_count=50,
              first_derivative_coefficient=0.2,
              second_derivative_coefficient=0.02,
              use_advanced=False,
              do_grid_refinement=True,
              refinement_steps=20,
              start_nx=10,
              start_ny=10,
              do_drag=True,
              drag_iterations=8,
              drag_coefficient=0.4,
              sgs_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=1,
              range_normal=1,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type=""),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              kriging_radius=0,
              kriging_points=10,
              random_seed=0,
              sgs_transform_distribution=True,
              sgs_distribution_type="source_data",
              sgs_mean=0,
              sgs_stdev=1,
              sgs_alpha=1,
              sgs_beta=1,
              sgs_beta_use_shift_stretch_from_input=True,
              sgs_shift=0,
              sgs_stretch=1,
              sgs_uniform_min=0,
              sgs_uniform_max=0,
              grfs_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=1,
              range_normal=1,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type=""),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              use_kriging_points_grfs=False,
              kriging_points_grfs=50,
              random_seed_grfs=0,
              grfs_transform_distribution=True,
              grfs_distribution_type="source_data",
              grfs_mean=0,
              grfs_stdev=1,
              grfs_alpha=1,
              grfs_beta=1,
              grfs_beta_use_shift_stretch_from_input=True,
              grfs_shift=0,
              grfs_stretch=1,
              grfs_uniform_min=0,
              grfs_uniform_max=0,
              amazonas_params=AmazonasParameters (major_axis_src_type="value",
              major_semi_axis=250,
              major_semi_axis_blocks=5,
              major_semi_axis_map=find_object (name="",
              type=""),
              lateral_anizotropy=False,
              major_minor_src_type="value",
              major_minor_ratio=1,
              major_minor_ratio_map=find_object (name="",
              type=""),
              azimuth_src_type="value",
              azimuth=0,
              azimuth_map=find_object (name="",
              type=""),
              vertical_axis_src_type="map",
              vertical_semi_axis=5,
              vertical_semi_axis_blocks=2,
              dip=0,
              random_seed=0,
              aposteriori_drift_src_type="value",
              aposteriori_drift=0.0001,
              noise_map=find_object (name="",
              type=""),
              advanced_params=False,
              axis_units_src_type="length",
              use_apriori_drift=False,
              apriori_drift=0,
              min_threshold=5,
              src_points_weight=5,
              amazonas_stat_type="median",
              kernel_bandwidth=0.5),
              refinement_ratio=1.5,
              convergent_use_advanced=False,
              convergent_initial_approx_degree=0,
              convergent_initial_grid_size=2,
              accuracy=95,
              use_filter=False,
              filter=500,
              smooth_power=0.5,
              use_les_smoothing=True,
              linear_tensioning_deg=1,
              faster_convergence=True,
              use_max_iterations_num=False,
              max_iterations_num=100,
              pre_defined_params="normal",
              polynom_degree=1,
              use_local_diagram_update=False,
              global_splines_alpha=0.1,
              global_splines_solver_accuracy=1e-10,
              rbf_type="inverse_multiquadric",
              rbf_variogram_params=VariogramParameters (variogram_type="exponential",
              sill=1,
              nugget_effect=0,
              range_main=1,
              range_normal=1,
              range_vertical=1,
              azimuth=0,
              dip=0,
              azimuth_map=find_object (name="",
              type=""),
              use_azimuth_map=False,
              external_source=False,
              space_type="xyz",
              sill_map=find_object (name="",
              type=""),
              use_sill_map=False,
              source_object=find_object (name="",
              type="")),
              use_rbf_points=False,
              rbf_points=50,
              use_min_z=False,
              min_z=0,
              use_max_z=False,
              max_z=0.93)
        end_wf_item (index = 12)


        begin_wf_item (index = 13)
        polygon_create_by_map_intersection (result_polygon=find_object (name="PS_above_20",
              type="Curve3d"),
              top_z_type="map",
              top=find_object (name="PS_delta_otn",
              type="Map2d"),
              top_depth=0,
              bottom_z_type="depth",
              bottom=find_object (name="distance",
              type="Map2d"),
              bottom_depth=10)
        end_wf_item (index = 13)


        begin_wf_item (index = 14)
        polygon_create_by_map_intersection (result_polygon=find_object (name="PS_below_20",
              type="Curve3d"),
              top_z_type="map",
              top=find_object (name="PS_delta_otn",
              type="Map2d"),
              top_depth=0,
              bottom_z_type="depth",
              bottom=find_object (name="distance",
              type="Map2d"),
              bottom_depth=-10)
        end_wf_item (index = 14)


        if False:
            begin_wf_item (index = 15)
            switch_time_step (step_number=0)
            end_wf_item (index = 15)


        if False:
            begin_wf_item (index = 16)
            grid_property_calculator (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
                  type="gt_tnav_grid_3d_data"),
                  result_grid_property=find_object (name="PS5-plus",
                  type="Grid3dProperty"),
                  discrete_output=False,
                  use_filter=False,
                  user_cut_for_filter=find_object (name="ARRMUL~1 (INIT)",
                  type="gt_ecl_cube_3d_data"),
                  filter_comparator=Comparator (rule="not_equals",
                  value=0),
                  formula="(dynamic_property (\"YMFC5\")*72.15+\ndynamic_property (\"YMFC6C9\")*97.1868805753736+\ndynamic_property (\"YMFC10C17\")*169.378770746473+\ndynamic_property (\"YMFC18C26\")*292.498542960907+\ndynamic_property (\"YMFC27C35\")*440.291109266961+\ndynamic_property (\"YMFC36+\")*596.42419020597)/0.02404",
                  variables=variables)
            end_wf_item (index = 16)


        if False:
            begin_wf_item (index = 17)
            grid_property_calculator (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
                  type="gt_tnav_grid_3d_data"),
                  result_grid_property=find_object (name="PS5-plus",
                  type="Grid3dProperty"),
                  discrete_output=False,
                  use_filter=False,
                  user_cut_for_filter=find_object (name="ARRMUL~1 (INIT)",
                  type="gt_ecl_cube_3d_data"),
                  filter_comparator=Comparator (rule="not_equals",
                  value=0),
                  formula="(dynamic_property (\"YMFC5\")*72.15+\ndynamic_property (\"YMFC6C9\")*97.1868805753736+\ndynamic_property (\"YMFC10C17\")*169.378770746473+\ndynamic_property (\"YMFC18C26\")*292.498542960907+\ndynamic_property (\"YMFC27C35\")*440.291109266961+\ndynamic_property (\"YMFC36+\")*596.42419020597)/0.02404",
                  variables=variables)
            end_wf_item (index = 17)


        if False:
            begin_wf_item (index = 18)
            wells_log_create_by_grid_property (mesh=find_object (name="SHORT_AREA (Dynamic Model)",
                  type="gt_tnav_grid_3d_data"),
                  grid_property=find_object (name="PS5-plus",
                  type="Grid3dProperty"),
                  log_step_type="set_log_step",
                  log_step_val=0.1,
                  source_log=find_object (name="AHF10",
                  type="WellLog"),
                  result_log=find_object (name="PS_FROM_GDM",
                  type="WellLog"),
                  wells=find_object (name="Wells",
                  type="gt_wells_entity"),
                  trajectories=find_object (name="Trajectories",
                  type="Trajectories"),
                  use_well_filter=False,
                  well_filter=find_object (name="AchDev",
                  type="WellFilter"))
            end_wf_item (index = 18)


        if False:
            begin_wf_item (index = 19)
            wells_attribute_create_by_wells_log_value (result_well_attribute=find_object (name="PC_ACH3_MODEL",
                  type="WellAttribute"),
                  well_log=find_object (name="PS_FROM_GDM",
                  type="WellLog"),
                  use_current_marker_set=False,
                  current_marker_set=find_object (name="Default Set",
                  type="MarkerSet"),
                  marker=find_object (name="ACH3+3",
                  type="WellMarker"),
                  use_well_filter=False,
                  well_filter=find_object (name="AchDev",
                  type="WellFilter"),
                  wells=find_object (name="Wells",
                  type="gt_wells_entity"),
                  trajectories=find_object (name="Trajectories",
                  type="Trajectories"),
                  use_override_discreteness=True,
                  override_discreteness="Continuous",
                  use_no_log_value=False,
                  no_log_value=0)
            end_wf_item (index = 19)



    end_wf_item (index = 6)


    if False:
        begin_wf_item (index = 21, name = "ПГИ")
        workflow_folder ()
        if True:
            pass



            if False:
                begin_wf_item (index = 22, name = "Скрипт оценки доли притока по пластам в модели")
                run_graph_calculator (gc_code="#пишите здесь ваш код\n# Automaticaly recalculate=true\n# Single model=false\n# Run for one model=false\n# Rock Flow Dynamics (R)\n##################################################\n################ Input Section ###################\n##################################################\n# Set up layers\nzones = [115, 335]\n##################################################\n################ Script Section ##################\n##################################################\n\nfor i in range(len(zones)):\n    rel_gas_rate = graph(type=\'well\', default_value=0)\n    #rel_oil_rate = graph(type=\'well\', default_value=0)\n   # layer_oil_rate = graph(type=\'well\', default_value=0)\n    layer_gas_rate = graph(type=\'well\', default_value=0)\n    if i == 0:\n        k1 = 1\n    else:\n        k1 = zones[i-1]+1\n    k2 = zones[i]\n    for w in get_all_wells():\n        for c in (w.connections + w.virtual_connections):\n            if c.k >= k1 and c.k < k2:\n                layer_gas_rate[w] += cgpr[c]\n                #layer_oil_rate[w] += copt[c]\n        rel_gas_rate[w] = layer_gas_rate[w]\n        #rel_oil_rate[w] = layer_oil_rate[w]/wopt[w]\n    export(rel_gas_rate, name=\'tot_gas_rate_layers_\' +\n           str(k1)+\'-\'+str(k2), units=\"no\")\n    #export(rel_oil_rate, name=\'tot_oil_rate_layers_\' +\n           #str(k1)+\'-\'+str(k2), units=\"no\")",
                      font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
                      models=["SHORT_AREA:UNGKM_13_big"],
                      variables=variables)
                end_wf_item (index = 22)


            if False:
                begin_wf_item (index = 23, name = "Скрипт импорта данных по притокам с Ач-5")
                run_graph_calculator (gc_code="from datetime import datetime\nimport getpass\nimport os\nfrom datetime import datetime\nimport pandas as pd\nfrom pathlib import Path\n\nfile_name = \'a5_PGI.csv\'\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\ndata = pd.read_csv(file_name, header=0, sep=\',\',names=[\'well\',\'date\',\'value\'])\ndata[\'date\'] = pd.to_datetime(data[\'date\'],format=\"%Y-%m-%d\")\ndata = data.loc[data.date<=\'31.12.2022\']\nprint(data)\n\nhist = graph_from_dataframe (type=\'well\',default_value= 0.0, dataframe= data, object = \'well\', date=\'date\', value=\'value\')\n\nexport(hist, name=\'ach5_work\')\n",
                      font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
                      models=["SHORT_AREA:UNGKM_13_big"],
                      variables=variables)
                end_wf_item (index = 23)


            if False:
                begin_wf_item (index = 24, name = "Скрипт расчета отклонений по притокам")
                run_graph_calculator (gc_code="#пишите здесь ваш код\nfrom pathlib import Path\nimport pandas as pd\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\npgi_ach5_hist = get_global_graph (name = \'ach5_work\')\npgi_ach5_model = get_global_graph (name = \'tot_gas_rate_layers_232-335\')\n\nhist = pgi_ach5_hist.to_dataframe ()\nmodel = pgi_ach5_model.to_dataframe ()\nprint(hist.columns)\nconcated = pd.merge(left=hist, right=model, on=[\'Скважины\',\'Дата\'])\nconcated.columns=[\'date\', \'well\', \'history\', \'model\']\nconcated=concated.loc[concated.history>0]\n#.to_csv(\'rate_from_model.csv\', sep=\',\')\n# %% отклонение считает по среднему \nto_model = concated.loc[:, [\'well\', \'history\', \'model\']].groupby(\'well\').agg(\'mean\')\nto_model[\'pgi_otn\'] = (to_model.history-to_model.model)/to_model.history*100\nto_model[\'pgi_abs\'] = (to_model.history-to_model.model)*100\nto_model[\'model\'] = to_model[\'model\']*100\nto_model[\'history\'] = to_model[\'history\']*100\nprint(to_model)\n# %%\nto_model.reset_index().to_csv(\'pgi_model.csv\')\n#",
                      font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
                      models=["SHORT_AREA:UNGKM_13_big"],
                      variables=variables)
                end_wf_item (index = 24)


            if False:
                begin_wf_item (index = 25, is_custom_code = True, name = "Переносим в атрибуты для карты")
                from datetime import datetime
                from pathlib import Path


                def create_report_dir(path):
                    path = Path(path)
                    path = path.joinpath('reports')
                    path.mkdir(parents=True, exist_ok=True)
                    os.chdir(path)


                create_report_dir(get_project_folder ( ))


                def create_attr_from_dataframe(df, well_coll, target_coll, attr_name, marker_name, create_attr=False):
                	if create_attr==True:
                		create_well_attribute (name=attr_name, overwrite_existing=True)
                	else:
                		pass
                	attr=get_well_attribute_by_name (name=attr_name)
                	marker = get_marker_by_name (name=marker_name)
                	for _, row in df[[well_coll, target_coll]].iterrows():
                		try:
                			w = get_well_by_name(name = str(row[well_coll]))
                			#if float(column[1])!=0:
                			attr.set_value(md=float(marker.get_points(well=w)[0]), value=float(row[target_coll]), wellbore=w.get_wellbores ()[0], overwrite_existing=True)
                		except:
                			print(f'не удалось подгрузить скважину {row[well_coll]}')
                			continue
                				
                pgi_frame = pd.read_csv('pgi_model.csv')

                for coll in pgi_frame.columns[2:]:
                	print(f'pgi_{coll}')
                	create_attr_from_dataframe(pgi_frame, 'well', coll, f'pgi_{coll}', 'Ach3_top', create_attr=False)
                	

                #core =  pd.read_csv(r'/home/albert.vafin/Документы/UNGKM/UNGKM_RES_ENG2/reports/core_ach5_to_attr.csv')
                #create_attr_from_dataframe(core, 'well', 'samples', 'Ach5_core', 'Ach3_top', create_attr=True)
                end_wf_item (index = 25)


            if False:
                begin_wf_item (index = 26)
                map_2d_interpolate (result_map_2d=find_object (name="pgi_delta_abs",
                      type="Map2d"),
                      use_source_pointset=False,
                      source_pointset=find_object (name="Source_Points",
                      type="PointSet3d"),
                      use_residual_attribute=False,
                      residual_attribute=find_object (name="Residual",
                      type="PointsetAttribute"),
                      overwrite_pointset=True,
                      attributes_group_box=True,
                      well_atributes_table=[{"use" : True, "well_attribute" : find_object (name="pgi_pgi_abs",
                      type="WellAttribute")}],
                      use_well_filter=False,
                      well_filter=find_object (name="ExpWells",
                      type="WellFilter"),
                      pointset_attributes_group_box=False,
                      pointset_attributes_table=[],
                      maps_group_box=True,
                      maps_table=[{"use" : False, "map" : find_object (name="Old_petro",
                      type="Map2d")}],
                      polygons_group_box=True,
                      polygons_table=[],
                      fault_polygons_group_box=False,
                      fault_polygons_table=[],
                      seam_with_LS=False,
                      simplify_faults_geometry=True,
                      simplify_extension=False,
                      wells=find_object (name="Wells",
                      type="gt_wells_entity"),
                      trajectories=find_object (name="Trajectories",
                      type="Trajectories"),
                      use_trend_map=False,
                      trend_map=find_object (name="distance",
                      type="Map2d"),
                      grid_2d_settings=Grid2DSettings (grid_2d_settings_shown=True,
                      autodetect_box=True,
                      min_x=573648.5762539159,
                      min_y=7351627.100932668,
                      length_x=29176.221745807212,
                      length_y=61342.29204871226,
                      margin_x=0,
                      margin_y=0,
                      consider_blank_nodes=False,
                      autodetect_angle=True,
                      angle=6.696227728206645,
                      autodetect_grid=False,
                      grid_adjust_mode="step",
                      step_x=50,
                      step_y=50,
                      counts_x=0,
                      counts_y=0,
                      sample_object=absolute_object_name (name=None,
                      typed_names=[typed_object_name (obj_name="2km_area",
                      obj_type="Curve3d")]),
                      autodetect_during_wf_calculation=True),
                      target_func_resampling=True,
                      use_polygon=False,
                      polygon=find_object (name="1A_4A_5A",
                      type="Curve3d"),
                      interpolation_type="idw",
                      power_parameter=3,
                      idw_azimuth=0,
                      idw_axis_ratio=1,
                      kriging_mode="simple",
                      use_kriging_global_mean=False,
                      kriging_global_mean=0,
                      kriging_variogram_params=VariogramParameters (variogram_type="exponential",
                      sill=1,
                      nugget_effect=0,
                      range_main=2000,
                      range_normal=2000,
                      range_vertical=1,
                      azimuth=0,
                      dip=0,
                      azimuth_map=find_object (name="",
                      type="Map2d"),
                      use_azimuth_map=False,
                      external_source=False,
                      space_type="xyz",
                      sill_map=find_object (name="",
                      type=""),
                      use_sill_map=False,
                      source_object=find_object (name="",
                      type="")),
                      use_kriging_points_count=False,
                      kriging_points_count=50,
                      first_derivative_coefficient=0.2,
                      second_derivative_coefficient=0.02,
                      use_advanced=False,
                      do_grid_refinement=True,
                      refinement_steps=20,
                      start_nx=10,
                      start_ny=10,
                      do_drag=True,
                      drag_iterations=8,
                      drag_coefficient=0.4,
                      sgs_variogram_params=VariogramParameters (variogram_type="exponential",
                      sill=1,
                      nugget_effect=0,
                      range_main=1,
                      range_normal=1,
                      range_vertical=1,
                      azimuth=0,
                      dip=0,
                      azimuth_map=find_object (name="",
                      type=""),
                      use_azimuth_map=False,
                      external_source=False,
                      space_type="xyz",
                      sill_map=find_object (name="",
                      type=""),
                      use_sill_map=False,
                      source_object=find_object (name="",
                      type="")),
                      kriging_radius=0,
                      kriging_points=10,
                      random_seed=0,
                      sgs_transform_distribution=True,
                      sgs_distribution_type="source_data",
                      sgs_mean=0,
                      sgs_stdev=1,
                      sgs_alpha=1,
                      sgs_beta=1,
                      sgs_beta_use_shift_stretch_from_input=True,
                      sgs_shift=0,
                      sgs_stretch=1,
                      sgs_uniform_min=0,
                      sgs_uniform_max=0,
                      grfs_variogram_params=VariogramParameters (variogram_type="exponential",
                      sill=1,
                      nugget_effect=0,
                      range_main=1,
                      range_normal=1,
                      range_vertical=1,
                      azimuth=0,
                      dip=0,
                      azimuth_map=find_object (name="",
                      type=""),
                      use_azimuth_map=False,
                      external_source=False,
                      space_type="xyz",
                      sill_map=find_object (name="",
                      type=""),
                      use_sill_map=False,
                      source_object=find_object (name="",
                      type="")),
                      use_kriging_points_grfs=False,
                      kriging_points_grfs=50,
                      random_seed_grfs=0,
                      grfs_transform_distribution=True,
                      grfs_distribution_type="source_data",
                      grfs_mean=0,
                      grfs_stdev=1,
                      grfs_alpha=1,
                      grfs_beta=1,
                      grfs_beta_use_shift_stretch_from_input=True,
                      grfs_shift=0,
                      grfs_stretch=1,
                      grfs_uniform_min=0,
                      grfs_uniform_max=0,
                      amazonas_params=AmazonasParameters (major_axis_src_type="value",
                      major_semi_axis=250,
                      major_semi_axis_blocks=5,
                      major_semi_axis_map=find_object (name="",
                      type=""),
                      lateral_anizotropy=False,
                      major_minor_src_type="value",
                      major_minor_ratio=1,
                      major_minor_ratio_map=find_object (name="",
                      type=""),
                      azimuth_src_type="value",
                      azimuth=0,
                      azimuth_map=find_object (name="",
                      type=""),
                      vertical_axis_src_type="map",
                      vertical_semi_axis=5,
                      vertical_semi_axis_blocks=2,
                      dip=0,
                      random_seed=0,
                      aposteriori_drift_src_type="value",
                      aposteriori_drift=0.0001,
                      noise_map=find_object (name="",
                      type=""),
                      advanced_params=False,
                      axis_units_src_type="length",
                      use_apriori_drift=False,
                      apriori_drift=0,
                      min_threshold=5,
                      src_points_weight=5,
                      amazonas_stat_type="median",
                      kernel_bandwidth=0.5),
                      refinement_ratio=1.5,
                      convergent_use_advanced=False,
                      convergent_initial_approx_degree=0,
                      convergent_initial_grid_size=2,
                      accuracy=95,
                      use_filter=False,
                      filter=500,
                      smooth_power=0.5,
                      use_les_smoothing=True,
                      linear_tensioning_deg=1,
                      faster_convergence=True,
                      use_max_iterations_num=False,
                      max_iterations_num=100,
                      pre_defined_params="normal",
                      polynom_degree=1,
                      use_local_diagram_update=False,
                      global_splines_alpha=0.1,
                      global_splines_solver_accuracy=1e-10,
                      rbf_type="inverse_multiquadric",
                      rbf_variogram_params=VariogramParameters (variogram_type="exponential",
                      sill=1,
                      nugget_effect=0,
                      range_main=1,
                      range_normal=1,
                      range_vertical=1,
                      azimuth=0,
                      dip=0,
                      azimuth_map=find_object (name="",
                      type=""),
                      use_azimuth_map=False,
                      external_source=False,
                      space_type="xyz",
                      sill_map=find_object (name="",
                      type=""),
                      use_sill_map=False,
                      source_object=find_object (name="",
                      type="")),
                      use_rbf_points=False,
                      rbf_points=50,
                      use_min_z=False,
                      min_z=0,
                      use_max_z=False,
                      max_z=0.93)
                end_wf_item (index = 26)


            if False:
                begin_wf_item (index = 27)
                polygon_create_by_map_intersection (result_polygon=find_object (name="pgi_less",
                      type="Curve3d"),
                      top_z_type="map",
                      top=find_object (name="pgi_delta_abs",
                      type="Map2d"),
                      top_depth=0,
                      bottom_z_type="depth",
                      bottom=find_object (name="distance",
                      type="Map2d"),
                      bottom_depth=-10)
                end_wf_item (index = 27)


            if False:
                begin_wf_item (index = 28)
                polygon_create_by_map_intersection (result_polygon=find_object (name="pgi_more",
                      type="Curve3d"),
                      top_z_type="map",
                      top=find_object (name="pgi_delta_abs",
                      type="Map2d"),
                      top_depth=0,
                      bottom_z_type="depth",
                      bottom=find_object (name="distance",
                      type="Map2d"),
                      bottom_depth=10)
                end_wf_item (index = 28)



        end_wf_item (index = 21)


    if False:
        begin_wf_item (index = 30, name = "Пластовые давления")
        workflow_folder ()
        if True:
            pass



            if False:
                begin_wf_item (index = 31, name = "Скрипт импорта данных по пластовому давлению")
                run_graph_calculator (gc_code="from datetime import datetime\nimport getpass\nimport os\nfrom datetime import datetime\nimport pandas as pd\nfrom pathlib import Path\n\nfile_name = \'concated_press.csv\'\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\ndata = pd.read_csv(file_name, header=0, sep=\',\',names=[\'well\',\'date\',\'press\'])\ndata[\'date\'] = pd.to_datetime(data[\'date\'],format=\"%Y-%m-%d\")\ndata = data.loc[data.date<=\'31.12.2023\']\nprint(data)\n\nhist = graph_from_dataframe (type=\'well\',default_value= 0.0, dataframe= data, object = \'well\', date=\'date\', value=\'press\')\n\nexport(hist, name=\'P_plast\')\n",
                      font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
                      models=["SHORT_AREA:UNGKM_13_big"],
                      variables=variables)
                end_wf_item (index = 31)


            if False:
                begin_wf_item (index = 32, name = "Скрипт расчета отклонений по пластовым")
                run_graph_calculator (gc_code="#пишите здесь ваш код\nfrom pathlib import Path\nimport pandas as pd\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\nplast_hist = get_global_graph (name = \'P_plast\')\nplast_model = wbp9\n\nhist = plast_hist.to_dataframe ()\nmodel = plast_model.to_dataframe ()\nprint(hist.columns)\nconcated = pd.merge(left=hist, right=model, on=[\'Скважины\',\'Дата\'])\nconcated.columns=[\'date\', \'well\', \'history\', \'model\']\nconcated=concated.loc[concated.history>0]\n#.to_csv(\'rate_from_model.csv\', sep=\',\')\n# %% отклонение считает по среднему \nto_model = concated#.loc[:, [\'well\', \'history\', \'model\']].groupby(\'well\').agg(\'mean\')\nto_model[\'pgi_otn\'] = (to_model.history-to_model.model)/to_model.history*100\nto_model[\'pgi_abs\'] = (to_model.history-to_model.model)\n#to_model[\'model\'] = to_model[\'model\']*100\n#to_model[\'history\'] = to_model[\'history\']*100\n#print(concated)\n# %%\nto_model.reset_index().to_csv(\'plast_crossplot.csv\')\n#",
                      font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
                      models=["SHORT_AREA:UNGKM_13_big"],
                      variables=variables)
                end_wf_item (index = 32)



        end_wf_item (index = 30)


    begin_wf_item (index = 34)
    workflow_folder ()
    if True:
        pass



        begin_wf_item (index = 35, name = "Скрипт расчета отклонений по продуктивностям")
        run_graph_calculator (gc_code="#пишите здесь ваш код\nfrom pathlib import Path\nimport pandas as pd\nimport numpy as np\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\nproductivity_hist = wwgprh\nproductivity_model = wwgpr\nmean_prod=graph(type = \'well\', default_value =0)\n\n\n\nhist = productivity_hist.to_dataframe ()\nmodel = productivity_model.to_dataframe ()\nconcated = pd.merge(left=hist, right=model, on=[\'Скважины\',\'Дата\'])\nconcated.columns=[\'date\', \'well\', \'history\', \'model\']\nconcated=concated.loc[concated.history>0]\nconcated = concated.drop_duplicates (subset=[\'history\'])\nconcated[\'prod_otn\'] = np.abs((concated.history-concated.model)/concated.history*100)\n\nfor graph, name in zip([\'history\', \'model\'], [\'history_productivity\', \'model_productivity\']):\n	ex_graph = graph_from_dataframe (type=\'well\',default_value= np.nan, dataframe= concated, object = \'well\', date=\'date\', value=graph)\n	export(ex_graph, name=name)\n\nconcated.reset_index().to_csv(\'prod_match.csv\')\ndiffs = graph_from_dataframe (type=\'well\',default_value= np.nan, dataframe= concated, object = \'well\', date=\'date\', value=\'prod_otn\')\n\nimport numpy as np\n\nprod_diffs = concated.loc[:, [\"well\", \"prod_otn\"]].groupby(\"well\").describe()\nprod_diffs.columns = [\'count\', \'mean\', \'std\', \'min\', \'25%\', \'50%\', \'75%\', \'max\']\nprod_diffs.loc[:,[\'25%\', \'50%\', \'75%\']]\n# %%\nfor name, row in prod_diffs.iterrows():\n	w = get_well_by_name(name)\n	mean_prod[w]=row[\'50%\']\n\nexport(mean_prod, name=\'prod_diff_mean\', units=\'persent_1\')\nexport(diffs, name=\'prod_otn\', units=\'persent_1\')\n\n\n\n\n\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 35)



    end_wf_item (index = 34)


    if False:
        begin_wf_item (index = 37, is_custom_code = True, name = "Индекс участка в атрибуты")
        from datetime import datetime
        from pathlib import Path


        def create_report_dir(path):
            path = Path(path)
            path = path.joinpath('reports')
            path.mkdir(parents=True, exist_ok=True)
            os.chdir(path)


        create_report_dir(get_project_folder ( ))

         

        def create_attr_by_well_loc(attr_name, marker_name, create_attr=False):
        	if create_attr==True:
        		create_well_attribute (name=attr_name, overwrite_existing=True)
        	else:
        		pass
        	attr=get_well_attribute_by_name (name=attr_name)
        	marker = get_marker_by_name (name=marker_name)
        	for w in get_all_wells ():
        		try:
        			print(w.name)
        			loc = int(w.name[0])
        			attr.set_value(md=float(marker.get_points(well=w)[0]), value=loc, wellbore=w.get_wellbores ()[0], overwrite_existing=True)
        		except:
        			continue

        create_attr_by_well_loc('Well_loc', 'Ach3_top', create_attr=False)
        end_wf_item (index = 37)


    if False:
        begin_wf_item (index = 38, is_custom_code = True, name = "Начальное содержание ПС в атрибуты")
        from datetime import datetime
        from pathlib import Path


        def create_report_dir(path):
            path = Path(path)
            path = path.joinpath('reports')
            path.mkdir(parents=True, exist_ok=True)
            os.chdir(path)


        create_report_dir(get_project_folder ( ))


        def create_attr_from_file(file_name, attr_name, marker_name, create_attr=False):
        	if create_attr==True:
        		create_well_attribute (name=attr_name, overwrite_existing=True)
        	else:
        		pass
        	attr=get_well_attribute_by_name (name=attr_name)
        	marker = get_marker_by_name (name=marker_name)
        	with open(file_name,"r") as f:
        		for line in f:
        			column=line.split()
        			try:
        				w = get_well_by_name(name = str(column[0]))
        				if float(column[1])!=0:
        					attr.set_value(md=float(marker.get_points(well=w)[0]), value=float(column[1]), wellbore=w.get_wellbores ()[0], overwrite_existing=True)
        			except:
        				continue


        	
        create_attr_from_file(r'/home/albert.vafin/Документы/UNGKM/test/CUSTOM/PS_C5_for_map2.txt', 'PC_GKI', 'Ach3_top', create_attr=False)
         
        # скрипт по местоположению скважин и отнесению их к участку
        def create_attr_by_well_loc(attr_name, marker_name, create_attr=False):
        	if create_attr==True:
        		create_well_attribute (name=attr_name, overwrite_existing=True)
        	else:
        		pass
        	attr=get_well_attribute_by_name (name=attr_name)
        	marker = get_marker_by_name (name=marker_name)
        	for w in get_all_wells ():
        		try:
        			print(w.name)
        			loc = int(w.name[0])
        			attr.set_value(md=float(marker.get_points(well=w.name)[0]), value=loc, wellbore=w.get_wellbores ()[0], overwrite_existing=True)
        		except:
        			continue

        create_attr_by_well_loc('Well_loc', 'Ach3_top', create_attr=False)
        end_wf_item (index = 38)


    if False:
        begin_wf_item (index = 39, name = "Скрипт по экспорту C5+ в базу данных")
        run_graph_calculator (gc_code="import pandas as pd\nimport getpass\nimport numpy as np\nfrom datetime import datetime\nfrom sqlalchemy import create_engine\n\nkeyword = {\'grou\':get_all_groups(), \'wells\':get_all_wells(), \'mod\' : get_all_models(), \'step\':get_all_timesteps()}\n\ndef dataframe_creater(*args, start=\'01.01.1950\', **kwarg):\n    \"\"\"создает pandas Dataframe с данными из модели.\n         Принимает неограниченное количество параметров для\n          импорта, позволяет осуществлять импорт как по скважинам\n          так и по группам заданием kwarg\n         function for converting navigation format to pandas dataframe\n         *args - list of arguments to issue in the frame\n             dimens - well, here is one of two:\n                        well - for issuing a frame for wells\n                        group - for issuing by group\"\"\"\n    indicators = [x for x in args]\n    name = [\'Parametr{}\'.format(x) for x in range(0, len(indicators))]\n    indicators_dict = dict.fromkeys([\'date\', \'well\']+name)\n    indicators_dict = {x: [] for x in indicators_dict.keys()}\n    assos_dict = {x: y for x, y in zip(indicators, name)}\n    start_date = datetime.strptime(start, \'%d.%m.%Y\')\n    try:\n        for m in kwarg[\'mod\']:\n            for w in kwarg[\'wells\']:\n                for t in kwarg[\'step\']:\n                    if t.to_datetime() >= start_date:\n                        indicators_dict[\'date\'].append(t.to_datetime())\n                        indicators_dict[\'well\'].append(w.name)\n                        for i in indicators:\n                            indicators_dict[assos_dict[i]].append(\n                                i[m, w, t].to_list()[0])\n                    else:\n                        continue\n    except Exception as e:\n        m = kwarg[\'mod\']\n        for w in kwarg[\'wells\']:\n            for t in kwarg[\'step\']:\n                if t.to_datetime() >= start_date:\n                    indicators_dict[\'date\'].append(t.to_datetime())\n                    indicators_dict[\'well\'].append(w.name)\n                    for i in indicators:\n                        indicators_dict[assos_dict[i]].append(\n                            i[m, w, t].to_list()[0])\n                else:\n                    continue\n    result = pd.DataFrame(indicators_dict, index=indicators_dict[\'date\'])\n    return result.drop(\'date\', axis=1)\n\nps = get_global_graph (name = \'PS_C5\')\n\ndf = dataframe_creater(ps, **keyword)\ndf.columns = [\'well\', \'ps\']\ndf[\'result_date\'] = datetime.now().strftime(\"%Y-%m-%d %H:%M\")\ndf[\'model\'] = get_all_models ()[0].name\ndf[\'path\'] = (get_project_folder ())\nprint(df.head())\npost_con = create_engine(\'postgresql://test:test@localhost:5434/ungkm\')\ndf.to_sql(\'PS_C5plus_model\', con=post_con, if_exists=\'append\')\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 39)


    if False:
        begin_wf_item (index = 40, name = "Скрипт импорта данных по давлениям на границах ")
        run_graph_calculator (gc_code="from datetime import datetime\nimport getpass\nimport os\nfrom datetime import datetime\nimport pandas as pd\nfrom pathlib import Path\n\nfile_name = \'bound_fip_press.csv\'\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\ndata = pd.read_csv(file_name, header=0, sep=\',\',names=[\'fip\',\'date\',\'value\'])\ndata[\'date\'] = pd.to_datetime(data[\'date\'],format=\"%Y-%m-%d\")\n\n\nhist = graph_from_dataframe (type=\'fip\',default_value= 0.0, dataframe= data, object = \'fip\', date=\'date\', value=\'value\')\n\nexport(hist, name=\'bound_press\')\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 40)


    if False:
        begin_wf_item (index = 41, name = "Импорт данных по дебиту ГКС из файла")
        run_graph_calculator (gc_code=" \n\nimport pandas as pd\n\ndf = pd.read_table(r\'/home/albert.vafin/Documents/UNGKM/test/CUSTOM/GKS_FOR_MODEL.txt\', delimiter=\' \', usecols=[0, 1, 2], names=[\'well\', \'date\', \'q_gks\'])\ndf.date = pd.to_datetime(df.date)\ndf = df.loc[df.date<\'01.01.2023\']\ngks = graph_from_dataframe (type= \'well\', default_value= 0, dataframe= df, object = \'well\', date=\'date\', value=\'q_gks\')\nexport(gks, name = \'GKS_hist\')\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 41)


    if False:
        begin_wf_item (index = 42, name = "Скрипт импорта данных по давлениям на границах ")
        run_graph_calculator (gc_code="from datetime import datetime\nimport getpass\nimport os\nfrom datetime import datetime\nimport pandas as pd\nfrom pathlib import Path\n\nfile_name = \'bound_fip_press.csv\'\n\ndef create_report_dir(path):\n    path = Path(path)\n    path = path.joinpath(\'reports\')\n    path.mkdir(parents=True, exist_ok=True)\n    os.chdir(path)\n\ncreate_report_dir(get_project_folder ( ))\n\nfile=open(file_name,\"r\")\nevent=graph(type = \'fip\', default_value = 0)\n\nfor line in file:\n	column=line.split(\',\')\n	try:\n		print(column[0], column[1], column[2])\n		w = get_fip_region(family_name= \'FIPNUM\', fip_num=int(column[0]))\n		t=get_timestep_from_datetime (datetime.strptime(str(column[1]), \'%Y-%m-%d\'), mode = \'nearest\')\n		event[w, t]=float(column[2])\n	except:\n		continue\n\nexport(event, name = \'PRESS_bound\')\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 42)


    if False:
        begin_wf_item (index = 43, name = "Скрипт по экспорту данных расчета в базу")
        run_graph_calculator (gc_code="import pandas as pd\nimport getpass\nimport numpy as np\nfrom datetime import datetime\nfrom sqlalchemy import create_engine\n\nkeyword = {\'grou\':get_all_groups(), \'wells\':get_all_wells(), \'mod\' : get_all_models(), \'step\':get_all_timesteps()}\n\ndef dataframe_creater(*args, start=\'01.01.1950\', **kwarg):\n    \"\"\"создает pandas Dataframe с данными из модели.\n         Принимает неограниченное количество параметров для\n          импорта, позволяет осуществлять импорт как по скважинам\n          так и по группам заданием kwarg\n         function for converting navigation format to pandas dataframe\n         *args - list of arguments to issue in the frame\n             dimens - well, here is one of two:\n                        well - for issuing a frame for wells\n                        group - for issuing by group\"\"\"\n    indicators = [x for x in args]\n    name = [\'Parametr{}\'.format(x) for x in range(0, len(indicators))]\n    indicators_dict = dict.fromkeys([\'date\', \'well\']+name)\n    indicators_dict = {x: [] for x in indicators_dict.keys()}\n    assos_dict = {x: y for x, y in zip(indicators, name)}\n    start_date = datetime.strptime(start, \'%d.%m.%Y\')\n    try:\n        for m in kwarg[\'mod\']:\n            for w in kwarg[\'wells\']:\n                for t in kwarg[\'step\']:\n                    if t.to_datetime() >= start_date:\n                        indicators_dict[\'date\'].append(t.to_datetime())\n                        indicators_dict[\'well\'].append(w.name)\n                        for i in indicators:\n                            indicators_dict[assos_dict[i]].append(\n                                i[m, w, t].to_list()[0])\n                    else:\n                        continue\n    except Exception as e:\n        m = kwarg[\'mod\']\n        for w in kwarg[\'wells\']:\n            for t in kwarg[\'step\']:\n                if t.to_datetime() >= start_date:\n                    indicators_dict[\'date\'].append(t.to_datetime())\n                    indicators_dict[\'well\'].append(w.name)\n                    for i in indicators:\n                        indicators_dict[assos_dict[i]].append(\n                            i[m, w, t].to_list()[0])\n                else:\n                    continue\n    result = pd.DataFrame(indicators_dict, index=indicators_dict[\'date\'])\n    return result.drop(\'date\', axis=1)\n\n\ndf = dataframe_creater(wopt, wopth, wgpt, wgpth, wwpt, wwpth, **keyword)\ndf.columns = [\'well\', \'wopt\', \'wopth\', \'wgpt\', \'wgpth\', \'wwpt\', \'wwpth\']\ndf[\'result_date\'] = datetime.now().strftime(\"%Y-%m-%d %H:%M\")\ndf[\'model\'] = get_all_models ()[0].name\ndf[\'path\'] = (get_project_folder ())\nprint(df.head())\npost_con = create_engine(\'postgresql://test:test@localhost:5434/ungkm\')\ndf.to_sql(\'total_result\', con=post_con, if_exists=\'replace\')\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 43)


    if False:
        begin_wf_item (index = 44, name = "для Айдара")
        run_graph_calculator (gc_code="import pandas as pd\nimport getpass\nimport numpy as np\nfrom datetime import datetime\nfrom sqlalchemy import create_engine\n\nkeyword = {\'grou\':get_all_groups(), \'wells\':get_all_wells(), \'mod\' : get_all_models(), \'step\':get_all_timesteps()}\n\ndef dataframe_creater(*args, start=\'01.01.1950\', **kwarg):\n    \"\"\"создает pandas Dataframe с данными из модели.\n         Принимает неограниченное количество параметров для\n          импорта, позволяет осуществлять импорт как по скважинам\n          так и по группам заданием kwarg\n         function for converting navigation format to pandas dataframe\n         *args - list of arguments to issue in the frame\n             dimens - well, here is one of two:\n                        well - for issuing a frame for wells\n                        group - for issuing by group\"\"\"\n    indicators = [x for x in args]\n    name = [\'Parametr{}\'.format(x) for x in range(0, len(indicators))]\n    indicators_dict = dict.fromkeys([\'date\', \'well\']+name)\n    indicators_dict = {x: [] for x in indicators_dict.keys()}\n    assos_dict = {x: y for x, y in zip(indicators, name)}\n    start_date = datetime.strptime(start, \'%d.%m.%Y\')\n    try:\n        for m in kwarg[\'mod\']:\n            for w in kwarg[\'wells\']:\n                for t in kwarg[\'step\']:\n                    if t.to_datetime() >= start_date:\n                        indicators_dict[\'date\'].append(t.to_datetime())\n                        indicators_dict[\'well\'].append(w.name)\n                        for i in indicators:\n                            indicators_dict[assos_dict[i]].append(\n                                i[m, w, t].to_list()[0])\n                    else:\n                        continue\n    except Exception as e:\n        m = kwarg[\'mod\']\n        for w in kwarg[\'wells\']:\n            for t in kwarg[\'step\']:\n                if t.to_datetime() >= start_date:\n                    indicators_dict[\'date\'].append(t.to_datetime())\n                    indicators_dict[\'well\'].append(w.name)\n                    for i in indicators:\n                        indicators_dict[assos_dict[i]].append(\n                            i[m, w, t].to_list()[0])\n                else:\n                    continue\n    result = pd.DataFrame(indicators_dict, index=indicators_dict[\'date\'])\n    return result.drop(\'date\', axis=1)\n\n\ndf = dataframe_creater(wwgpr, wogr, wwgr, wthp, wthph, wbhp, wbhph, **keyword)\ndf.columns = [\'well\', \'wwgpr\', \'wogr\', \'wwgr\', \'wthp\', \'wthph\', \'wbhp\', \'wbhph\']\ndf[\'result_date\'] = datetime.now().strftime(\"%Y-%m-%d %H:%M\")\ndf[\'model\'] = get_all_models ()[0].name\ndf[\'path\'] = (get_project_folder ())\nprint(df.head())\npost_con = create_engine(\'postgresql://test:test@localhost:5434/ungkm\')\ndf.to_sql(\'bhp_thp\', con=post_con, if_exists=\'replace\')\n",
              font="DejaVu Sans Mono,8,-1,5,50,0,0,0,0,0",
              models=["SHORT_AREA:UNGKM_13_big"],
              variables=variables)
        end_wf_item (index = 44)


