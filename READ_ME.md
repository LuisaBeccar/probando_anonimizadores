En este repositorio voy a probar distintos modelos y metodos de anonimizacion con los que me fui encontrando en la web.<br>
Dejo debajo de cada uno comentarios tras el intento de usarlos

1) tanaos.ipynb
    - https://docs.tanaos.com/artifex/text-anonymization/inference/
    - https://huggingface.co/tanaos/tanaos-text-anonymizer-v1

    - el numero de tipo sale raro
    - no pude hacer el finetune a español. mandé mail.
    + tiene para enmascarar personas, telefonos, direcciones, lugares, fechas; y a eleccion podes sacar que no enmascare fechas por ejemplo. 

2) anonimizador.py
    - basado en scrubadub, script por equipo CDD GOGIES
    + tiene para DNI, CUIL, MAIL, TELEFONO
    - falta nombres

