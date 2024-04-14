#  Этот файл был сгенерирован тНавигатор v23.4-5689-g1082f6c.
#  Copyright (C) Рок Флоу Динамикс 2005-2024.
#  Все права защищены.

# This file is MACHINE GENERATED! Do not edit.

#api_version=v0_0_117

from __main__.tnav.workflow import *
from tnav_debug_utilities import *
from datetime import datetime, timedelta


declare_workflow (workflow_name="Petro_convert",
      variables=[{"name" : "GRID_NAME", "type" : "string", "min" : 0, "max" : 3, "values" : ["GDM_with_petro_2023-09-04", "Ach_ungkm_smooth", "Cutted", "Cuted"], "distribution_type" : "Discrete", "discrete_distr_values" : [0, 1, 2, 3], "discrete_distr_probabilities" : [25, 25, 25, 25], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_6", "type" : "real", "min" : 3668, "max" : 3766, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_4", "type" : "real", "min" : 3726, "max" : 3786, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "WOC_DEPTH_S_5", "type" : "real", "min" : 3960, "max" : 4020, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_5", "type" : "real", "min" : 3800, "max" : 3880, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "GOC_DEPTH_S_9", "type" : "real", "min" : 3775, "max" : 3835, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "SWCR_PER", "type" : "real", "min" : 0.1, "max" : 0.336, "values" : [], "distribution_type" : "Normal", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "KRWR", "type" : "real", "min" : 0.02, "max" : 0.238, "values" : [], "distribution_type" : "Log-normal", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "KRWU", "type" : "real", "min" : 0.467, "max" : 0.97, "values" : [], "distribution_type" : "Triangular", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "SWCR_PER2", "type" : "real", "min" : 0.1, "max" : 0.3, "values" : [], "distribution_type" : "Uniform", "discrete_distr_values" : [], "discrete_distr_probabilities" : [], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}, {"name" : "VARIANT", "type" : "string", "min" : 0, "max" : 0, "values" : ["SHORT_AREA"], "distribution_type" : "Discrete", "discrete_distr_values" : [0], "discrete_distr_probabilities" : [100], "initial_distribution" : [], "truncated_mean" : 0, "truncated_sigma" : 0, "mode" : 0}])


Petro_convert_variables = {
"GRID_NAME" : "Cuted",
"GOC_DEPTH_S_6" : 3753,
"GOC_DEPTH_S_4" : 3753,
"WOC_DEPTH_S_5" : 4012,
"GOC_DEPTH_S_5" : 3800,
"GOC_DEPTH_S_9" : 3800,
"SWCR_PER" : 0.282,
"KRWR" : 0.04,
"KRWU" : 0.62,
"SWCR_PER2" : 0.1,
"VARIANT" : "SHORT_AREA"
}

def Petro_convert (variables = Petro_convert_variables):
    pass
    check_launch_method ()

    GRID_NAME = variables["GRID_NAME"]
    GOC_DEPTH_S_6 = variables["GOC_DEPTH_S_6"]
    GOC_DEPTH_S_4 = variables["GOC_DEPTH_S_4"]
    WOC_DEPTH_S_5 = variables["WOC_DEPTH_S_5"]
    GOC_DEPTH_S_5 = variables["GOC_DEPTH_S_5"]
    GOC_DEPTH_S_9 = variables["GOC_DEPTH_S_9"]
    SWCR_PER = variables["SWCR_PER"]
    KRWR = variables["KRWR"]
    KRWU = variables["KRWU"]
    SWCR_PER2 = variables["SWCR_PER2"]
    VARIANT = variables["VARIANT"]

    begin_user_imports ()
    end_user_imports ()

    begin_wf_item (index = 1, name = "PERMX")
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


    begin_wf_item (index = 2, name = "Газ-вода")
    workflow_folder ()
    if True:
        pass



        begin_wf_item (index = 3, name = "SWL")
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
              formula="(PetroTypes==1)*3.4701*exp(-13.63*PORO)+\n(PetroTypes==2)*2.623*exp(-9.052*PORO)+(PetroTypes==3)*3.4701*exp(-13.63*PORO)+(PetroTypes==4)*2.623*exp(-9.052*PORO)",
              variables=variables)
        end_wf_item (index = 3)


        begin_wf_item (index = 4, name = "KRGU")
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="KRGU",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula=" 0.7977*PERMX-0.5825",
              variables=variables)
        end_wf_item (index = 4)


        begin_wf_item (index = 5, name = "SGCR")
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="SGCR",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula="1-SWL-(0.7*(exp (-0.4475*PERMX^0.2223)))*(1-SWL)",
              variables=variables)
        end_wf_item (index = 5)


        begin_wf_item (index = 6, name = "SWCR")
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="SWCR",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula=resolve_variables_in_string (string_with_variables="(PetroTypes==1)*@SWCR_PER@*(1-SGCR-SWL)+SWL+\n(PetroTypes==2)*@SWCR_PER2@*(1-SGCR-SWL)+SWL+(PetroTypes==3)*@SWCR_PER2@*(1-SGCR-SWL)+SWL+(PetroTypes==4)*@SWCR_PER2@*(1-SGCR-SWL)+SWL",
              variables=variables),
              variables=variables)
        end_wf_item (index = 6)


        begin_wf_item (index = 7, name = "KRWR")
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
              formula=resolve_variables_in_string (string_with_variables="@KRWR@",
              variables=variables),
              variables=variables)
        end_wf_item (index = 7)


        begin_wf_item (index = 8, name = "KRWU")
        grid_property_calculator (mesh=find_object (name=resolve_variables_in_string (string_with_variables="@GRID_NAME@",
              variables=variables),
              type="Grid3d"),
              result_grid_property=find_object (name="KRWU",
              type="Grid3dProperty"),
              discrete_output=False,
              use_filter=False,
              user_cut_for_filter=find_object (name="ZONE",
              type="Grid3dProperty"),
              filter_comparator=Comparator (rule="not_equals",
              value=0),
              formula=resolve_variables_in_string (string_with_variables="@KRWR@",
              variables=variables),
              variables=variables)
        end_wf_item (index = 8)



    end_wf_item (index = 2)


    begin_wf_item (index = 10)
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
          formula="(PetroTypes==1)*0.119126+(\nPetroTypes==2)*0.119126+(PetroTypes==3)*0.5385*exp(-2.679*PERMX)+(PetroTypes==4)*0.5385*exp(-2.679*PERMX)",
          variables=variables)
    end_wf_item (index = 10)


    begin_wf_item (index = 11)
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
    end_wf_item (index = 11)


    begin_wf_item (index = 12)
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
    end_wf_item (index = 12)


    begin_wf_item (index = 13)
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
    end_wf_item (index = 13)


    begin_wf_item (index = 14)
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
          formula="if (round(if(PetroTypes==0, 1, PetroTypes))>0,\nround(if(PetroTypes==0, 1, PetroTypes)),\n1)\n\n",
          variables=variables)
    end_wf_item (index = 14)


    begin_wf_item (index = 15)
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
    end_wf_item (index = 15)


    begin_wf_item (index = 16, name = "PCW")
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
          formula="((PetroTypes==1)*1.58+(\nPetroTypes==2)*2.3+\n(PetroTypes==3)*0.98+\n(PetroTypes==4)*0.637)*\n35*0.318316*((PORO/PERMX)^0.5)",
          variables=variables)
    end_wf_item (index = 16)


    begin_wf_item (index = 17)
    static_mapping (cases=find_object (name=resolve_variables_in_string (string_with_variables="@VARIANT@",
          variables=variables),
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
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}, {"description" : "ID_PVTNUM", "keyword" : "PVTNUM", "component" : None, "property" : find_object (name="PVTNUM",
          type="Grid3dProperty"), "constant" : None, "porosity" : "matrix"}])
    end_wf_item (index = 17)


    begin_wf_item (index = 18)
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
    end_wf_item (index = 18)


    begin_wf_item (index = 19)
    adjust_equil_table (table_name="ach4",
          datum_depth=3650,
          datum_pressure=604.08,
          woc_depth=arithmetic (expression="GOC_DEPTH_S_6",
          variables=variables),
          woc_capillary_pressure=0,
          goc_depth=arithmetic (expression="GOC_DEPTH_S_6",
          variables=variables),
          goc_capillary_pressure=0,
          live_black_oil=0,
          wet_gas=0,
          accuracy=None,
          compos_init_type=None,
          compos_press_type_on_contact=None)
    end_wf_item (index = 19)


    begin_wf_item (index = 20)
    adjust_equil_table (table_name="ach51",
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
    end_wf_item (index = 20)


    begin_wf_item (index = 21)
    adjust_equil_table (table_name="ach52",
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
    end_wf_item (index = 21)


    begin_wf_item (index = 22)
    grid_property_calculator (mesh=find_object (name="Cuted",
          type="Grid3d"),
          result_grid_property=find_object (name="Areas",
          type="Grid3dProperty"),
          discrete_output=False,
          use_filter=False,
          user_cut_for_filter=find_object (name="ZONE",
          type="Grid3dProperty"),
          filter_comparator=Comparator (rule="not_equals",
          value=0),
          formula="0",
          variables=variables)
    end_wf_item (index = 22)


    begin_wf_item (index = 23)
    grid_property_edit_inside_polygon (grid=find_object (name="Cuted",
          type="Grid3d"),
          grid_property=find_object (name="Areas",
          type="Grid3dProperty"),
          clear_values=False,
          polygon=find_object (name="1A",
          type="Curve3d"),
          polygon_filter_rule="by_center",
          position="inside",
          stored_value=1,
          use_filter_property=False,
          filter_property=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator=Comparator (rule="not_equals",
          value=0))
    end_wf_item (index = 23)


    begin_wf_item (index = 24)
    grid_property_edit_inside_polygon (grid=find_object (name="Cuted",
          type="Grid3d"),
          grid_property=find_object (name="Areas",
          type="Grid3dProperty"),
          clear_values=False,
          polygon=find_object (name="1A",
          type="Curve3d"),
          polygon_filter_rule="by_center",
          position="inside",
          stored_value=1,
          use_filter_property=False,
          filter_property=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator=Comparator (rule="not_equals",
          value=0))
    end_wf_item (index = 24)


    begin_wf_item (index = 25)
    grid_property_edit_inside_polygon (grid=find_object (name="Cuted",
          type="Grid3d"),
          grid_property=find_object (name="Areas",
          type="Grid3dProperty"),
          clear_values=False,
          polygon=find_object (name="4A",
          type="Curve3d"),
          polygon_filter_rule="by_center",
          position="inside",
          stored_value=4,
          use_filter_property=False,
          filter_property=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator=Comparator (rule="not_equals",
          value=0))
    end_wf_item (index = 25)


    begin_wf_item (index = 26)
    grid_property_edit_inside_polygon (grid=find_object (name="Cuted",
          type="Grid3d"),
          grid_property=find_object (name="Areas",
          type="Grid3dProperty"),
          clear_values=False,
          polygon=find_object (name="5A",
          type="Curve3d"),
          polygon_filter_rule="by_center",
          position="inside",
          stored_value=5,
          use_filter_property=False,
          filter_property=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator=Comparator (rule="not_equals",
          value=0))
    end_wf_item (index = 26)


    begin_wf_item (index = 27)
    map_2d_create_by_grid_property (grid=find_object (name="Cuted",
          type="Grid3d"),
          use_user_cut=True,
          user_cut=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator=Comparator (rule="less",
          value=7),
          use_user_cut_second=False,
          user_cut_second=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator_second=Comparator (rule="equals",
          value=1),
          use_zone=False,
          zone=find_object (name="ZONE",
          type="Grid3dProperty"),
          continuous_properties=True,
          continues_cube_and_map_table=[{"use" : True, "cube" : find_object (name="PT_corr",
          type="Grid3dProperty"), "map_2d" : find_object (name="New_petro",
          type="Map2d"), "zone_id" : 0, "method" : "average", "smooth" : False, "blocked_wells" : None}, {"use" : True, "cube" : find_object (name="PetroTypes_final+smooth Copy1",
          type="Grid3dProperty"), "map_2d" : find_object (name="Old_petro",
          type="Map2d"), "zone_id" : 0, "method" : "average", "smooth" : False, "blocked_wells" : None}],
          discrete_properties=True,
          discrete_cube_and_map_table=[{"use" : False, "cube" : find_object (name="PT_corr",
          type="Grid3dProperty"), "code_value" : 0, "map_2d" : find_object (name="Heff_from3D_Ach3",
          type="Map2d"), "zone_id" : 0, "method" : "top", "smooth" : False, "blocked_wells" : None}, {"use" : False, "cube" : find_object (name="PetroTypes_final+smooth Copy1",
          type="Grid3dProperty"), "code_value" : 3, "map_2d" : find_object (name="Heff_from3D_Ach4",
          type="Map2d"), "zone_id" : 0, "method" : "thickness", "smooth" : False, "blocked_wells" : None}, {"use" : False, "cube" : find_object (name="ZONE",
          type="Grid3dProperty"), "code_value" : 5, "map_2d" : find_object (name="Heff_from3D_Ach51",
          type="Map2d"), "zone_id" : 0, "method" : "thickness", "smooth" : False, "blocked_wells" : None}, {"use" : False, "cube" : find_object (name="ZONE",
          type="Grid3dProperty"), "code_value" : 7, "map_2d" : find_object (name="Heff_from3D_Ach523",
          type="Map2d"), "zone_id" : 0, "method" : "thickness", "smooth" : False, "blocked_wells" : None}],
          smoothing_radius=10,
          ignore_faults=False,
          set_na_instead_of_zero=False,
          compatibility_options=False,
          set_na_outside_filter=True,
          grid_2d_source="custom",
          add_half_cell_offset=False,
          subdivision=3,
          grid_2d_settings=Grid2DSettings (grid_2d_settings_shown=True,
          autodetect_box=True,
          min_x=567912.01707,
          min_y=7349193.83429,
          length_x=35299.99417,
          length_y=67300.02597000078,
          margin_x=0,
          margin_y=0,
          consider_blank_nodes=False,
          autodetect_angle=True,
          angle=0,
          autodetect_grid=False,
          grid_adjust_mode="step",
          step_x=100,
          step_y=100,
          counts_x=0,
          counts_y=0,
          sample_object=absolute_object_name (name=None,
          typed_names=[typed_object_name (obj_name="Map boundary",
          obj_type="Curve3d")]),
          autodetect_during_wf_calculation=True))
    end_wf_item (index = 27)


    begin_wf_item (index = 28)
    grid_property_calculator (mesh=find_object (name="Cuted",
          type="Grid3d"),
          result_grid_property=find_object (name="PT_corr",
          type="Grid3dProperty"),
          discrete_output=False,
          use_filter=False,
          user_cut_for_filter=find_object (name="ZONE",
          type="Grid3dProperty"),
          filter_comparator=Comparator (rule="not_equals",
          value=0),
          formula="if Property1>0 & ZONE <7 then 2\nelseif grid_property (\"PetroTypes_final+smooth\")==2 & PORO>0.15 then 1\nelse grid_property (\"PetroTypes_final+smooth\")\nendif\n",
          variables=variables)
    end_wf_item (index = 28)


    begin_wf_item (index = 29)
    grid_property_calculator (mesh=find_object (name="Cuted",
          type="Grid3d"),
          result_grid_property=find_object (name="PT_corr",
          type="Grid3dProperty"),
          discrete_output=False,
          use_filter=False,
          user_cut_for_filter=find_object (name="ZONE",
          type="Grid3dProperty"),
          filter_comparator=Comparator (rule="not_equals",
          value=0),
          formula="if Property1>0 & ZONE <7 then 2\nelseif grid_property (\"PetroTypes_final+smooth\")==2 & PORO>0.15 then 1\nelse grid_property (\"PetroTypes_final+smooth\")\nendif\n",
          variables=variables)
    end_wf_item (index = 29)


    begin_wf_item (index = 30)
    map_2d_create_by_grid_property (grid=find_object (name="Cuted",
          type="Grid3d"),
          use_user_cut=True,
          user_cut=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator=Comparator (rule="less",
          value=7),
          use_user_cut_second=False,
          user_cut_second=find_object (name="ZONE",
          type="Grid3dProperty"),
          comparator_second=Comparator (rule="equals",
          value=1),
          use_zone=False,
          zone=find_object (name="ZONE",
          type="Grid3dProperty"),
          continuous_properties=True,
          continues_cube_and_map_table=[{"use" : True, "cube" : find_object (name="PT_corr",
          type="Grid3dProperty"), "map_2d" : find_object (name="New_petro",
          type="Map2d"), "zone_id" : 0, "method" : "average", "smooth" : False, "blocked_wells" : None}, {"use" : True, "cube" : find_object (name="PetroTypes_final+smooth Copy1",
          type="Grid3dProperty"), "map_2d" : find_object (name="Old_petro",
          type="Map2d"), "zone_id" : 0, "method" : "average", "smooth" : False, "blocked_wells" : None}],
          discrete_properties=True,
          discrete_cube_and_map_table=[{"use" : False, "cube" : find_object (name="PT_corr",
          type="Grid3dProperty"), "code_value" : 0, "map_2d" : find_object (name="Heff_from3D_Ach3",
          type="Map2d"), "zone_id" : 0, "method" : "top", "smooth" : False, "blocked_wells" : None}, {"use" : False, "cube" : find_object (name="PetroTypes_final+smooth Copy1",
          type="Grid3dProperty"), "code_value" : 3, "map_2d" : find_object (name="Heff_from3D_Ach4",
          type="Map2d"), "zone_id" : 0, "method" : "thickness", "smooth" : False, "blocked_wells" : None}, {"use" : False, "cube" : find_object (name="ZONE",
          type="Grid3dProperty"), "code_value" : 5, "map_2d" : find_object (name="Heff_from3D_Ach51",
          type="Map2d"), "zone_id" : 0, "method" : "thickness", "smooth" : False, "blocked_wells" : None}, {"use" : False, "cube" : find_object (name="ZONE",
          type="Grid3dProperty"), "code_value" : 7, "map_2d" : find_object (name="Heff_from3D_Ach523",
          type="Map2d"), "zone_id" : 0, "method" : "thickness", "smooth" : False, "blocked_wells" : None}],
          smoothing_radius=10,
          ignore_faults=False,
          set_na_instead_of_zero=False,
          compatibility_options=False,
          set_na_outside_filter=True,
          grid_2d_source="custom",
          add_half_cell_offset=False,
          subdivision=3,
          grid_2d_settings=Grid2DSettings (grid_2d_settings_shown=True,
          autodetect_box=True,
          min_x=567912.01707,
          min_y=7349193.83429,
          length_x=35299.99417,
          length_y=67300.02597000078,
          margin_x=0,
          margin_y=0,
          consider_blank_nodes=False,
          autodetect_angle=True,
          angle=0,
          autodetect_grid=False,
          grid_adjust_mode="step",
          step_x=100,
          step_y=100,
          counts_x=0,
          counts_y=0,
          sample_object=absolute_object_name (name=None,
          typed_names=[typed_object_name (obj_name="Map boundary",
          obj_type="Curve3d")]),
          autodetect_during_wf_calculation=True))
    end_wf_item (index = 30)


