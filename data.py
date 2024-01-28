class RowanUniversityData:
    def __init__(self):
        self.application_info = {
            "common_application": {"deadline": "March 1 (Fall) / Jan. 5 (Spring)", "fee": "$65"},
            "coalition_application": {"deadline": "March 1 (Fall) / Jan. 5 (Spring)", "fee": "$65"},
            "rowan_application": {"deadline": "March 1 (Fall) / Jan. 5 (Spring)", "fee": "$65"},
            "degree_in_3_application": {"deadline": "May 1", "fee": "No Fee"},
            "fafsa_application": {"deadline": "April 15", "fee": "No Fee"},
            "rowan_choice_application": {"deadline": "April 1", "fee": "$65"}
        }

        self.confirmation_of_enrollment_info = {
            "fall": {"deadline": "May 1", "fee": "$200"},
            "spring": {"deadline": "Jan. 10", "fee": "$200"}
        }

        self.performing_creative_arts_info = {
            "deadline": {"fall": "April 27", "spring": "Oct. 26"},
            "fee": "$45",
            "confirmation_of_enrollment_deadline": {"fall": "July 1", "spring": "Dec. 1"}
        }

        self.transfer_requirements = {
            "unofficial_transcript_deadline": "Admissions decision based on unofficial transcript",
            "official_transcript_deadline": "Send official college transcript(s) for formal credit evaluation",
            "transfer_credit_appeal_process": "Complete Transfer Credit Appeal Process if needed",
            "second_bachelor_degree_process": "Follow re-enrollment process for second bachelor's degree"
        }

        self.transfer_credits_info = {
            "transfer_equivalency_self_service": "Use TREQ to enter coursework and view transfer credit evaluation",
            "credit_evaluation_timing": "Credit evaluation available online about eight weeks after acceptance"
        }

        self.transfer_benefits_info = {
            "state_wide_transfer_agreement": "Participate in the State-wide Transfer Agreement for credit transfer",
            "additional_benefits": "Special scholarship funding, financial aid programs for transfer students"
        }

        self.course_equivalency_info = {
            "course_equivalents_database": "Available prior to applying",
            "treq_service": "Use TREQ to enter coursework and AP test scores for degree progress",
            "access_transfer_credits_online": "Access transfer credits online via student account after admission"
        }

        self.contact_info = {
            "associate_director": "Lisa Orr",
            "office": "Enterprise Center, Office of Admissions",
            "phone": "856.256.4208",
            "email": "admissions@rowan.edu"
        }


class RowanUniversityPrograms:
    def __init__(self):
        self.garden_state_guarantee_info = {
            "program_name": "Garden State Guarantee",
            "description": "Financial aid program providing up to four semesters of free tuition and fees for NJ students.",
            "eligibility_criteria": {
                "agi_less_than_65000": "Pay nothing for tuition and fees in junior and senior years.",
                "agi_between_65001_and_80000": "Net cost for tuition and fees is no more than $7,500 total for fall and spring semesters."
            },
            "details_page": "Visit Garden State Guarantee page on Financial Aid website."
        }

        self.returning_students_info = {
            "re_enrollment_process": "For former Rowan students who lost matriculated status or Rowan graduates seeking a second bachelor's degree.",
            "contact_info": {
                "assistant_director": "Assistant Director of University Advising Services",
                "phone": "856-256-4937",
                "email": "delesandro@rowan.edu"
            }
        }

        self.admission_alternative_pathways_info = {
            "1_educational_opportunity": "EOF Program for NJ residents with financial assistance and academic support services.",
            "2_rowan_choice": "Rowan Choice offers a residential college experience at a fraction of the cost.",
            "3_degree_in_three": "Army ROTC program providing leadership training with scholarships covering tuition and fees.",
            "4_rise": "RISE program supports high achieving, diverse students transitioning from high school to college.",
            "5_camden_commuter_experience": "Financial support for Camden County residents through state grants.",
            "6_dual_credit": "High achieving high school students in eleventh or twelfth grades can earn college credits."
        }

        self.contact_info = {
            "enterprise_center": {
                "address": "225 Rowan Blvd., Glassboro, NJ 08028",
                "sms": "(856)-997-2999",
                "calls": "(877)-787-6926",
                "email": "admissions@rowan.edu"
            },
            "admissions_counselor_inclusive_excellence": {
                "sms": "856-431-5005",
                "phone": "(856) 256-4216",
                "email": "jasmarie@admissions.rowan.edu"
            }
        }


class RowanFreshmanRequirements:
    def __init__(self):
        self.application_process = {
            "start_process": "Go to commonapp.org and add Rowan University to your 'My Colleges' list.",
            "complete_common_app": "Complete the Common Application, Rowan University question set, and Recommenders and FERPA section.",
            "invite_recommenders": "Invite recommenders before submitting your application electronically.",
            "submit_all_documents": "Have your school counselor and teachers submit all documents electronically.",
            "submit_application": "Submit your application using your official name on all documents.",
            "portfolio_audition_info": "Review specific requirements for Art, Theatre/Dance, or Music program applicants."
        }

        self.requirements = {
            "common_application": "Freshman/First-Year Common Application (see application calendar and fees)",
            "application_fee": "Application Fee of $65 (see all application deadlines and fees)",
            "activities_list_resume": "Activities List or Resume",
            "official_high_school_transcripts": "Official High School Transcripts",
            "recommendations_teacher_evaluations": "Recommendations/Teacher Evaluations",
            "personal_essay": "Personal Essay",
            "portfolio_audition": "Portfolio or Audition if applying to an Art, Theatre/Dance, or Music Program"
        }

        self.check_status_info = "To check the status of your application, log into your admissions portal or email admissions@rowan.edu."

        self.test_optional_admissions = {
            "overview": "Standardized test scores are not a good indicator for student success. Test Optional admissions are available.",
            "exceptions": "Some students (e.g., applying for the 3+4 BS/MD or BS/DO program) are required to submit test scores.",
            "super_scoring": "Rowan uses Super Scoring to use the best section-level scores across all SAT dates."
        }

        self.highschool_transcript_info = {
            "how_to_submit": "Have your high school send your official high school transcript electronically to the Office of Admissions.",
            "mailing_address": "If necessary, transcripts can be mailed to: Rowan University, Enterprise Center, 225 Rowan Boulevard, Glassboro, NJ 08028",
            "requirements": "Admission to Rowan requires a minimum of 16 college preparatory units in high school."
        }

        self.school_report_counselor_recommendation_info = "The Common Application School Report and Counselor Recommendation provide information about your academic experience within your school environment."

        self.teacher_evaluations_info = {
            "how_to_submit": "Recommendations from teachers can be submitted online through the Common Application platform or by mail using the offline form.",
            "minimum_recommendations": "At least one recommendation from a teacher or school counselor is required."
        }

        self.homeschooled_applicants_info = {
            "requirements": "Submit Rowan University’s application, including the application fee, SAT or ACT scores (unless applying test-optional), and two letters of recommendation.",
            "contact_info": "Contact Undergraduate Admissions at Enterprise Center, 225 Rowan Blvd., Glassboro, NJ 08028. SMS: (856)-997-2999 | Calls: (877)-787-6926 | Email: admissions@rowan.edu"
        }

        self.important_dates = {
            "application_deadline": "01 March 2024 - Application deadline for fall 2024",
            "open_house": "03 March - Open house",
            "fafsa_deadline": "15 April - File your FAFSA Financial Aid",
            "scholarship_deadline": "31 Jan - Scholarship deadline for fall 2024"
        }


# Example usage:
rowan_data = RowanUniversityData()
rowan_programs = RowanUniversityPrograms()
rowan_freshman_requirements = RowanFreshmanRequirements()

# Accessing information:
print(rowan_data.application_info["common_application"]["deadline"])
print(rowan_programs.garden_state_guarantee_info["program_name"])
print(rowan_freshman_requirements.application_process["start_process"])
