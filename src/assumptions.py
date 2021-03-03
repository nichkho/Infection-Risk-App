var = {
"infection_rate" = 0.0075,
"wet_asl_d": 5,
"virus_life": 1.7,
"hi_viral_load": 500000000,
"si_viral_load": 5000000000,
"deposition_prob": 0.5,
"cv": 1e9,
"ci": 0.02,
"mask_efficacy": {".8μm": 0.3,"1.8μm": 0.5, "3.5μm": 0.7, "5.5μm": 0.8},
#Inhalation Rate
"IR": {"resting": 0.49,
       "standing": 0.54,
       "light_exercise": 1.38,
       "moderate_exercise": 2.35,
       "heavy_exercise": 3.30},
"droplet_conc": {
                "speaking": {".8μm": 0.4935,"1.8μm": 0.1035, "3.5μm": 0.073, "5.5μm": 0.035},
                "counting":  
                            {".8μm": 0.236, "1.8μm": 0.068, "3.5μm": 0.007, "5.5μm": 0.011},
                "whispering":
                            {".8μm": 0.110, "1.8μm": 0.014, "3.5μm": 0.004, "5.5μm": 0.002},
                "singing":
                            {".8μm": 0.751, "1.8μm": 0.139, "3.5μm": 0.139, "5.5μm": 0.059},
                "breathing":
                            {".8μm": 0.084, "1.8μm": 0.009, "3.5μm": 0.003, "5.5μm": 0.002}},
    
"droplet_vol": {".8μm": 0.26808257310632905, "1.8μm": 3.053628059289279, "3.5μm": 22.44929750377706, "5.5μm": 87.11374629016697},
"pass_vent_rate" : 0.35,
"deposition_rate" : 0.24,
    
    
"viral_inactivation" : 0.63,
"initial_quanta" : 0,
"viral_load_sptm" : 1000000000,
'ASHRAE_table': {
        'lectureClassroom': {'Rp': 7.5, 'Ra': .06, 'Od': 65},
        'lectureHall': {'Rp': 7.5, 'Ra': .06, 'Od': 150},
        'artClassroom': {'Rp': 10, 'Ra': .18, 'Od': 20},
        'collegeLaboratories': {'Rp': 10, 'Ra': .18, 'Od': 25},
        'woodMetalShop': {'Rp': 10, 'Ra': .18, 'Od': 20},
        'officeSpace': {'Rp': 5, 'Ra': .06, 'Od': 5},
        'libraries' : {'Rp': 5, 'Ra': .12, 'Od': 10},
        'mediaCenter':  {'Rp': 10, 'Ra': .12, 'Od': 25},
        'theatre/Dance': {'Rp': 10, 'Ra': .06, 'Od': 35},
        'multiuseAssembly': {'Rp': 7.5, 'Ra': .06, 'Od': 100},
        'kitchen': {'Rp': 7.5, 'Ra': .12, 'Od': 20},
        'gym': {'Rp': 20, 'Ra': .18, 'Od': 15},
    }
}