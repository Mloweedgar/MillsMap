import json, csv

secret_tokens = json.load(open('secret_tokens.json', 'r'))
email = secret_tokens['email']
password = secret_tokens['password']
aut = (email, password)
base_url = 'https://schooldataserver.tz'

mill_columns = 'coordinatesDescription_coodinates_coordinates,start,end,school_details-school_name,interviewee_details-interviewee_role,interviewee_details-date_of_interview,school_details-school_name,school_details-school_type,school_details_Location-addr_region,\
school_details_Location-addr_district,school_details_Location-addr_ward_shehiya,school_details_Location-other_ward_sheiya,school_details_Location-addr_subward,school_details_Status-school_registration_number,\
school_details_Status-school_distance_centre,school_details_Status-status,school_details_Status-title_deed_number,school_details_Status-school_coverage,school_details_Status-school_services,school_details_Status-school_ownership,\
school_details_Status-school_accommodation,school_details_Teachers_student-school_teachers_male,school_details_Teachers_student-school_teachers_female,school_details_Teachers_student-school_teachers,\
school_details_Teachers_student-enrolled_pre_primary,school_details_Teachers_student-school_students_boys_pre_primary,school_details_Teachers_student-school_students_girlspre_primary,\
school_details_Teachers_student-school_students_pre_primary,school_details_Teachers_student-enrolled_primary,school_details_Teachers_student-school_students_boys_primary,school_details_Teachers_student-school_students_girls_primary,\
school_details_Teachers_student-school_students_primary,school_details_Teachers_student-school_students_average_class,school_details_Teachers_student-droupout,school_details_Teachers_student-droupout_other,\
school_details_Teachers_student-school_students_special_educational_needs,school_details_Teachers_student-school_students_specialneeds_number_female,school_details_Teachers_student-school_students_specialneeds_number_male,\
school_details_NonTeaching-non_teaching_staff_status,school_details_NonTeaching-nonteaching_staff,school_details_NonTeaching-nonteaching_staff_other,school_details_NonTeaching-How_many_driver,school_details_NonTeaching-How_many_gardener,\
school_details_NonTeaching-How_many_cook,school_details_NonTeaching-How_many_cleaner,school_details_NonTeaching-How_many_guard,school_details_NonTeaching-How_many_secretary,school_details_NonTeaching-How_many_matron_patron,\
school_details_NonTeaching-nonstaff_payments,feeding-feeding_status,feeding-feeding_status_yes_allstudents,feeding-feeding_status_no_allstudents,feeding-feeding_status_no_allstudents_other,feeding-pre_primary_students,\
feeding-standard_1_students,feeding-standard_2_students,feeding-standard_3_students,feeding-standard_4_students,feeding-standard_5_students,feeding-standard_6_students,feeding-standard_7_students,Food_purchases-feeding_frequency,\
Food_purchases-how_many_times,Food_purchases-feeding_program_planning,Food_purchases-foodtype,Food_purchases-foodtype_other,Food_purchases-meals_timetable,Food_purchases-meals_timetable_changes,Food_purchases-meals_timetable_changes_other,\
Food_purchases-food_othering,Food_purchases-feeding_sustainable,Food_purchases-parent_commettee_for_school_feeding,Sponsorship-feeding_program_provider_or_sponsor,Sponsorship-feeding_program_provider_or_sponsor_other,\
Sponsorship-parents_name,Sponsorship-parents_number,Sponsorship-school_name,Sponsorship-school_number,Sponsorship-government_name,Sponsorship-government_number,Sponsorship-religious_institution_name,Sponsorship-religious_institution_number,\
Sponsorship-non_government_organization_name,Sponsorship-non_government_organization_number,Sponsorship-individual_name,Sponsorship-individual_number,Sponsorship-international_institution_name,Sponsorship-international_institution_number,\
Food-food_source,Food-food_supplier,Food-food_supplier_other,Food-food_store,Food-food_store_other,Food-often_buying_receive,Food-often_buying_receive_other,Food-fortified_food,Food-fortified_type,Food-bio_fortified_food,\
Food-biofortified_type,Food-biofortified_type_other,school_farm-staple_foods_available,school_farm-staple_foods_available_other,school_farm-school_garden_or_farm,school_farm-school_garden_or_farm_size,school_farm-school_poultry,\
school_farm-cultivated_vegetables_or_crops,school_farm-cultivated_vegetables_or_crops_other,school_farm-grow_biofortified_food,school_farm-cultivated_bio_fortified,school_farm-cultivated_bio_fortified_other,\
school_farm-school_garden_or_farm_maintainer,school_farm-school_garden_or_farm_maintainer_other,school_farm-school_garden_or_farm_produce_uses,school_farm-school_garden_or_farm_produce_uses_other,Nutrition_club-school_nutrition_club,\
Nutrition_club-school_nutrition_club_meet_frequency,Nutrition_club-school_nutrition_club_meet_frequency_other,Nutrition_club-school_nutrition_other_clubs,Nutrition_club-other_club_nutrition_agenda,Cooking-cooking_area,\
Cooking-cooking_area_other,Cooking-cooking_stoves,Cooking-energy,Cooking-school_utensils,Cooking-school_utensils_other,Cooking-utensil_store,Cooking-utensil_store_other,Cooking-school_dining_hall,Electricity-school_electricity_access,\
Electricity-school_electricity_source,Electricity-school_electricity_source_other,Electricity-school_electrical_appliances,Electricity-school_electrical_appliances_list,Electricity-school_electrical_appliances_list_other,\
Electricity-school_water_source,Electricity-school_water_source_other,coordinatesDescription-teacher_canupdate'

columns = {'Submissions': mill_columns}

# filters = {
#     'school_details_Location_addr_region': 'Region',
#     'school_details_Location_addr_district': 'District',
#     'Food_purchases_foodtype': 'Food purchases type',
#     'school_details_school_type': 'School type',
#     'school_details_Status_school_ownership': 'School ownership',
#     'school_details_Status_school_accommodation': 'School Accommodation',
#     'feeding_feeding_status': 'Feeding Status',
#     'Food_purchases_feeding_program_planning': 'Feeding Program Planning',
#     'Food_purchases_meals_timetable': 'Meals Timetable',
#     'Sponsorship_feeding_program_provider_or_sponsor': 'School Meals Sponsor',
#     'Food_food_source': 'Food Source',
#     'Food_fortified_food': 'Cooking Fortified food',
#     'Food_fortified_type': 'Fortified type',
#     'Food_bio_fortified_food': 'Cooking Biofortified food',
#     'Food_biofortified_type': 'Biofortified type',
#     'school_farm_staple_foods_available': 'Staple foods available',
#     'school_farm_school_poultry': 'School poultry',
#     'school_farm_school_garden_or_farm': 'Does the school have the Farm or Garden',
#     'school_farm_cultivated_vegetables_or_crops': 'What vegetables or crops are cultivated in the school garden or farm?',
#     'Nutrition_club_school_nutrition_club': 'School nutrition club',
#     'Cooking_cooking_area': 'Cooking area',
#     'Cooking_energy': 'Cooking Energy',
#     'Electricity_school_electricity_access': 'Electricity access',
# }
filters = list()
with open('app/static/js/filter_graphic_config.csv', newline='') as file:
    form = csv.DictReader(file)
    for row in form:
        filters.append(row)
# print(filter_graphic_config)
# filters = [
#     {'key': 'school_details_Location_addr_region', 'name': 'Region', 'array_column': '0', 'single_column': '0', 'piechart': '1', 'filter': '1'},
# ]

infographics = {
    # 'school_details_Location_addr_region': 'Region',
    # 'school_details_Location_addr_district': 'District',
    'Food_purchases_foodtype': 'Food purchases type',
    'school_details_school_type': 'School type',
    'school_details_Status_school_ownership': 'School ownership',
    'school_details_Status_school_accommodation': 'School Accommodation',
    'feeding_feeding_status': 'Feeding Status',
    'Food_purchases_feeding_program_planning': 'Feeding Program Planning',
    # 'Food_purchases_meals_timetable': 'Meals Timetable',
    'Sponsorship_feeding_program_provider_or_sponsor': 'School Meals Sponsor',
    'Food_food_source': 'Food Source',
    'Food_fortified_food': 'Cooking Fortified food',
    'Food_fortified_type': 'Fortified type',
    'Food_bio_fortified_food': 'Cooking Biofortified food',
    'Food_biofortified_type': 'Biofortified type',
    'school_farm_staple_foods_available': 'Staple foods available',
    'school_farm_school_poultry': 'School poultry',
    'school_farm_school_garden_or_farm': 'Does the school have the Farm or Garden',
    'school_farm_cultivated_vegetables_or_crops': 'What vegetables or crops are cultivated in the school garden or farm?',
    'Nutrition_club_school_nutrition_club': 'School nutrition club',
    'Cooking_cooking_area': 'Cooking area',
    'Cooking_energy': 'Cooking Energy',
    'Electricity_school_electricity_access': 'Electricity access',
}
submission_files_path = 'app/submission_files'
figures_path = 'app/static/figures'
update_time = 60 #time in seconds to check and update new submissions
id_columns = ['geo']
# Get the form configured data
# TODO: Do not create the form config file on the fly.
# This should be a database table ideally.
form_details = list()
with open('app/static/form_config.csv', newline='') as file:
    form_config = csv.DictReader(file)
    for row in form_config:
        form_details.append(row)
form_index = 0
projectId = form_details[form_index]['projectId']
formId = form_details[form_index]['formId']
lastNumberRecordsMills = form_details[form_index]['lastNumberRecordsMills']

array_columns = [
    'Food_purchases_foodtype',
    'Sponsorship_feeding_program_provider_or_sponsor',
    'Food_food_source',
    'Food_fortified_type',
    'Food_biofortified_type',
    'school_farm_staple_foods_available',
    'school_farm_cultivated_vegetables_or_crops',
    'Cooking_cooking_area',
    'Cooking_energy'
    ]
single_columns = [
    'school_details_Location_addr_district', 
    'school_details_Status_school_accommodation',
    'school_farm_school_garden_or_farm'
    ]

# array_columns = ['non_operational', 'commodity_milled', 'energy_source']
# single_columns = ['Packaging_flour_fortified', 'operational_mill', 'interviewee_mill_owner', 'Packaging_flour_fortified_standard', 'mill_type']
