#%%
!pip install scrubadub 
import re
import scrubadub
from scrubadub.filth import Filth
from scrubadub.detectors import Detector
import pandas as pd

#%% Cargar datos de ejemplo
with open(r"C:\Users\luisa\OneDrive\Documentos\RepositorioVS_Github\probando_anonimizadores\testtxt.txt", "r", encoding="utf-8") as f:
    texto = f.read()    
texto
#%%

# tiene DNI TELEFONO CUIL MAIL
# NO tiene nombres ni direcciones

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
#%%

# -------------------------------
# Crear Scrubber limpio, sin detectores por defecto
scrubber = scrubadub.Scrubber(detector_list=[])

# Agregar solo tus detectores personalizados
scrubber.add_detector(DniDetector())
scrubber.add_detector(TelDetector())
scrubber.add_detector(CuilDetector())
scrubber.add_detector(MailDetector())

# -------------------------------
# Probar sobre un texto
#texto = "El paciente con DNI 20333444 llamó desde el número 11-45678901 mi_mail@mail.com"


resultado = scrubber.clean(texto)

print(resultado)

#%%
'''
#df["evolucion"] = df["evolucion"].fillna("").astype(str)
df["evolucion_limpia"] = df["evolucion"].apply(scrubber.clean)

#%%
#df["diferencia"] = df[ 'evolucion'] != df["evolucion_limpia"]

df_cambiado = df[df['diferencia']==True]
#%%
#df.to_excel('prueba_scrubadub.xlsx', index=False)  # index=False evita que se guarde el índice
#df_cambiado.to_excel('cambios_scrubadub.xlsx', index=False)  # index=False evita que se guarde el índice
'''
