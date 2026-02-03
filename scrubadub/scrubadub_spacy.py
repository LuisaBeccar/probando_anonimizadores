#%%
#pip install scrubadub
#pip install scrubadub_spacy
#pip install spacy_transformers
#%%
import pandas as pd
import spacy_transformers
import scrubadub, scrubadub_spacy
from detectores_personalizado_scrubadub import DniDetector, CuilDetector, TelDetector, MailDetector, NumerosDetector

#%% 
### Se inicializa el scrubber con la localización del país para que reconozca características específicas, como números de teléfono. 
scrubber = scrubadub.Scrubber(locale="es_AR") 
### Se agrega el detector elegido 
scrubber.add_detector(scrubadub_spacy. detectors.SpacyEntityDetector(model = "es_core_news_md")) 
# Agregar el detectores personalizados
#scrubber.add_detector(DniDetector())
#scrubber.add_detector(CuilDetector())
#scrubber.add_detector(TelDetector())    
scrubber.add_detector(NumerosDetector())
scrubber.add_detector(MailDetector())

def clean_text(text):
    return scrubber.clean(text)
    
#%%
text = "Mi nombre es Louisa Parker, vivo en la la  123 Park Avenue NY. mi DNI es 12345122 y mi celular 1555543345."
#%%
scrubber.clean(text)
