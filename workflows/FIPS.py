#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="FIPS",
      variables=[])


FIPS_variables = {

}

def FIPS (variables = FIPS_variables):
    pass
    check_launch_method ()


    begin_user_imports ()
    end_user_imports ()

    begin_wf_item (index = 1)
    PROP_NAME = "FIPNUM"
    set_var_type (n = "PROP_NAME", t = "STRING", it = "PY_EXPR", val = PROP_NAME)
    variables["PROP_NAME"] = PROP_NAME

    end_wf_item (index = 1)


    begin_wf_item (index = 2, is_custom_code = True, name = "Получаем перечень полигонов из папки")
    polygons = get_all_curves_3d_in_folder (folder="FIPS", recursive=True)
    end_wf_item (index = 2)


    begin_wf_item (index = 3)
    for poly in enumerate(polygons):
        pass
        set_var_type (n = "poly", t = "PY_EXPR", it = "PY_EXPR", val = poly)
        begin_loop_iteration (info = "poly = " + str (poly))



        begin_wf_item (index = 4, is_custom_code = True, name = "Присваивание внутри полигонов")
        print(poly[0], poly[1].name)
        n = poly[0]+2
        polygon = poly[1].name

        grid_property_edit_inside_polygon (grid=find_object (name="Cuted",
              type="Grid3d"),
              grid_property=find_object (name=PROP_NAME,
              type="Grid3dProperty"),
              clear_values=False,
              polygon=find_object (name=resolve_variables_in_string (string_with_variables=polygon,
              variables=variables),
              type="Curve3d"),
              polygon_filter_rule="by_center",
              stored_value=n,
              use_filter_property=False,
              filter_property=find_object (name="ZONE",
              type="Grid3dProperty"),
              comparator=Comparator (rule="not_equals",
              value=0))
        end_wf_item (index = 4)


        if False:
            begin_wf_item (index = 5, is_custom_code = True, name = "ЭКСПОРТ МНОГОУГОЛЬНИКОВ")
            print(poly[0], poly[1].name)
            n = poly[0]+2
            polygon = poly[1].name

            path = f'../../../../public/2023/UNGKM/for_GDM/POLYGONS/{polygon}'
            polygon_export_ascii_classic_format (file_name=path,
                  polygon=find_object (name=polygon,
                  type="Curve3d"),
                  use_length_unit=False,
                  length_unit="metres")
            end_wf_item (index = 5)


        if False:
            begin_wf_item (index = 6)
            grid_property_edit_inside_polygon (grid=find_object (name="Cuted",
                  type="Grid3d"),
                  grid_property=find_object (name="Property2",
                  type="Grid3dProperty"),
                  clear_values=False,
                  polygon=find_object (name=resolve_variables_in_string (string_with_variables="@POLYGON@",
                  variables=variables),
                  type="Curve3d"),
                  polygon_filter_rule="by_center",
                  position="inside",
                  stored_value=2,
                  use_filter_property=False,
                  filter_property=find_object (name="ZONE",
                  type="Grid3dProperty"),
                  comparator=Comparator (rule="not_equals",
                  value=0))
            end_wf_item (index = 6)


        end_loop_iteration ()

    end_wf_item (index = 3)


    begin_wf_item (index = 8)
    grid_property_calculator (mesh=find_object (name="Cuted",
          type="Grid3d"),
          result_grid_property=find_object (name=resolve_variables_in_string (string_with_variables="@PROP_NAME@",
          variables=variables),
          type="Grid3dProperty"),
          discrete_output=False,
          use_filter=False,
          user_cut_for_filter=find_object (name="ZONE",
          type="Grid3dProperty"),
          filter_comparator=Comparator (rule="not_equals",
          value=0),
          formula=resolve_variables_in_string (string_with_variables="(ZONE==1)*@PROP_NAME@+\n(ZONE==3)*(19+@PROP_NAME@)+\n(ZONE==5)*(19*2+@PROP_NAME@)+\n(ZONE==7)*(19*3+@PROP_NAME@)",
          variables=variables),
          variables=variables)
    end_wf_item (index = 8)


    if False:
        begin_wf_item (index = 9)
        wells_history_export_simple_table_format (wells=find_object (name="Wells",
              type="gt_wells_entity"),
              well_production=find_object (name="UNGKM_prod_from_VAR",
              type="gt_wells_production_data"),
              file_name="history.txt",
              delimiter="two_spaces",
              use_delimiter_str=False,
              delimiter_str=",",
              selected_columns=[{"use" : True, "column_name" : "well"}, {"use" : True, "column_name" : "date"}, {"use" : True, "column_name" : "oil"}, {"use" : True, "column_name" : "water"}, {"use" : True, "column_name" : "gas"}, {"use" : False, "column_name" : "liquid"}, {"use" : False, "column_name" : "resv"}, {"use" : False, "column_name" : "injected_gas"}, {"use" : False, "column_name" : "injected_water"}, {"use" : False, "column_name" : "injected_oil"}, {"use" : False, "column_name" : "injected_resv"}, {"use" : True, "column_name" : "oil_production"}, {"use" : True, "column_name" : "water_production"}, {"use" : True, "column_name" : "gas_production"}, {"use" : False, "column_name" : "liquid_production"}, {"use" : False, "column_name" : "resv_production"}, {"use" : False, "column_name" : "gas_injection"}, {"use" : False, "column_name" : "water_injection"}, {"use" : False, "column_name" : "oil_injection"}, {"use" : False, "column_name" : "resv_injection"}, {"use" : True, "column_name" : "thp"}, {"use" : False, "column_name" : "bhp"}, {"use" : False, "column_name" : "wefac"}, {"use" : False, "column_name" : "artificial_lift"}, {"use" : False, "column_name" : "steam_quality"}, {"use" : False, "column_name" : "inj_temperature"}, {"use" : False, "column_name" : "inj_pressure"}, {"use" : False, "column_name" : "inj_enthalpy"}, {"use" : False, "column_name" : "polymer_conc"}, {"use" : False, "column_name" : "alkaline_conc"}, {"use" : False, "column_name" : "surfactant_conc"}, {"use" : False, "column_name" : "salt_conc"}, {"use" : False, "column_name" : "wet_gas_rate"}, {"use" : False, "column_name" : "total_molar_rate"}, {"use" : False, "column_name" : "steam_rate"}, {"use" : False, "column_name" : "satur_temperature"}, {"use" : False, "column_name" : "satur_pressure"}, {"use" : False, "column_name" : "calorific_rate"}, {"use" : False, "column_name" : "ngl_rate"}, {"use" : False, "column_name" : "water_oil_ratio"}, {"use" : False, "column_name" : "watercut"}, {"use" : False, "column_name" : "water_gas_ratio"}, {"use" : False, "column_name" : "gas_oil_ratio"}, {"use" : False, "column_name" : "gas_liquid_ratio"}, {"use" : False, "column_name" : "oil_gas_ratio"}, {"use" : True, "column_name" : "operation_time"}, {"use" : False, "column_name" : "comment"}],
              use_well_filter=False,
              well_filter=find_object (name="AchDev",
              type="WellFilter"),
              date_filter=False,
              first_date=datetime (year=2023,
              month=7,
              day=27,
              hour=0,
              minute=0,
              second=0),
              last_date=datetime (year=2023,
              month=7,
              day=27,
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
        end_wf_item (index = 9)


    if False:
        begin_wf_item (index = 10)
        map_2d_distance_to_polygon (result_map_2d=find_object (name="distance",
              type="Map2d"),
              curve=find_object (name="1A_4A_5A",
              type="Curve3d"),
              grid_2d_settings=Grid2DSettings (grid_2d_settings_shown=True,
              autodetect_box=False,
              min_x=569112.0018733925,
              min_y=7350093.499322926,
              length_x=33300,
              length_y=64900,
              margin_x=0,
              margin_y=0,
              consider_blank_nodes=False,
              autodetect_angle=False,
              angle=0,
              autodetect_grid=False,
              grid_adjust_mode="step",
              step_x=100,
              step_y=100,
              counts_x=0,
              counts_y=0,
              sample_object=absolute_object_name (name=None,
              typed_names=[typed_object_name (obj_name="Ach_ungkm",
              obj_type="Grid3d")]),
              autodetect_during_wf_calculation=True))
        end_wf_item (index = 10)


    if False:
        begin_wf_item (index = 11)
        polygon_export_ascii_classic_format (file_name="../../../../public/2023/UNGKM/for_GDM/POLYGONS/51A",
              polygon=find_object (name="1A",
              type="Curve3d"),
              use_length_unit=False,
              length_unit="metres")
        end_wf_item (index = 11)


