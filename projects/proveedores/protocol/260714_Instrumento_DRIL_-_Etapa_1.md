## Agent version: V260714 - Identificación de iniciativas públicas para la generación y consolidación de relaciones de proveeduría

### 1. Propósito del instrumento

Este instrumento corresponde a la primera etapa de aplicación de la metodología DRIL para construir una base de datos de iniciativas públicas orientadas a crear, promover, apoyar o consolidar relaciones de proveeduría entre grandes empresas, empresas ancla o empresas tractoras, y mipymes, pymes, proveedores locales o empresas proveedoras.

El objetivo de esta etapa no es caracterizar en profundidad las iniciativas, sino identificar iniciativas candidatas que cumplan con la definición operacional del estudio y documentar la evidencia mínima que justifica su inclusión. La caracterización detallada de los programas se realizará en una segunda etapa, una vez que las iniciativas candidatas hayan sido revisadas y validadas humanamente.

### 2. Rol del agente de implementación

El agente de implementación debe aplicar este instrumento de manera independiente a cada entidad pública incluida en el mapped unit space. Para cada entidad, deberá realizar búsqueda web, revisar fuentes relevantes, evaluar si existen iniciativas elegibles, aplicar las reglas de inclusión y exclusión, y producir una o más filas estructuradas de salida.

El agente no debe modificar la definición de iniciativa elegible, añadir variables nuevas, reinterpretar las reglas de codificación ni reducir el universo de unidades. Cuando la evidencia sea insuficiente, ambigua o contradictoria, debe registrar el estado correspondiente y documentar la razón, en lugar de inferir o completar información sin respaldo.

## 3. Definición operacional de iniciativa elegible

Se considera iniciativa elegible todo programa, convocatoria, línea de apoyo, proyecto, instrumento, estrategia pública o mecanismo institucional ofrecido, ejecutado, financiado, promovido o coordinado por una entidad pública nacional o subnacional, cuyo objetivo sea crear, promover, apoyar, fortalecer o consolidar relaciones de proveeduría entre:

- una empresa cliente, gran empresa, empresa ancla, empresa tractora, cadena productiva o sector demandante; y
- mipymes, pymes, proveedores locales, pequeños negocios o empresas proveedoras.

La iniciativa puede estar dirigida a los proveedores, a las empresas ancla o a ambos actores, siempre que el vínculo de proveeduría o encadenamiento entre ellos sea un componente explícito de la intervención.

### 4. Criterios de inclusión

Debe codificarse una iniciativa como elegible cuando la evidencia disponible muestre al menos una de las siguientes condiciones:

1. La iniciativa busca desarrollar, fortalecer o consolidar proveedores para grandes empresas, empresas ancla o empresas tractoras.
2. La iniciativa busca integrar mipymes, pymes o proveedores locales a cadenas de valor, cadenas de suministro, compras de grandes empresas o mercados liderados por empresas demandantes.
3. La iniciativa ofrece asistencia técnica, capacitación, acompañamiento, certificación, financiamiento, formalización o mejora de capacidades productivas con el propósito explícito de que las empresas proveedoras cumplan requisitos, estándares o condiciones de compra de empresas ancla o cadenas productivas.
4. La iniciativa busca reducir barreras administrativas, comerciales, financieras o técnicas que impiden a mipymes o proveedores locales vender a grandes empresas, empresas ancla, entidades tractoras o cadenas de valor.
5. La iniciativa promueve mecanismos de articulación, matchmaking, ruedas de negocio, acuerdos comerciales o vinculación estratégica entre empresas demandantes y empresas proveedoras.
6. La iniciativa tiene una formulación sectorial, territorial o productiva específica, pero incluye explícitamente un componente de encadenamiento, proveeduría, desarrollo de proveedores o articulación entre empresas de distinto tamaño dentro de una cadena de valor.

### 5. Criterios de exclusión

No debe codificarse una iniciativa como elegible cuando:

1. Es un programa general de apoyo a mipymes, emprendimiento, innovación, productividad, digitalización o financiamiento, pero no existe evidencia de que busque articularlas con empresas ancla o grandes empresas.
2. Es una política de compras públicas, proveedor del Estado o mercado público, salvo que el programa tenga un componente explícito de vinculación entre mipymes/proveedores locales y grandes empresas o empresas ancla privadas o mixtas.
3. Es una iniciativa de clúster, competitividad regional o desarrollo productivo sin evidencia explícita de relaciones de proveeduría, desarrollo de proveedores o encadenamiento entre empresas ancla y proveedores.
4. Es solo una noticia, evento, feria o rueda de negocios aislada, sin evidencia de que forme parte de un programa, instrumento, convocatoria o línea de acción pública.
5. La entidad participa marginalmente como invitada, patrocinadora o asistente en una actividad, pero no ofrece, ejecuta, financia, coordina ni promueve la iniciativa.
6. La iniciativa corresponde exclusivamente a capacitación laboral, empleabilidad, formación de trabajadores o intermediación laboral, sin componente de relación entre empresas ancla y proveedores.

### 6. Mapped unit space

El mapped unit space está compuesto por una lista de entidades públicas nacionales y subnacionales. Cada unidad de investigación inicial corresponde a una entidad pública.

Cada entidad del mapped unit space debe contener, como mínimo, los siguientes campos de entrada:

| Variable de entrada | Descripción                                                |
| ------------------- | ---------------------------------------------------------- |
| entity_id           | Identificador único de la entidad en el mapped unit space. |
| entidad_input       | Nombre original de la entidad pública.                     |
| pais                | País de la entidad.                                        |
| entidad_nivel       | Nivel de la entidad: nacional o subnacional.               |
| tipo_entidad        | Tipo de entidad pública.                                   |

La unidad inicial de aplicación del instrumento es la entidad pública. Sin embargo, la unidad de salida de la base de datos será el programa candidato. Por lo tanto, una misma entidad puede generar cero, una o múltiples filas en la base final de esta etapa.

### 7. Reglas para entidades con múltiples programas

Es posible que una misma entidad pública cuente con más de una iniciativa elegible. El agente debe buscar y registrar todas las iniciativas elegibles encontradas para cada entidad, dentro de límites razonables de búsqueda.

La variable n_programas_candidatos debe registrar la cantidad total de iniciativas elegibles identificadas para esa entidad.

La estructura de salida debe seguir estas reglas:

- Si no se encuentra ninguna iniciativa elegible, se debe generar una fila para la entidad, con existe_programa_proveeduria = 0, n_programas_candidatos = 0 y los campos de programa en blanco o marcados como no aplicables.
- Si se encuentra una iniciativa elegible, se debe generar una fila, con existe_programa_proveeduria = 1 y n_programas_candidatos = 1.
- Si se encuentran dos o más iniciativas elegibles, se debe generar una fila por cada programa identificado. En todas esas filas debe repetirse el mismo valor de entity_id, entidad_input, pais, entidad_nivel, existe_programa_proveeduria = 1 y n_programas_candidatos, indicando el total de programas candidatos encontrados para esa entidad.
- Cada programa candidato debe tener su propio programa_candidato_id, nombre_candidato, razon_inclusion y campos de evidencia.
- No deben combinarse programas distintos en una misma fila.
- No deben duplicarse convocatorias específicas si corresponden al mismo programa madre, salvo que la convocatoria tenga nombre, alcance o entidad ejecutora diferenciada y sea relevante registrarla como iniciativa propia.

#### 7.1. Ejemplo de estructura para múltiples programas

Si la entidad E001 tiene tres programas elegibles, la salida debe ser:

| entity_id | entidad_input | existe_programa_proveeduria | n_programas_candidatos | programa_candidato_id | nombre_candidato |
| --------- | ------------- | --------------------------- | ---------------------- | --------------------- | ---------------- |
| E001      | Entidad A     | 1                           | 3                      | E001_P01              | Programa 1       |
| E001      | Entidad A     | 1                           | 3                      | E001_P02              | Programa 2       |
| E001      | Entidad A     | 1                           | 3                      | E001_P03              | Programa 3       |

Si la entidad E002 no tiene programas elegibles, la salida debe ser:

| entity_id | entidad_input | existe_programa_proveeduria | n_programas_candidatos | programa_candidato_id | nombre_candidato |
| --------- | ------------- | --------------------------- | ---------------------- | --------------------- | ---------------- |
| E002      | Entidad B     | 0                           | 0                      | NA                    | NA               |

### 8. Reglas para distinguir programa madre, convocatoria y actividad

Cuando la fuente identifique una convocatoria específica dentro de un programa más amplio, el agente debe seguir estas reglas:

1. Si la convocatoria es solo una edición territorial, anual o sectorial de un programa madre claramente identificado, registrar como nombre_candidato el nombre del programa madre y mencionar la convocatoria específica en observaciones.
2. Si la convocatoria tiene nombre propio, objetivos específicos y evidencia suficiente para ser tratada como iniciativa diferenciada, puede registrarse como programa candidato independiente.
3. Si solo se encuentra una noticia sobre una actividad puntual, sin indicios de continuidad, bases, convocatoria, programa, línea de apoyo o instrumento institucional, no debe registrarse como programa candidato. Puede mencionarse en notas_busqueda si ayudó a orientar la búsqueda.
4. Si existen dudas razonables sobre si dos registros corresponden al mismo programa o a iniciativas distintas, deben registrarse por separado y marcarse con status = "needs_human_review".

### 9. Codebook de variables de salida

| Variable                    | Tipo        | Pregunta                                                                                   | Reglas de codificación                                                                                                                                                                                                                                                         |
| --------------------------- | ----------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| entity_id                   | texto / ID  | ¿Cuál es el identificador único de la entidad en el mapped unit space?                     | Copiar desde la base de entrada. No modificar.                                                                                                                                                                                                                                 |
| entidad_input               | texto       | ¿Cuál es el nombre original de la entidad?                                                 | Copiar desde la base de entrada. No traducir ni normalizar.                                                                                                                                                                                                                    |
| pais                        | texto       | ¿Cuál es el país de la entidad?                                                            | Copiar desde la base de entrada.                                                                                                                                                                                                                                               |
| entidad_nivel               | categórica  | ¿Cuál es el nivel de la entidad?                                                           | Copiar desde la base de entrada.                                                                                                                                                                                                                                               |
| tipo_entidad                | categórica  | ¿Qué tipo de institución pública es la entidad?                                            | Copiar desde la base de entrada.                                                                                                                                                                                                                                               |
| existe_programa_proveeduria | binaria     | ¿Cuenta esta entidad con al menos un programa candidato de proveeduría estratégica?        | 1 = Sí, se encontró al menos una iniciativa elegible; 0 = No se encontró evidencia suficiente de iniciativas elegibles.                                                                                                                                                        |
| n_programas_candidatos      | entero      | ¿Cuántas iniciativas elegibles se encontraron para esta entidad?                           | Registrar el total de programas candidatos identificados para la entidad. Si no se encuentra ninguno, registrar 0. Si hay múltiples filas para una entidad, repetir el mismo total en cada fila.                                                                               |
| programa_candidato_id       | texto / ID  | ¿Cuál es el identificador del programa candidato dentro de la entidad?                     | Crear un ID compuesto: entity_id + número correlativo de programa, por ejemplo E001_P01, E001_P02. Si no hay programa, usar NA.                                                                                                                                                |
| nombre_candidato            | texto       | ¿Cuál es el nombre completo del programa, convocatoria, línea o iniciativa candidata?      | Registrar el nombre oficial más completo disponible. Si hay sigla y nombre completo, incluir ambos. Si no hay programa, dejar en blanco.                                                                                                                                       |
| razon_inclusion             | texto breve | ¿Por qué esta iniciativa parece cumplir la definición operacional del estudio?             | Explicar en 1–3 frases la relación entre la iniciativa y la generación, fortalecimiento o consolidación de relaciones de proveeduría entre empresas ancla/grandes empresas y mipymes/proveedores locales. No caracterizar dimensiones que serán recogidas en la segunda etapa. |
| evidencia_excerpt           | texto       | ¿Qué fragmento textual respalda la existencia e inclusión del programa?                    | Copiar una cita textual breve y suficiente desde la fuente. Debe respaldar su vínculo con proveeduría, encadenamiento, empresas ancla o proveedores locales.                                                                                                                   |
| evidencia_url               | URL         | ¿Cuál es la URL de la fuente consultada?                                                   | Registrar URL funcional. Si la fuente es un documento descargado, registrar URL de descarga o página de origen.                                                                                                                                                                |
| evidencia_fecha_acceso      | fecha       | ¿Cuándo fue consultada la fuente?                                                          | Registrar fecha de acceso en formato YYYY-MM-DD.                                                                                                                                                                                                                               |
| evidencia_locator           | texto       | ¿Dónde se ubica exactamente la evidencia dentro de la fuente?                              | Registrar sección, título, subtítulo, párrafo, página, tabla, artículo, numeral o cualquier localizador preciso.                                                                                                                                                               |
| source_title                | texto       | ¿Cuál es el título de la fuente?                                                           | Registrar título de la página, documento, noticia, convocatoria, bases o informe.                                                                                                                                                                                              |
| source_role                 | categórica  | ¿Qué tipo de fuente respalda la codificación?                                              | Usar: official_entity_page, official_program_page, official_call_document, official_report, public_partner_source, multilateral_source, press_or_secondary_source, other.                                                                                                      |
| source_institution          | texto       | ¿Qué institución publica la fuente?                                                        | Registrar institución responsable de la página o documento.                                                                                                                                                                                                                    |
| status                      | categórica  | ¿Cuál es el estado de codificación del registro?                                           | Usar: answered, not_found_after_search,  needs_human_review.                                                                                                                                                                                                                   |
| gap_reason                  | categórica  | Si no se encontró un programa elegible, ¿cuál es la razón principal?                       | Usar solo cuando existe_programa_proveeduria = 0. Valores: no_relevant_source_found, insufficient_evidence, out_of_scope, other.                                                                                                                                               |
| notas_busqueda              | texto       | ¿Qué limitaciones de la información disponible se identificaron en el proceso de búsqueda? | Resumir brevemente las limitaciones en el acceso a información, como problemas de acceso, sitios caídos, documentos no disponibles, buscadores deficientes, ambigüedad institucional,  información contradictoria, cobertura temporal u otras restricciones                    |
| fecha_ejecucion             | fecha       | ¿Cuándo se ejecutó la búsqueda para esta entidad?                                          | Registrar fecha en formato YYYY-MM-DD.                                                                                                                                                                                                                                         |
| agent_version               | texto       | ¿Qué versión del protocolo/agente produjo el registro?                                     | Registrar identificador de versión definido en este protocolo.                                                                                                                                                                                                                 |

### 10. Reglas específicas para existe_programa_proveeduria

Codificar existe_programa_proveeduria = 1 solo cuando exista evidencia suficiente de al menos una iniciativa elegible.

La evidencia suficiente debe demostrar simultáneamente:

1. que la iniciativa existe o existió como programa, convocatoria, línea, instrumento, proyecto o estrategia pública; y
2. que la iniciativa está vinculada con relaciones de proveeduría, desarrollo de proveedores, encadenamiento productivo, cadenas de valor, empresas ancla, empresas tractoras, grandes empresas o conexión entre empresas demandantes y mipymes/proveedores.

Codificar existe_programa_proveeduria = 0 cuando, después de una búsqueda razonable:

1. no se encuentra ninguna iniciativa relevante asociada a la entidad;
2. solo se encuentran programas generales de apoyo a mipymes sin relación explícita con proveeduría o encadenamiento;
3. solo se encuentran actividades puntuales o noticias sin evidencia de programa;
4. solo se encuentran fuentes ambiguas que no permiten justificar la inclusión; o
5. la entidad no tiene información disponible suficiente para respaldar la existencia de un programa elegible.

Si la evidencia sugiere que puede existir una iniciativa elegible, pero no permite confirmarlo, codificar existe_programa_proveeduria = 0, usar status = "needs_human_review" y explicar la ambigüedad en notas_busqueda.

### 11. Reglas específicas para n_programas_candidatos

La variable n_programas_candidatos debe ser un conteo a nivel de entidad, no a nivel de fila.

Ejemplos:

- Si la entidad no tiene programas elegibles: una fila con n_programas_candidatos = 0.
- Si la entidad tiene un programa elegible: una fila con n_programas_candidatos = 1.
- Si la entidad tiene tres programas elegibles: tres filas, cada una correspondiente a un programa distinto, y en las tres filas debe registrarse n_programas_candidatos = 3.

El conteo debe incluir únicamente iniciativas elegibles según este instrumento. No deben contarse programas dudosos, no elegibles, actividades puntuales ni iniciativas generales sin vínculo explícito con proveeduría.

Cuando existan dudas sobre si dos iniciativas son realmente distintas, el agente debe:

1. registrar ambas si tienen nombres, objetivos o fuentes diferenciadas;
2. asignar status = "needs_human_review";
3. explicar la duda en notas_busqueda.

### 12. Política de evidencia

Toda codificación positiva debe estar respaldada por evidencia verificable. La evidencia debe cumplir el siguiente contrato mínimo:

1. cita textual breve desde la fuente;
2. URL funcional o referencia documental;
3. fecha de acceso;
4. localizador preciso dentro de la fuente;
5. identificación de la institución que publica la fuente.

La evidencia debe ser suficientemente específica para que una persona pueda verificar por qué el programa fue incluido sin repetir toda la búsqueda.

### 13. Jerarquía de fuentes

El agente debe priorizar las fuentes según la siguiente jerarquía:

1. Página oficial de la entidad pública responsable.
2. Página oficial del programa, instrumento o convocatoria.
3. Bases de convocatoria, términos de referencia, reglamentos, manuales operativos o documentos oficiales.
4. Informes, memorias, reportes de gestión o documentos institucionales de la entidad.
5. Comunicados oficiales de entidades públicas asociadas.
6. Fuentes de organismos multilaterales, bancos de desarrollo, agencias de cooperación o instituciones públicas asociadas.
7. Prensa, blogs, presentaciones o fuentes secundarias.

Para codificar existe_programa_proveeduria = 1, se debe preferir una fuente oficial. Las fuentes secundarias pueden usarse como apoyo, pero no deben ser la única base para una codificación positiva, salvo que el registro quede marcado como needs_human_review y se explique la limitación.

### 14. Reglas de resolución de conflictos

Si distintas fuentes entregan información contradictoria, aplicar las siguientes reglas:

1. Preferir fuentes oficiales por sobre fuentes secundarias.
2. Preferir fuentes de la entidad responsable por sobre fuentes de terceros.
3. Preferir documentos de programa, bases o convocatorias por sobre noticias generales.
4. Preferir fuentes más recientes cuando se refieran al estado actual del programa.
5. Si se resuelven conflictos mediante inferencias, estas deben quedar documentadas en notas_busqueda.

### 15. Regla de exhaustividad

No limites la búsqueda a un número fijo de casos.
No te detengas al encontrar unas pocas iniciativas.

Debes identificar todas las iniciativas relevantes que puedas verificar razonablemente dentro del país. Si la entidad tiene muchas iniciativas, inclúyelas todas mientras sean verificables y suficientemente relevantes.

Para cada entidad, el agente deberá ejecutar el protocolo completo aunque ya haya encontrado uno o más programas candidatos.

#### 15.1. Prohibición de terminación temprana

Encontrar una iniciativa elegible no constituye una condición suficiente para finalizar la revisión de una entidad.

Después de cada hallazgo positivo, el agente deberá continuar buscando otras iniciativas potencialmente distintas, incluyendo programas vigentes, históricos, sectoriales, territoriales, interinstitucionales, convocatorias con nombre propio, mesas permanentes, plataformas, registros, líneas de asistencia y proyectos de desarrollo de proveedores.

El agente solo podrá cerrar la búsqueda de una entidad cuando haya completado todas las familias de búsqueda definidas en este protocolo y haya aplicado la regla de saturación.

#### 15.2. Familias mínimas de búsqueda obligatorias

Para cada entidad deberán realizarse, como mínimo, búsquedas en las siguientes familias:

1. Nombre exacto de la entidad combinado con:
    - proveedores;
    - desarrollo de proveedores;
    - proveedores locales;
    - pymes proveedoras;
    - cadena de valor;
    - cadenas de valor;
    - cadenas de suministro;
    - encadenamiento productivo;
    - encadenamientos productivos;
    - empresa ancla;
    - empresa tractora;
    - grandes empresas;
    - integración productiva;
    - articulación productiva.
2. Nombre exacto de la entidad combinado con tipos de instrumentos:
    - programa;
    - convocatoria;
    - proyecto;
    - iniciativa;
    - estrategia;
    - mesa;
    - red;
    - plataforma;
    - registro;
    - centro;
    - asistencia técnica;
    - financiamiento;
    - capacitación;
    - certificación;
    - fortalecimiento.
3. Nombre de la entidad combinado con sectores relevantes para su ámbito de actuación:
    - hidrocarburos;
    - energía;
    - minería;
    - naval;
    - automotriz;
    - agroindustria;
    - alimentos;
    - construcción;
    - industria;
    - turismo;
    - otros sectores pertinentes identificados durante la búsqueda.
4. Búsquedas por denominaciones institucionales alternativas:
    - siglas;
    - nombres anteriores;
    - ministerios o secretarías predecesoras;
    - organismos dependientes;
    - unidades ejecutoras;
    - consejos, agencias, institutos o direcciones vinculadas.
5. Búsquedas en fuentes documentales:
    - informes de gestión;
    - memorias institucionales;
    - presupuestos;
    - planes estratégicos;
    - documentos de política productiva;
    - bases y reglamentos;
    - repositorios de convocatorias;
    - boletines oficiales;
    - presentaciones institucionales;
    - informes de organismos públicos asociados.
6. Búsquedas históricas:
    - sin restricción al sitio web vigente;
    - con años específicos;
    - en versiones archivadas, informes anteriores y documentos históricos;
    - usando los nombres institucionales vigentes en cada período.

El agente debe adaptar los términos al idioma del país o fuente cuando corresponda. Por ejemplo, puede usar equivalentes como supplier development, anchor firms, value chains, local suppliers, small business suppliers, cadeias de valor, fornecedores locais, empresa âncora, desenvolvimento de fornecedores.
#### 15.3. Búsqueda expansiva a partir de cada hallazgo

Cada vez que se encuentre una iniciativa elegible o potencialmente elegible, el agente deberá realizar búsquedas adicionales usando:

- el nombre exacto de la iniciativa;
- variantes abreviadas o alternativas del nombre;
- el nombre de los organismos coejecutores;
- los sectores mencionados;
- los territorios participantes;
- los nombres de empresas ancla o cámaras empresariales mencionadas;
- expresiones distintivas contenidas en la fuente;
- referencias a ediciones, fases, convocatorias o programas madre.

Estas búsquedas deberán utilizarse para:

1. confirmar la existencia y continuidad de la iniciativa;
2. localizar una fuente oficial de mayor jerarquía;
3. determinar si la actividad pertenece a un programa más amplio;
4. identificar otras iniciativas relacionadas pero distintas;
5. identificar entidades públicas descubiertas conforme a las reglas del instrumento.

#### 15.4. Validación previa al cierre

Antes de asignar `answered` o `not_found_after_search`, el agente deberá responder internamente:

- ¿Continué buscando después del primer programa?
- ¿Busqué mesas, redes, plataformas, registros y proyectos, además de programas?
- ¿Revisé iniciativas compartidas con otras entidades públicas?
- ¿Busqué por sectores económicos?
- ¿Busqué nombres históricos y siglas?
- ¿Revisé informes de gestión y documentos, no solo páginas web?

Si alguna respuesta es negativa, la búsqueda no podrá considerarse concluida.

#### 15.5. Evidencia de exhaustividad en la salida

`notas_busqueda` deberá incluir, de forma breve pero verificable:

- principales dominios o repositorios revisados;
- nombres institucionales alternativos examinados;
- sectores explorados;
- iniciativas cercanas descartadas

Las notas de búsqueda no podrán ser genéricas ni repetirse de forma idéntica entre entidades.

### 16. Reglas para registrar búsquedas negativas

Cuando no se encuentre una iniciativa elegible, el agente debe documentar explícitamente la búsqueda negativa. En particular, debe registrar:

1. principales consultas ejecutadas;
2. fuentes o sitios revisados;
3. si se encontraron programas cercanos pero no elegibles;
4. razón por la cual esos programas fueron excluidos;
5. cualquier limitación relevante, por ejemplo sitio caído, enlaces rotos, ausencia de buscador interno, documentos no accesibles o ambigüedad institucional.

El objetivo es distinguir entre “no se buscó”, “se buscó y no se encontró” y “se encontró algo, pero no cumple la definición”.

### 17. Estados de codificación

Usar los siguientes valores para status:

| Valor                  | Definición                                                                                                                    |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| answered               | La variable fue respondida con evidencia suficiente.                                                                          |
| not_found_after_search | Se realizó una búsqueda razonable y no se encontró una iniciativa elegible.                                                   |
| needs_human_review     | El caso requiere revisión humana por duplicidad, ambigüedad, evidencia débil, fuentes contradictorias o decisión de frontera. |

### 18. Formato esperado de salida

Debes entregar los resultados en una tabla estructurada, como un archivo .xlsx llamado `dril_etapa1_[pais]_[version agente].xlsx` , con las columnas definidas en el instrumento DRIL.

La tabla final debe permitir reconstruir qué ocurrió con cada entidad del mapped unit space. Por eso, ninguna entidad debe desaparecer de la salida. Cada fila debe representar un programa candidato identificado para una entidad. Si no se encuentra ningún programa para una entidad, debe existir una fila de resultado negativo para esa entidad.

La tabla debe contener, como mínimo, las siguientes columnas, en este orden recomendado:

1. entity_id
2. entidad_input
3. pais
4. entidad_nivel
5. tipo_entidad
6. existe_programa_proveeduria
7. n_programas_candidatos
8. programa_candidato_id
9. nombre_candidato
10. razon_inclusion
11. evidencia_excerpt
12. evidencia_url
13. evidencia_fecha_acceso
14. evidencia_locator
15. source_title
16. source_role
17. source_institution
18. status
19. gap_reason
20. notas_busqueda
21. fecha_ejecucion
22. agent_version

### 19. Ventana temporal y búsqueda de iniciativas recientes

La búsqueda deberá cubrir tanto iniciativas con evidencia de su funcionamiento entre 2021 y 2026.

Para evitar omisiones de programas nuevos, el agente deberá ejecutar consultas específicas con:

- el año en curso (2026);
- los dos años anteriores (2024 y 2025);
- términos como “nuevo”, “lanzamiento”, “reglamentación”, “creación”, “convocatoria”, “registro” y “programa”.

También deberá revisar publicaciones recientes, resoluciones, decretos y páginas institucionales creadas después del último informe de gestión disponible.
### 20. Prompt operativo para el agente de implementación

Aplica el instrumento DRIL de Etapa 1 a la entidad pública asignada. Tu tarea es identificar si la entidad ofrece, ejecuta, financia, coordina o promueve una o más iniciativas públicas orientadas a crear, promover, apoyar o consolidar relaciones de proveeduría entre grandes empresas, empresas ancla o empresas tractoras, y mipymes, pymes, proveedores locales o empresas proveedoras.

Debes trabajar exclusivamente sobre la entidad asignada y no ampliar el mapped unit space. Realiza búsqueda web, priorizando fuentes oficiales de la entidad, páginas oficiales de programas, documentos de convocatoria, reglamentos, informes institucionales y fuentes públicas confiables. Aplica estrictamente los criterios de inclusión y exclusión del instrumento.

Si encuentras una iniciativa elegible, registra una fila por cada programa candidato. Si encuentras más de una iniciativa elegible para la misma entidad, registra una fila separada para cada una y repite en todas las filas el número total de iniciativas elegibles encontradas en n_programas_candidatos.

Para cada programa candidato, registra el nombre completo, una razón breve de inclusión y evidencia verificable. La evidencia debe incluir una cita textual, URL funcional, fecha de acceso, localizador preciso dentro de la fuente, título de la fuente e institución que la publica.

Si no encuentras ninguna iniciativa elegible, registra una fila negativa para la entidad, con existe_programa_proveeduria = 0, n_programas_candidatos = 0, status = "not_found_after_search" y una nota breve que documente las búsquedas realizadas y las razones por las que no se identificaron programas elegibles.

No infieras la existencia de programas sin evidencia. No codifiques como elegibles programas generales de apoyo a mipymes, innovación, productividad, emprendimiento o financiamiento si no existe evidencia explícita de relación con proveeduría, desarrollo de proveedores, empresas ancla, empresas tractoras, cadenas de valor o proveedores locales. Cuando exista ambigüedad, registra el caso como needs_human_review o unclear_definition y explica la razón.

### 21. Regla de honestidad de ejecución

El agente **no deberá declarar que una actividad fue realizada si no puede respaldarla en la bitácora**.

Cuando las limitaciones de tiempo, acceso, herramientas o volumen impidan completar el protocolo, deberá:

- identificar las entidades afectadas;
- usar `status = needs_human_review`;
- describir las familias de búsqueda pendientes;
- evitar presentar el resultado como exhaustivo o definitivo.

### 22. Checklist de validación previa a la entrega

El archivo puede entregarse únicamente cuando:

1. todas las entidades originales estén representadas;
2. todas las variables categóricas usen valores válidos; 
3. todas las filas positivas tengan evidencia verificable;
4. todas las filas negativas documenten una búsqueda razonable;
5. no existan incoherencias entre existe_programa_proveeduria, n_programas_candidatos, status y gap_reason.

Cuando un error no pueda corregirse con la evidencia disponible, el agente no debe ocultarlo ni completar información por inferencia. Debe asignar el estado correspondiente, explicar la limitación y marcar el caso para revisión humana.