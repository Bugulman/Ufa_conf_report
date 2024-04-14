#  Этот файл был сгенерирован тНавигатор v23.3-3480-gdbdbad1.
#  Copyright (C) Рок Флоу Динамикс 2005-2023.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0.0.107d

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="Dynamic",
      variables=[{"name" : "GRID_NAME", "type" : "string", "min" : 0, "max" : 3, "values" : ["GDM_with_petro_2023-09-04", "Ach_ungkm_smooth", "Cutted", "Cuted"], "distribution_type" : "Discrete", "discrete_distr_values" : [0, 1, 2, 3], "discrete_distr_probabilities" : [25, 25, 25, 25], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_6", "type" : "real", "min" : 3668, "max" : 3766, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_4", "type" : "real", "min" : 3726, "max" : 3786, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "WOC_DEPTH_S_5", "type" : "real", "min" : 3960, "max" : 4020, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_5", "type" : "real", "min" : 3820, "max" : 3880, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_9", "type" : "real", "min" : 3775, "max" : 3835, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}])


Dynamic_variables = {
"GRID_NAME" : "Cuted",
"GOC_DEPTH_S_6" : 3766,
"GOC_DEPTH_S_4" : 3766,
"WOC_DEPTH_S_5" : 4012,
"GOC_DEPTH_S_5" : 3840,
"GOC_DEPTH_S_9" : 3807
}

def Dynamic (variables = Dynamic_variables):
    pass
    check_launch_method ()

    GRID_NAME = variables["GRID_NAME"]
    GOC_DEPTH_S_6 = variables["GOC_DEPTH_S_6"]
    GOC_DEPTH_S_4 = variables["GOC_DEPTH_S_4"]
    WOC_DEPTH_S_5 = variables["WOC_DEPTH_S_5"]
    GOC_DEPTH_S_5 = variables["GOC_DEPTH_S_5"]
    GOC_DEPTH_S_9 = variables["GOC_DEPTH_S_9"]

    begin_user_imports ()
    end_user_imports ()

    begin_wf_item (index = 1)
    grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
          variables=variables),
          type="Grid3d"),
          result_grid_property=find_object (name="PERMX",
          type="Grid3dProperty"),
          discrete_output=False,
          use_filter=False,
          user_cut_for_filter=find_object (name="ZONE",
          type="Grid3dProperty"),
          filter_comparator=Comparator (rule="not_equals",
          value=0),
          formula="(PetroTypes==1)*10^(27.43796*PORO-4.696606)+(PetroTypes==2)*10^(8.126039*PORO-1.741823)+(PetroTypes==3)*10^(19.95081*PORO-3.817514)+(PetroTypes==4)*10^(9.784708*PORO-2.248439)",
          variables=variables)
    end_wf_item (index = 1)


    begin_wf_item (index = 2)
    grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
          variables=variables),
          type="Grid3d"),
          result_grid_property=find_object (name="SWL",
          type="Grid3dProperty"),
          discrete_output=False,
          use_filter=False,
          user_cut_for_filter=find_object (name="ZONE",
          type="Grid3dProperty"),
          filter_comparator=Comparator (rule="not_equals",
          value=0),
          formula="(PetroTypes==1)*(-0.0446*ln(PermX)+0.3804)+(PetroTypes==2)*(-0.1215*ln(PermX)+0.5039)+(PetroTypes==3)*(1.2192*exp(-6.3354*Poro))+(PetroTypes==4)*(0.9295*exp(-1.2453*Poro))",
          variables=variables)
    end_wf_item (index = 2)


    if False:
        begin_wf_item (index = 3)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="SOWCR",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="(PetroTypes==1)*0.33168+(PetroTypes==2)*0.345268+(PetroTypes==3)*0.325335+(PetroTypes==4)*0.3485",
              variables=variables)
        end_wf_item (index = 3)


    if False:
        begin_wf_item (index = 4)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="SOGCR",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="(PetroTypes==1)*0.119126+(PetroTypes==2)*0.119126+(PetroTypes==3)*0.5385*exp(-2.679*PERMX)+(PetroTypes==4)*0.5385*exp(-2.679*PERMX)",
              variables=variables)
        end_wf_item (index = 4)


    if False:
        begin_wf_item (index = 5)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="KRWR",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="(PetroTypes==1)*0.079327+(PetroTypes==2)*0.02071+(PetroTypes==3)*0.115154+(PetroTypes==4)*0.0945",
              variables=variables)
        end_wf_item (index = 5)


    if False:
        begin_wf_item (index = 6)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="KRORW",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="(PetroTypes==1)*0.2795+(PetroTypes==2)*0.07433+(PetroTypes==3)*0.210784+(PetroTypes==4)*0.264343642",
              variables=variables)
        end_wf_item (index = 6)


    if False:
        begin_wf_item (index = 7)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="KRORG",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="(PetroTypes==1)*0.297915+(PetroTypes==2)*0.297915+(PetroTypes==3)*0.19378+(PetroTypes==4)*0.19378",
              variables=variables)
        end_wf_item (index = 7)


    if False:
        begin_wf_item (index = 8)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="KRGR",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="(PetroTypes==1)*0.407157+(PetroTypes==2)*0.407157+ (PetroTypes==3)*0.1416273\n+(PetroTypes==4)*0.1416273",
              variables=variables)
        end_wf_item (index = 8)


    if False:
        begin_wf_item (index = 9)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="SATNUM",
              type="Grid3dProperty"),
              discrete_output=True,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="round(if(PetroTypes==0, 1, PetroTypes))",
              variables=variables)
        end_wf_item (index = 9)


    if False:
        begin_wf_item (index = 10)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="SGU",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="1-SWL",
              variables=variables)
        end_wf_item (index = 10)


    if False:
        begin_wf_item (index = 11)
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="PCW",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="((PetroTypes==1)*6.8275+(PetroTypes==2)*1.8209052281589093+(PetroTypes==3)*1.6417479517989417+(PetroTypes==4)*1.0008691818886366)*35*0.318316*((PORO/PERMX)^0.5)",
              variables=variables)
        end_wf_item (index = 11)


    begin_wf_item (index = 12)
    static_mapping (cases=find_object (name="SOME",
          type="Model_ex"),
          grid=find_object (name="Cuted",
          type="Grid3d"),
          set_grid=True,
          action="replace",
          static_table=[{"description" : "ID_PERMZ", "keyword" : "PERMZ", "component" : None, "property" : find_object (name="PERMX",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SWL", "keyword" : "SWL", "component" : None, "property" : find_object (name="SWL",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_KRGR", "keyword" : "KRGR", "component" : None, "property" : find_object (name="KRGR",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_KRORG", "keyword" : "KRORG", "component" : None, "property" : find_object (name="KRORG",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SOWCR", "keyword" : "SOWCR", "component" : None, "property" : find_object (name="SOWCR",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_PERMY", "keyword" : "PERMY", "component" : None, "property" : find_object (name="PERMX",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_PERMX", "keyword" : "PERMX", "component" : None, "property" : find_object (name="PERMX",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_KRORW", "keyword" : "KRORW", "component" : None, "property" : find_object (name="KRORW",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SATNUM", "keyword" : "SATNUM", "component" : None, "property" : find_object (name="SATNUM",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_EQLNUM", "keyword" : "EQLNUM", "component" : None, "property" : find_object (name="ZONE",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_NTG", "keyword" : "NTG", "component" : None, "property" : find_object (name="LITO",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SWCR", "keyword" : "SWCR", "component" : None, "property" : find_object (name="SWL",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_KRWR", "keyword" : "KRWR", "component" : None, "property" : find_object (name="KRWR",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_PCW", "keyword" : "PCW", "component" : None, "property" : find_object (name="PCW",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SGU", "keyword" : "SGU", "component" : None, "property" : find_object (name="SGU",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_PORO", "keyword" : "PORO", "component" : None, "property" : find_object (name="PORO",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SOGCR", "keyword" : "SOGCR", "component" : None, "property" : find_object (name="SOGCR",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_SWCR", "keyword" : "SWCR", "component" : None, "property" : find_object (name="SWL",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}])
    end_wf_item (index = 12)


    begin_wf_item (index = 13)
    adjust_equil_table (table_name="ach3",
          datum_depth=3740,
          datum_pressure=608.92,
          woc_depth=arithmetic (expression="GOC_DEPTH_S_4",
          variables=variables),
          woc_capillary_pressure=0,
          goc_depth=arithmetic (expression="GOC_DEPTH_S_4",
          variables=variables),
          goc_capillary_pressure=0,
          live_black_oil=0,
          wet_gas=0,
          accuracy=None,
          compos_init_type=None,
          compos_press_type_on_contact=None)
    end_wf_item (index = 13)


    begin_wf_item (index = 14)
    adjust_equil_table (table_name="ach3",
          datum_depth=3650,
          datum_pressure=604.08,
          woc_depth=arithmetic (expression="GOC_DEPTH_S_6",
          variables=variables),
          woc_capillary_pressure=0,
          goc_depth=arithmetic (expression="GOC_DEPTH_S_6",
          variables=variables),
          goc_capillary_pressure=0,
          live_black_oil=1,
          wet_gas=0,
          accuracy=None,
          compos_init_type=None,
          compos_press_type_on_contact=None)
    end_wf_item (index = 14)


    begin_wf_item (index = 15)
    adjust_equil_table (table_name="ach3",
          datum_depth=3840,
          datum_pressure=614,
          woc_depth=arithmetic (expression="WOC_DEPTH_S_5",
          variables=variables),
          woc_capillary_pressure=0,
          goc_depth=arithmetic (expression="GOC_DEPTH_S_5",
          variables=variables),
          goc_capillary_pressure=0,
          live_black_oil=0,
          wet_gas=0,
          accuracy=None,
          compos_init_type=None,
          compos_press_type_on_contact=None)
    end_wf_item (index = 15)


    begin_wf_item (index = 16)
    adjust_equil_table (table_name="ach3",
          datum_depth=3774,
          datum_pressure=610.41,
          woc_depth=arithmetic (expression="GOC_DEPTH_S_9",
          variables=variables),
          woc_capillary_pressure=0,
          goc_depth=arithmetic (expression="GOC_DEPTH_S_9",
          variables=variables),
          goc_capillary_pressure=0,
          live_black_oil=0,
          wet_gas=0,
          accuracy=None,
          compos_init_type=None,
          compos_press_type_on_contact=None)
    end_wf_item (index = 16)


