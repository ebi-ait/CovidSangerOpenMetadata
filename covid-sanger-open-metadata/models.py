from enum import Enum


class Donor:
    def __init__(self, accession, sample_type, lab_number, sanger_id, pool_target,  ega_sample_accession,
                 patient_id, covid_pcr_performed, covid_test_result, covid_interval, admission_reason,
                 vasoactive_reagents, covid_who_classification, symptoms,
                 developmental_stage, vital_status, taxon_id, smoking_status, smoking_pack_years, age, bmi, sex,
                 hiv, cd4_t_cell_count, hiv_viral_load, immunocompromised_status, organ_transplant,
                 organ_transplant_type, bone_marrow_transplant, automimmune_disease):
        self.accession = accession
        self.patient_id = patient_id
        self.covid_pcr_performed = covid_pcr_performed
        self.covid_test_result = covid_test_result
        self.covid_interval
        self.developmental_stage = developmental_stage
        self.vital_status = vital_status
        self.taxon_id = taxon_id
        self.sample_type = sample_type
        self.sanger_id = sanger_id
        self.pool_target = pool_target
        self.sex = sex
        self.age = age
        self.bmi = bmi
        self.ega_sample_accession = ega_sample_accession
        self.lab_number = lab_number

    def __str__(self):
        return str(vars(self))


class Sample:
    def __init__(self, accession, supplier_sample_id, sanger_sample_id, input_patient_id, taxon_id,
                 input_accession=None,
                 sample_type=None, input_dict=None):
        self.accession = accession
        self.supplier_sample_id = supplier_sample_id
        self.sanger_sample_id = sanger_sample_id
        self.input_accession = input_accession
        self.input_patient_id = input_patient_id
        self.sample_type = sample_type
        self.taxon_id = taxon_id
        self.ega_sample_accession
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


class ValidValues:
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
                                       "intubated/ventilated": "http://purl.obolibrary.org/obo/HP_0004887",
                                       "non-invasive/ventilation": "http://purl.obolibrary.org/obo/MAXO_0000506",
                                       "hospitalised/O2": "http://purl.obolibrary.org/obo/MAXO_0000066",
                                       "hospitalised/No O2": None,
                                       "not hospitalised": None}

        self.yes_no = ["Yes", "No", "not known"]

        self.smoking_status = {"Non-smoker": "http://purl.obolibrary.org/obo/NCIT_C65108",
                               "Smoker": "http://purl.obolibrary.org/obo/NCIT_C67150"}




