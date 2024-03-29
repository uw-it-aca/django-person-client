# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Person(models.Model):
    uwnetid = models.TextField(unique=True, blank=True, null=True)
    uwregid = models.TextField(unique=True, blank=True, null=True)
    pronouns = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    preferred_first_name = models.TextField(blank=True, null=True)
    preferred_middle_name = models.TextField(blank=True, null=True)
    preferred_surname = models.TextField(blank=True, null=True)
    whitepages_publish = models.BooleanField(blank=True, null=True)
    is_active_student = models.BooleanField(
        db_column='_is_active_student', blank=True, null=True)
    is_active_employee = models.BooleanField(
        db_column='_is_active_employee', blank=True, null=True)
    last_changed = models.DateTimeField(
        db_column='_last_changed', blank=True, null=True)
    system_key = models.TextField(blank=True, null=True)
    prior_uwnetids = ArrayField(models.CharField(max_length=24))
    prior_uwregids = ArrayField(models.CharField(max_length=32))

    class Meta:
        managed = False
        db_table = 'person'


class Employee(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING)
    employee_number = models.TextField()
    employee_affiliation_state = models.TextField(blank=True, null=True)
    email_addresses = ArrayField(models.CharField(max_length=100))
    home_department = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    last_changed = models.DateTimeField(
        db_column='_last_changed', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Adviser(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    is_dept_adviser = models.BooleanField(blank=True, null=True)
    advising_email = models.TextField(blank=True, null=True)
    advising_phone_number = models.TextField(blank=True, null=True)
    advising_program = models.TextField(blank=True, null=True)
    advising_pronouns = models.TextField(blank=True, null=True)
    booking_url = models.TextField(blank=True, null=True)
    last_changed = models.DateTimeField(
        db_column='_last_changed', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adviser'


class Term(models.Model):
    year = models.SmallIntegerField()
    quarter = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'term'
        unique_together = (('year', 'quarter'),)


class Major(models.Model):
    major_abbr_code = models.TextField(blank=True, null=True)
    major_full_name = models.TextField(blank=True, null=True)
    major_name = models.TextField(blank=True, null=True)
    major_short_name = models.TextField(blank=True, null=True)
    major_branch = models.SmallIntegerField(blank=True, null=True)
    major_cip_code = models.IntegerField(blank=True, null=True)
    major_concur_cc = models.BooleanField(blank=True, null=True)
    major_dept = models.TextField(blank=True, null=True)
    major_desc = models.TextField(blank=True, null=True)
    major_dist_learn = models.BooleanField(blank=True, null=True)
    major_evening = models.BooleanField(blank=True, null=True)
    major_first_qtr = models.SmallIntegerField(blank=True, null=True)
    major_first_yr = models.SmallIntegerField(blank=True, null=True)
    major_gnm = models.BooleanField(blank=True, null=True)
    major_grad_certif = models.BooleanField(blank=True, null=True)
    major_graduate = models.BooleanField(blank=True, null=True)
    major_home_url = models.TextField(blank=True, null=True)
    major_last_qtr = models.SmallIntegerField(blank=True, null=True)
    major_last_yr = models.SmallIntegerField(blank=True, null=True)
    major_measles_ex = models.BooleanField(blank=True, null=True)
    major_minor = models.BooleanField(blank=True, null=True)
    major_non_degree = models.BooleanField(blank=True, null=True)
    major_nonmatric = models.BooleanField(blank=True, null=True)
    major_not_termin = models.BooleanField(blank=True, null=True)
    major_osfa_inelig = models.BooleanField(blank=True, null=True)
    major_pathway = models.SmallIntegerField(blank=True, null=True)
    major_premaj = models.BooleanField(blank=True, null=True)
    major_premaj_ext = models.BooleanField(blank=True, null=True)
    major_professional = models.BooleanField(blank=True, null=True)
    major_ss_inelig = models.BooleanField(blank=True, null=True)
    major_ss_std_act = models.BooleanField(blank=True, null=True)
    major_ug_certif = models.BooleanField(blank=True, null=True)
    major_undergrad = models.BooleanField(blank=True, null=True)
    college = models.TextField(blank=True, null=True)
    major_branch_name = models.TextField(blank=True, null=True)
    major_college_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major'


class Sport(models.Model):
    sport_code = models.TextField(blank=True, null=True)
    short_sport_name = models.TextField(blank=True, null=True)
    sport_descrip = models.TextField(blank=True, null=True)
    sport_reg_pr_aut = models.BooleanField(blank=True, null=True)
    sport_reg_pr_spr = models.BooleanField(blank=True, null=True)
    sport_reg_pr_sum = models.BooleanField(blank=True, null=True)
    sport_reg_pr_win = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sport'


class Student(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING)
    academic_term = models.ForeignKey(
        Term, models.DO_NOTHING, blank=True, null=True)
    system_key = models.TextField(unique=True)
    student_number = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    student_email = models.TextField(blank=True, null=True)
    external_email = models.TextField(blank=True, null=True)
    local_phone_number = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    cumulative_gpa = models.TextField(blank=True, null=True)
    campus_code = models.SmallIntegerField(blank=True, null=True)
    campus_desc = models.TextField(blank=True, null=True)
    perm_addr_line1 = models.TextField(blank=True, null=True)
    perm_addr_line2 = models.TextField(blank=True, null=True)
    perm_addr_city = models.TextField(blank=True, null=True)
    perm_addr_state = models.TextField(blank=True, null=True)
    perm_addr_5digit_zip = models.TextField(blank=True, null=True)
    perm_addr_4digit_zip = models.TextField(blank=True, null=True)
    perm_addr_postal_code = models.TextField(blank=True, null=True)
    last_changed = models.DateTimeField(
        db_column='_last_changed', blank=True, null=True)
    class_code = models.SmallIntegerField(blank=True, null=True)
    class_desc = models.TextField(blank=True, null=True)
    perm_addr_country = models.TextField(blank=True, null=True)
    registered_in_quarter = models.BooleanField(blank=True, null=True)
    resident_code = models.SmallIntegerField(blank=True, null=True)
    resident_desc = models.TextField(blank=True, null=True)
    total_credits = models.TextField(blank=True, null=True)
    total_deductible_credits = models.TextField(blank=True, null=True)
    total_extension_credits = models.TextField(blank=True, null=True)
    total_grade_attempted = models.TextField(blank=True, null=True)
    total_grade_points = models.TextField(blank=True, null=True)
    total_lower_div_transfer_credits = models.TextField(blank=True, null=True)
    total_non_graded_credits = models.TextField(blank=True, null=True)
    total_registered_credits = models.TextField(blank=True, null=True)
    total_transfer_credits = models.TextField(blank=True, null=True)
    total_uw_credits = models.TextField(blank=True, null=True)
    total_upper_div_transfer_credits = models.TextField(blank=True, null=True)
    veteran_benefit_code = models.SmallIntegerField(blank=True, null=True)
    veteran_benefit_desc = models.TextField(blank=True, null=True)
    veteran_desc = models.TextField(blank=True, null=True)
    admitted_for_yr_qtr_desc = models.TextField(blank=True, null=True)
    admitted_for_yr_qtr_id = models.TextField(blank=True, null=True)
    application_status_code = models.SmallIntegerField(blank=True, null=True)
    application_status_desc = models.TextField(blank=True, null=True)
    application_type_code = models.TextField(blank=True, null=True)
    application_type_desc = models.TextField(blank=True, null=True)
    applied_to_graduate_yr_qtr_desc = models.TextField(blank=True, null=True)
    applied_to_graduate_yr_qtr_id = models.TextField(blank=True, null=True)
    asuwind = models.BooleanField(blank=True, null=True)
    directory_release_ind = models.BooleanField(blank=True, null=True)
    disability_ind = models.BooleanField(blank=True, null=True)
    enroll_status_code = models.SmallIntegerField(blank=True, null=True)
    exemption_code = models.SmallIntegerField(blank=True, null=True)
    exemption_desc = models.TextField(blank=True, null=True)
    first_generation_4yr_ind = models.BooleanField(blank=True, null=True)
    first_generation_ind = models.BooleanField(blank=True, null=True)
    high_school_gpa = models.TextField(blank=True, null=True)
    high_school_graduation_date = models.TextField(blank=True, null=True)
    honors_program_code = models.TextField(blank=True, null=True)
    honors_program_ind = models.BooleanField(blank=True, null=True)
    jr_col_gpa = models.TextField(blank=True, null=True)
    last_enrolled_yr_qtr_desc = models.TextField(blank=True, null=True)
    last_enrolled_yr_qtr_id = models.TextField(blank=True, null=True)
    local_addr_4digit_zip = models.TextField(blank=True, null=True)
    local_addr_5digit_zip = models.TextField(blank=True, null=True)
    local_addr_city = models.TextField(blank=True, null=True)
    local_addr_country = models.TextField(blank=True, null=True)
    local_addr_line1 = models.TextField(blank=True, null=True)
    local_addr_line2 = models.TextField(blank=True, null=True)
    local_addr_postal_code = models.TextField(blank=True, null=True)
    local_addr_state = models.TextField(blank=True, null=True)
    new_continuing_returning_code = models.SmallIntegerField(
        blank=True, null=True)
    new_continuing_returning_desc = models.TextField(blank=True, null=True)
    previous_institution_name = models.TextField(blank=True, null=True)
    previous_institution_type = models.TextField(blank=True, null=True)
    previous_institution_type_desc = models.TextField(blank=True, null=True)
    record_load_dttm = models.TextField(blank=True, null=True)
    record_update_dttm = models.TextField(blank=True, null=True)
    reg_first_yr_qtr_desc = models.TextField(blank=True, null=True)
    reg_first_yr_qtr_id = models.TextField(blank=True, null=True)
    registration_hold_ind = models.BooleanField(blank=True, null=True)
    special_program_code = models.TextField(blank=True, null=True)
    special_program_desc = models.TextField(blank=True, null=True)
    sr_col_gpa = models.TextField(blank=True, null=True)
    birth_city = models.TextField(blank=True, null=True)
    birth_country = models.TextField(blank=True, null=True)
    birth_state = models.TextField(blank=True, null=True)
    child_of_alumni = models.BooleanField(blank=True, null=True)
    citizen_country = models.TextField(blank=True, null=True)
    emergency_email = models.TextField(blank=True, null=True)
    emergency_name = models.TextField(blank=True, null=True)
    emergency_phone = models.TextField(blank=True, null=True)
    iss_perm_resident_country = models.TextField(blank=True, null=True)
    parent_name = models.TextField(blank=True, null=True)
    visa_type = models.TextField(blank=True, null=True)
    intended_major1_code = models.TextField(blank=True, null=True)
    intended_major2_code = models.TextField(blank=True, null=True)
    intended_major3_code = models.TextField(blank=True, null=True)
    requested_major1_code = models.TextField(blank=True, null=True)
    requested_major2_code = models.TextField(blank=True, null=True)
    requested_major3_code = models.TextField(blank=True, null=True)
    major_1 = models.ForeignKey(
        Major, models.DO_NOTHING, related_name='student_major_1_set',
        blank=True, null=True)
    major_2 = models.ForeignKey(
        Major, models.DO_NOTHING, related_name='student_major_2_set',
        blank=True, null=True)
    major_3 = models.ForeignKey(
        Major, models.DO_NOTHING, related_name='student_major_3_set',
        blank=True, null=True)
    pending_major_1 = models.ForeignKey(
        Major, models.DO_NOTHING, related_name='student_pending_major_1_set',
        blank=True, null=True)
    pending_major_2 = models.ForeignKey(
        Major, models.DO_NOTHING, related_name='student_pending_major_2_set',
        blank=True, null=True)
    pending_major_3 = models.ForeignKey(
        Major, models.DO_NOTHING, related_name='student_pending_major_3_set',
        blank=True, null=True)
    enroll_status_request_code = models.TextField(blank=True, null=True)
    enroll_status_desc = models.TextField(blank=True, null=True)
    spp_qtrs_allowed = models.SmallIntegerField(blank=True, null=True)
    spp_qtrs_used = models.SmallIntegerField(blank=True, null=True)
    spp_qtrs_used_dt = models.DateTimeField(blank=True, null=True)
    spp_status = models.SmallIntegerField(blank=True, null=True)
    spp_status_dt = models.DateTimeField(blank=True, null=True)
    spp_category = models.SmallIntegerField(blank=True, null=True)
    spp_category_dt = models.DateTimeField(blank=True, null=True)
    ethnic_code = models.TextField(blank=True, null=True)
    ethnic_desc = models.TextField(blank=True, null=True)
    ethnic_long_desc = models.TextField(blank=True, null=True)
    ethnic_group_code = models.TextField(blank=True, null=True)
    hispanic_code = models.TextField(blank=True, null=True)
    hispanic_desc = models.TextField(blank=True, null=True)
    hispanic_long_desc = models.TextField(blank=True, null=True)
    hispanic_group_code = models.TextField(blank=True, null=True)
    deceased_date = models.DateField(blank=True, null=True)
    ethnic_group_desc = models.TextField(blank=True, null=True)
    hispanic_group_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentHold(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    seq = models.SmallIntegerField()
    hold_dt = models.DateTimeField(blank=True, null=True)
    hold_office = models.TextField(blank=True, null=True)
    hold_office_desc = models.TextField(blank=True, null=True)
    hold_reason = models.TextField(blank=True, null=True)
    hold_type = models.SmallIntegerField(blank=True, null=True)
    hold_type_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_hold'
        unique_together = (('student', 'seq'),)


class StudentToAdviser(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    adviser = models.ForeignKey(Adviser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_to_adviser'
        unique_together = (('student', 'adviser'),)


class StudentToSport(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    sport = models.ForeignKey(Sport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_to_sport'
        unique_together = (('student', 'sport'),)


class Degree(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    degree_term = models.ForeignKey(
        Term, models.DO_NOTHING, blank=True, null=True)
    campus_code = models.SmallIntegerField(blank=True, null=True)
    degree_abbr_code = models.TextField(blank=True, null=True)
    degree_pathway_num = models.SmallIntegerField(blank=True, null=True)
    degree_level_code = models.TextField(blank=True, null=True)
    degree_level_desc = models.TextField(blank=True, null=True)
    degree_type_code = models.TextField(blank=True, null=True)
    degree_level_type_desc = models.TextField(blank=True, null=True)
    degree_desc = models.TextField(blank=True, null=True)
    degree_uw_credits = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    degree_transfer_credits = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    degree_extension_credits = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    degree_gpa = models.TextField(blank=True, null=True)
    fin_org_key = models.TextField(blank=True, null=True)
    primary_fin_org_key = models.TextField(blank=True, null=True)
    degree_college_code = models.TextField(blank=True, null=True)
    degree_status_code = models.TextField(blank=True, null=True)
    degree_status_desc = models.TextField(blank=True, null=True)
    degree_date = models.DateField(blank=True, null=True)
    degree_grad_honor = models.SmallIntegerField(blank=True, null=True)
    degree_index = models.SmallIntegerField(blank=True, null=True)
    degree_major_index = models.SmallIntegerField(blank=True, null=True)
    campus_name = models.TextField(blank=True, null=True)
    degree_college_name = models.TextField(blank=True, null=True)
    degree_grad_honor_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'degree'
        unique_together = ((
            'student', 'degree_term', 'campus_code', 'degree_abbr_code',
            'degree_pathway_num'),)


class Transcript(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    tran_term = models.ForeignKey(
        Term, models.DO_NOTHING, blank=True, null=True)
    leave_ends_term = models.ForeignKey(
        Term, models.DO_NOTHING, related_name='transcript_leave_ends_term_set',
        blank=True, null=True)
    veteran = models.SmallIntegerField(blank=True, null=True)
    veteran_benefit = models.SmallIntegerField(blank=True, null=True)
    resident = models.SmallIntegerField(blank=True, null=True)
    resident_cat = models.TextField(blank=True, null=True)
    qtr_grade_points = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    qtr_graded_attmp = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    class_code = models.SmallIntegerField(blank=True, null=True)
    honors_program = models.SmallIntegerField(blank=True, null=True)
    special_program = models.SmallIntegerField(blank=True, null=True)
    scholarship_type = models.SmallIntegerField(blank=True, null=True)
    yearly_honor_type = models.SmallIntegerField(blank=True, null=True)
    exemption_code = models.SmallIntegerField(blank=True, null=True)
    num_ind_study = models.SmallIntegerField(blank=True, null=True)
    num_courses = models.SmallIntegerField(blank=True, null=True)
    enroll_status = models.SmallIntegerField(blank=True, null=True)
    tenth_day_credits = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    tr_en_stat_dt = models.DateTimeField(blank=True, null=True)
    last_changed = models.DateTimeField(
        db_column='_last_changed', blank=True, null=True)
    over_qtr_deduct = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    over_qtr_grade_at = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    over_qtr_grade_pt = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    over_qtr_nongrd = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    qtr_comment = models.TextField(blank=True, null=True)
    qtr_deductible = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    qtr_nongrd_earned = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    add_to_cum = models.BooleanField(blank=True, null=True)
    scholarship_abbr = models.TextField(blank=True, null=True)
    scholarship_desc = models.TextField(blank=True, null=True)
    enroll_status_request_code = models.TextField(blank=True, null=True)
    enroll_status_desc = models.TextField(blank=True, null=True)
    special_program_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transcript'


class Transfer(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    institution_code = models.TextField(blank=True, null=True)
    year_ending = models.SmallIntegerField(blank=True, null=True)
    year_beginning = models.SmallIntegerField(blank=True, null=True)
    transfer_gpa = models.DecimalField(
        max_digits=5, decimal_places=5, blank=True, null=True)
    trans_updt_dt = models.DateTimeField(blank=True, null=True)
    trans_updt_id = models.TextField(blank=True, null=True)
    degree_earned = models.TextField(blank=True, null=True)
    degree_earned_yr = models.SmallIntegerField(blank=True, null=True)
    degree_earned_mo = models.SmallIntegerField(blank=True, null=True)
    credential_lvl = models.SmallIntegerField(blank=True, null=True)
    credential_yr = models.SmallIntegerField(blank=True, null=True)
    transfer_comment = models.TextField(blank=True, null=True)
    institution_name = models.TextField(blank=True, null=True)
    inst_addr_line_1 = models.TextField(blank=True, null=True)
    inst_addr_line_2 = models.TextField(blank=True, null=True)
    inst_city = models.TextField(blank=True, null=True)
    inst_state = models.TextField(blank=True, null=True)
    inst_zip_5 = models.TextField(blank=True, null=True)
    inst_zip_filler = models.TextField(blank=True, null=True)
    inst_country = models.TextField(blank=True, null=True)
    inst_postal_cd = models.TextField(blank=True, null=True)
    inst_record_stat = models.BooleanField(blank=True, null=True)
    two_year = models.BooleanField(blank=True, null=True)
    wa_cc = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer'
