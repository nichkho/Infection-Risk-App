var = {
 #Infection Rate
 #Source: https://returntolearn.ucsd.edu/dashboard/index.html
"infection_rate" : 0.0075,
#Viral Load in the Sputum
#Source: https://doi.org/10.1186/s13054-020-02893-8
"cv": 1e9,
#Quanta per RNA copy (Conversion Factor)
#Source: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1539-6924.2010.01427.x
"ci": 0.02,
#Inhalation Rate by Activity
#Source: https://ww2.arb.ca.gov/sites/default/files/classic//research/apr/past/a033-205.pdf
"IR": {"resting": 0.49,
       "standing": 0.54,
       "light_exercise": 1.38,
       "moderate_exercise": 2.35,
       "heavy_exercise": 3.30},
#Droplet Concetrations by activity
#Source: https://doi.org/10.1016/j.jaerosci.2008.11.002
"droplet_conc": {
                "speaking": {".8um": 0.4935,"1.8um": 0.1035, "3.5um": 0.073, "5.5um": 0.035},
                "counting":  
                            {".8um": 0.236, "1.8um": 0.068, "3.5um": 0.007, "5.5um": 0.011},
                "whispering":
                            {".8um": 0.110, "1.8um": 0.014, "3.5um": 0.004, "5.5um": 0.002},
                "singing":
                            {".8um": 0.751, "1.8um": 0.139, "3.5um": 0.139, "5.5um": 0.059},
                "breathing":
                            {".8um": 0.084, "1.8um": 0.009, "3.5um": 0.003, "5.5um": 0.002}},
#Tidal Volume by Droplet Size
#Source: https://doi.org/10.1016/j.jaerosci.2008.11.002
"droplet_vol": {".8um": 0.26808257310632905, "1.8um": 3.053628059289279, "3.5um": 22.44929750377706, "5.5um": 87.11374629016697},
#Mask Efficacy by Droplet Size
#Source: https://doi.org/10.1016/j.ajic.2007.07.008
"mask_efficacy": {".8um": 0.2,"1.8um": 0.4, "3.5um": 0.7, "5.5um": 0.8},
#Deposition Rate of infectious particle
#Source: https://doi.org/10.1016/j.culher.2019.02.017
"deposition_rate" : 0.24,
#Inactivation Rate of Infectious Particle
#Source: https://doi.org/10.1056/nejmc2004973
"viral_inactivation" : 0.63,
#Initial Quanta present is assumed to be 0 by Default
"initial_quanta" : 0
}