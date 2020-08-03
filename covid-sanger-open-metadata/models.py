from .exceptions import InvalidInputError


class Donor:

    def __init__(self, accession,
                 sample_type=None, lab_number=None, sanger_id=None, pool_target=None, ega_sample_accession=None,
                 patient_id=None, covid_pcr_performed=None, covid_test_result=None, covid_interval=None,
                 admission_reason=None,
                 vasoactive_reagents=None, covid_who_classification=None, symptoms=None,
                 developmental_stage=None, vital_status=None, taxon_id=9606, smoking_status=None,
                 smoking_pack_years=None, age=None, bmi=None, sex=None,
                 ethnicity=None,
                 com_hiv=None, com_cd4_count=None, com_hiv_load=None, com_immunocomp=None, com_immunocomp_time=None,
                 com_transplant=None, com_bm_transplant=None, com_transplant_type=None,
                 com_autoimm_rheum=None, com_type_i_diabetes=None,
                 com_type_ii_diabetes=None, com_asthma=None, com_chronic_pulm=None, com_cystic_fibrosis=None,
                 com_sleep_apnea=None, com_sleep_cpap=None,
                 com_liver=None, com_gallbl=None, com_pancreas=None, com_chronic_kidney=None,
                 com_angio=None, com_bypass=None, com_heart_failure=None,
                 com_hypertension=None, com_infarction_type1=None, com_infarction_type2=None, com_vascular=None,
                 com_stroke=None, com_arrythmias=None,
                 com_dementia=None, com_neurological=None, com_leukemia=None, com_lymphoma=None,
                 com_malignant_solid=None
                 ):

        field_validator = ValidatorCurator()

        # Patient identification
        self.accession = accession
        self.patient_id = "" if patient_id is None else patient_id
        self.taxon_id = "" if taxon_id is None else taxon_id
        self.sample_type = "" if sample_type is None else sample_type
        self.sanger_id = "" if sanger_id is None else sanger_id
        self.pool_target = "" if pool_target is None else pool_target
        self.ega_sample_accession = "" if ega_sample_accession is None else ega_sample_accession
        self.lab_number = "" if lab_number is None else lab_number

        # Demographics
        self.ethnicity = field_validator.validate_against_dict(ethnicity,
                                                               field_validator.ethnicity)
        self.covid_pcr_performed = field_validator.validate_against_list(covid_pcr_performed,
                                                                         field_validator.yes_no)
        self.covid_test_result = covid_test_result
        self.covid_interval = covid_interval
        self.admission_reason = field_validator.validate_against_dict(admission_reason,
                                                                      field_validator.reasons)
        self.developmental_stage = developmental_stage
        self.vital_status = vital_status
        self.sex = field_validator.validate_against_list(sex, field_validator.sex)
        self.age = age
        self.bmi = bmi

        self.symptoms = field_validator.validate_against_dict(symptoms,
                                                              field_validator.symptoms)
        self.covid_who_classification = field_validator.validate_against_dict(covid_who_classification,
                                                                              field_validator.disease_classification)
        self.vasoactive_reagents = field_validator.validate_against_list(vasoactive_reagents,
                                                                         field_validator.yes_no)
        # Risk factors
        self.smoking_status = field_validator.validate_against_dict(smoking_status,
                                                                    field_validator.smoking_status)
        self.smoking_pack_years = smoking_pack_years

        # Co-morbidities
        self.com_hiv = field_validator.validate_against_list(com_hiv, field_validator.yes_no)
        self.com_cd4_count = com_cd4_count
        self.com_hiv_load = com_hiv_load
        self.com_immunocomp = field_validator.validate_against_list(com_immunocomp, field_validator.yes_no)
        self.com_immunocomp_time = field_validator.validate_against_list(com_immunocomp_time, field_validator.yes_no)
        self.com_transplant = field_validator.validate_against_list(com_transplant, field_validator.yes_no)
        self.com_bm_transplant = field_validator.validate_against_list(com_bm_transplant, field_validator.yes_no)
        self.com_transplant_type = com_transplant_type
        self.com_autoimm_rheum = field_validator.validate_against_list(com_autoimm_rheum, field_validator.yes_no)
        self.com_type_i_diabetes = field_validator.validate_against_list(com_type_i_diabetes, field_validator.yes_no)
        self.com_type_ii_diabetes = field_validator.validate_against_list(com_type_ii_diabetes, field_validator.yes_no)
        self.com_asthma = field_validator.validate_against_list(com_asthma, field_validator.yes_no)
        self.com_chronic_pulm = field_validator.validate_against_list(com_chronic_pulm, field_validator.yes_no)
        self.com_cystic_fibrosis = field_validator.validate_against_list(com_cystic_fibrosis, field_validator.yes_no)
        self.com_sleep_apnea = field_validator.validate_against_list(com_sleep_apnea, field_validator.yes_no)
        self.com_sleep_cpap = field_validator.validate_against_list(com_sleep_cpap, field_validator.yes_no)
        self.com_liver = field_validator.validate_against_list(com_liver, field_validator.yes_no)
        self.com_gallbl = field_validator.validate_against_list(com_gallbl, field_validator.yes_no)
        self.com_pancreas = field_validator.validate_against_list(com_pancreas, field_validator.yes_no)
        self.com_chronic_kidney = field_validator.validate_against_list(com_chronic_kidney, field_validator.yes_no)
        self.com_angio = field_validator.validate_against_list(com_angio, field_validator.yes_no)
        self.com_bypass = field_validator.validate_against_list(com_bypass, field_validator.yes_no)
        self.com_heart_failure = field_validator.validate_against_list(com_heart_failure, field_validator.yes_no)
        self.com_hypertension = field_validator.validate_against_list(com_hypertension, field_validator.yes_no)
        self.com_infarction_type1 = field_validator.validate_against_list(com_infarction_type1, field_validator.yes_no)
        self.com_infarction_type2 = field_validator.validate_against_list(com_infarction_type2, field_validator.yes_no)
        self.com_vascular = field_validator.validate_against_list(com_vascular, field_validator.yes_no)
        self.com_stroke = field_validator.validate_against_list(com_stroke, field_validator.yes_no)
        self.com_arrythmias = field_validator.validate_against_list(com_arrythmias, field_validator.yes_no)
        self.com_dementia = field_validator.validate_against_list(com_dementia, field_validator.yes_no)
        self.com_neurological = field_validator.validate_against_list(com_neurological, field_validator.yes_no)
        self.com_leukemia = field_validator.validate_against_list(com_leukemia, field_validator.yes_no)
        self.com_lymphoma = field_validator.validate_against_list(com_lymphoma, field_validator.yes_no)
        self.com_malignant_solid = field_validator.validate_against_list(com_malignant_solid, field_validator.yes_no)

    def __str__(self):
        return str(vars(self))


class Sample:
    def __init__(self, accession, supplier_sample_id, sanger_sample_id, input_patient_id, taxon_id,
                 ega_sample_accession, input_accession=None, sample_type=None, input_dict=None):
        self.accession = accession
        self.supplier_sample_id = supplier_sample_id
        self.sanger_sample_id = sanger_sample_id
        self.input_accession = input_accession
        self.input_patient_id = input_patient_id
        self.sample_type = sample_type
        self.taxon_id = taxon_id
        self.ega_sample_accession = ega_sample_accession
        self._get_input_accession(input_dict)

    def __str__(self):
        return str(vars(self))

    def _get_input_accession(self, input_dict):
        try:
            self.input_accession = input_dict[self.input_patient_id].accession
        except KeyError as err:
            print("Patient id " + str(err) + " not found in input dict.")
        except TypeError as err:
            print(err)
            print("Valid input dictionary not specified.")

    def _get_sample_type(self, input_dict):
        try:
            self.sample_type = input_dict[self.input_patient_id].sample_type
        except KeyError as err:
            print("Patient id " + str(err) + " not found in input dict.")
        except TypeError as err:
            print(err)
            print("Valid input dictionary not specified.")


class ValidatorCurator:
    def __init__(self):
        self.reasons = {"cough": "http://purl.obolibrary.org/obo/HP_0012735",
                        "fever": "http://purl.obolibrary.org/obo/HP_0001945",
                        "difficulty breathing": "http://purl.obolibrary.org/obo/HP_0002094",
                        "fatigue": "http://purl.obolibrary.org/obo/HP_0012378",
                        "myalgia": "http://purl.obolibrary.org/obo/HP_0003326",
                        "sore throat": "http://purl.obolibrary.org/obo/HP_0025439",
                        "loss of smell": "http://purl.obolibrary.org/obo/HP_0000458",
                        "diarrhea": "http://purl.obolibrary.org/obo/HP_0002014",
                        "nausea": "http://purl.obolibrary.org/obo/HP_0002018",
                        "runny nose": "http://purl.obolibrary.org/obo/HP_0031417",
                        "other": None}

        self.symptoms = {"fever": "http://purl.obolibrary.org/obo/HP_0001945",
                         "cough": "http://purl.obolibrary.org/obo/HP_0012735",
                         "respiratory failure": "http://purl.obolibrary.org/obo/HP_0002878",
                         "rhinorrhea": "http://purl.obolibrary.org/obo/HP_0031417",
                         "fatigue": "http://purl.obolibrary.org/obo/HP_0012378",
                         "digestive symptoms": "http://purl.obolibrary.org/obo/SYMP_0000459",
                         "asymptomatic": "http://purl.obolibrary.org/obo/NCIT_C3833"}

        self.sex = ["Female", "Male", "Intersex", "Prefer not to answer"]

        self.ethnicity = {"White": "http://purl.obolibrary.org/obo/HANCESTRO_0005",
                          "Black": "http://purl.obolibrary.org/obo/HANCESTRO_0005",
                          "Hispanic": "http://purl.obolibrary.org/obo/HANCESTRO_0014",
                          "East Asian/Pacific Islander": "http://purl.obolibrary.org/obo/HANCESTRO_0009||http://purl.obolibrary.org/obo/HANCESTRO_0574",
                          "South Asian": "http://purl.obolibrary.org/obo/HANCESTRO_0006",
                          "Middle Eastern or Central Asian": "http://purl.obolibrary.org/obo/HANCESTRO_0015||http://purl.obolibrary.org/obo/HANCESTRO_0286",
                          "More than one race": None,
                          "American Indian or Alaska Native": "http://purl.obolibrary.org/obo/HANCESTRO_0013",
                          "Native Hawaiian or Other Pacific Islander": "http://purl.obolibrary.org/obo/HANCESTRO_0573||http://purl.obolibrary.org/obo/HANCESTRO_0574",
                          "Don't Know": None,
                          "Prefer not to answer": None}

        self.disease_classification = {"Death": "http://purl.obolibrary.org/obo/UBERON_0000071",
                                       "Intubated/Ventilated": "http://purl.obolibrary.org/obo/HP_0004887",
                                       "Non-invasive/Ventilation": "http://purl.obolibrary.org/obo/MAXO_0000506",
                                       "Hospitalised/O2": "http://purl.obolibrary.org/obo/MAXO_0000066",
                                       "Hospitalised/No O2": None,
                                       "Not Hospitalised": None}

        self.yes_no = ["Yes", "No", "unknown"]

        self.smoking_status = {"Non-smoker": "http://purl.obolibrary.org/obo/NCIT_C65108",
                               "Smoker": "http://purl.obolibrary.org/obo/NCIT_C67150"}

        self.comorbidities = {"com_hiv": "http://purl.obolibrary.org/obo/MONDO_0005109",
                              "com_immunocomp": "http://purl.obolibrary.org/obo/NCIT_C14139",
                              "com_transplant": "http://purl.obolibrary.org/obo/NCIT_C130200",
                              "com_bm_transplant": "http://purl.obolibrary.org/obo/NCIT_C131759",
                              "com_autoimm_rheum": "http://purl.obolibrary.org/obo/MONDO_0007179",
                              "com_type_i_diabetes": "http://purl.obolibrary.org/obo/MONDO_0005147",
                              "com_type_ii_diabetes": "http://purl.obolibrary.org/obo/MONDO_0005148",
                              "com_asthma": "http://purl.obolibrary.org/obo/MONDO_0004979",
                              "com_chronic_pulm": "http://purl.obolibrary.org/obo/MONDO_0005002",
                              "com_cystic_fibrosis": "http://purl.obolibrary.org/obo/MONDO_0009061",
                              "com_sleep_apnea": "http://purl.obolibrary.org/obo/MONDO_0005296",
                              "com_liver": "http://purl.obolibrary.org/obo/MONDO_0005154",
                              "com_gallbl": "http://purl.obolibrary.org/obo/MONDO_0005281",
                              "com_pancreas": "http://purl.obolibrary.org/obo/MONDO_0002356",
                              "com_chronic_kidney": "http://purl.obolibrary.org/obo/MONDO_0005300",
                              "com_angio": "http://www.ebi.ac.uk/efo/EFO_0003951",
                              "com_bypass": "http://www.ebi.ac.uk/efo/EFO_0003776",
                              "com_heart_failure": "http://purl.obolibrary.org/obo/MONDO_0005009",
                              "com_hypertension": "http://www.ebi.ac.uk/efo/EFO_0000537",
                              "com_infarction_type1": "http://purl.obolibrary.org/obo/MONDO_0005068",
                              "com_infarction_type2": "http://purl.obolibrary.org/obo/MONDO_0005068",
                              "com_vascular": "http://purl.obolibrary.org/obo/MONDO_0005294",
                              "com_stroke": "http://purl.obolibrary.org/obo/MONDO_0005098",
                              "com_arrythmias": "http://www.ebi.ac.uk/efo/EFO_0004269",
                              "com_dementia": "http://purl.obolibrary.org/obo/MONDO_0001627",
                              "com_neurological": "http://purl.obolibrary.org/obo/MONDO_0005071",
                              "com_leukemia": "http://purl.obolibrary.org/obo/MONDO_0005059",
                              "com_lymphoma": "http://purl.obolibrary.org/obo/MONDO_0005062",
                              "com_malignant_solid": "http://purl.obolibrary.org/obo/NCIT_C132146"}

    def validate_against_list(self, provided_text, valid_list):
        if provided_text in valid_list:
            return provided_text
        else:
            raise InvalidInputError("Provided text '" + provided_text + "' not in allowed values: " + str(valid_list))

    def validate_against_dict(self, provided_text, valid_dict):
        if provided_text in valid_dict.keys():
            return provided_text
        else:
            raise InvalidInputError("Provided text '" + provided_text + "' not in allowed values: " +
                                    str(valid_dict.keys()))

    def annotate_ontology(self, field_value, field_dict_name):
        field_dict = vars(self)[field_dict_name]
        return field_dict[field_value]

    def annotate_ethnicity(self, field_value):
        try:
            return self.ethnicity[field_value]
        except KeyError:
            print("Field not found in provided dictionary")
