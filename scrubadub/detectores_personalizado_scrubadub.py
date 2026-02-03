#%%
# correr en terminal de repo
#pip install scrubadub
#pip install scrubadub_spacy
#pip install spacy_transformers
# %%
from pydoc import text
import pandas as pd
import re
import scrubadub
from scrubadub.filth import Filth
from scrubadub.detectors import Detector
import pandas as pd

#%%
# CREA  DNI TELEFONO CUIL MAIL
# -------------------------------

# DNI

class DniFilth(Filth):
    type = 'dni'

class DniDetector(Detector):
    name = 'dni'
    def iter_filth(self, text, document_name=None):
        dni_pattern = r'(?<!\d)(?<!-)\b\d{7,8}\b(?!\d)(?!-)'
        # dejaria que lo haga para cualquier numero largo que venga sepues de dni doc lu pas
        for match in re.finditer(dni_pattern, text):
            yield DniFilth(
                beg=match.start(),
                end=match.end(),
                text=match.group(),
                document_name=document_name,
                detector_name=self.name
            )



# TELEFONO

class TelFilth(Filth):
    type = 'telefono'

# Detector para teléfono
class TelDetector(Detector):
    name = 'tel'
    def iter_filth(self, text, document_name=None):
        tel_pattern = r'\b(?:(?:1[15]-?(?:\d{4}-?\d{4}))|(?:[234]\d-?(?:\d{3}-?\d{4}|\d{8}))|(?:\d{2}-?\d{8})|(?:\d{3}-?\d{7})|(?:\d{4}-?\d{6}))\b'
# agregaria un lookbehind de "tel", "cel" 
        for match in re.finditer(tel_pattern, text):
            yield TelFilth(
                beg=match.start(),
                end=match.end(),
                text=match.group(),
                document_name=document_name,
                detector_name=self.name
            )


# CUIL

class CuilFilth(Filth):
    type = 'CUIL'

class CuilDetector(Detector):
    name = 'cuil'
    def iter_filth(self, text, document_name=None):
        cuil_pattern = r'\b(20|25|27)(\d{8}|\-\d{7,8}\-\d)\b'
        for match in re.finditer(cuil_pattern, text):
            yield CuilFilth(
                beg=match.start(),
                end=match.end(),
                text=match.group(),
                document_name=document_name,
                detector_name=self.name
            )


#  MAIL
class MailFilth(Filth):
    type = 'MAIL'

class MailDetector(Detector):
    name = 'mail'
    def iter_filth(self, text, document_name=None):
        
        mail_pattern=r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com\b'
        for match in re.finditer(mail_pattern, text):
            yield MailFilth(
                beg=match.start(),
                end=match.end(),
                text=match.group(),
                document_name=document_name,
                detector_name=self.name
            )


#  Numero sensible generico (by Lui)

class NumerosFilth(Filth):
    type = 'MAIL'

class NumerosDetector(Detector):
    name = 'numeros sensibles'
    def iter_filth(self, text, document_name=None):
        
        numeros_sensibles_pattern=r'(?<!\d)(?<!-)\b(\d{7,8}|\d{1,2}(?:\.\d{3}){2}|(?:\+?54\s?)?9?\s?\d{2,4}[-.\s]?\d{6,8})\b(?!-)(?!\d)'
        for match in re.finditer(numeros_sensibles_pattern, text):
            yield NumerosFilth(
                beg=match.start(),
                end=match.end(),
                text=match.group(),
                document_name=document_name,
                detector_name=self.name)