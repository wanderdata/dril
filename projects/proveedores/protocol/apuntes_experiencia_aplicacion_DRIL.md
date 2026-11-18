
## 1. Objetivo del ejercicio

El objetivo del ejercicio fue **mapear iniciativas públicas de desarrollo estratégico de proveedores en América Latina y el Caribe** y construir una base de datos que permitiera posteriormente caracterizarlas de manera sistemática.

El principal desafío metodológico era la **completitud del levantamiento**. La información sobre programas públicos se encuentra dispersa entre instituciones, sitios web, documentos y distintos niveles de gobierno. Además, la existencia de una iniciativa no siempre implica que toda la información relevante —por ejemplo, presupuesto, criterios de selección o reglamentos— esté disponible públicamente.

Para enfrentar este problema se utilizó la metodología **Deep Research on a Loop (DRIL)**, adaptándola a un levantamiento en el que la exhaustividad era especialmente importante.

---

## 2. ¿Qué es DRIL?

La metodología **Deep Research on a Loop (DRIL)**, propuesta por Santiago Afonso, Sebastian Galiani, Ramiro H. Gálvez y Raul A. Sosaque (2026), concibe la construcción de bases de datos de investigación como un proceso integrado de:

1. búsqueda de información;
2. evaluación de la evidencia;
3. extracción de información; y
4. codificación de los resultados.

A diferencia de un esquema en que estas tareas se realizan por separado, DRIL utiliza un agente de inteligencia artificial que recibe dos insumos principales:

- un **instrumento de investigación**, que especifica qué información debe buscarse y cómo debe codificarse; y
- un **mapa de unidades de búsqueda** (*mapped unit space*), que define sobre qué entidades, casos o unidades debe ejecutarse la búsqueda.

A estos elementos se suma una **política de evidencia**, que establece qué fuentes priorizar, cómo resolver discrepancias y cómo documentar la información utilizada.

Sobre esta base, el agente realiza de forma relativamente autónoma el proceso de búsqueda y extracción. El producto esperado no es solamente una base estructurada, sino también un **registro auditable de la evidencia** que permita rastrear cómo se construyó cada observación.

---

## 3. Componentes que fue necesario adaptar

Para aplicar DRIL al mapeo de programas de desarrollo de proveedores fue necesario operacionalizar tres componentes: el instrumento de investigación, el mapa de unidades de búsqueda y la política de evidencia.

### 3.1. Instrumento de investigación

El instrumento funciona de manera similar a un **libro de códigos**. Para cada variable debe establecer:

- la pregunta precisa que debe responder el agente;
- el tipo de respuesta esperada;
- las restricciones o valores admisibles;
- las reglas para traducir la información encontrada en categorías o valores comparables; y
- el formato del campo de salida.

Además de las reglas específicas de cada variable, el instrumento debe contener criterios transversales para situaciones frecuentes durante el levantamiento. Por ejemplo:

- qué hacer cuando la fuente no contiene una coincidencia literal con la información buscada;
- cómo registrar información faltante;
- cuándo incorporar una nota interpretativa;
- qué casos deben quedar marcados para revisión humana; y
- cuánto detalle conservar sobre las fuentes utilizadas.

En esta aplicación fue especialmente importante definir con claridad **qué debía entenderse por una iniciativa candidata**, qué nivel de caracterización se requería y qué información necesitaba conocer el agente para decidir si una iniciativa debía incorporarse al levantamiento.

### 3.2. Mapa de unidades de búsqueda

El *mapped unit space* define las unidades sobre las cuales se ejecutará el instrumento.

En DRIL, cada unidad representa una instancia en que el agente debe aplicar el protocolo completo. Por ejemplo, un levantamiento compuesto por 30 países observados durante 20 años tendría 600 unidades de búsqueda.

En este caso, como el objetivo era identificar iniciativas públicas, el primer mapa de unidades se construyó a partir de **entidades que potencialmente podían promover programas de desarrollo de proveedores**.

Se incorporaron:

- ministerios y entidades nacionales vinculadas al desarrollo productivo;
- organismos sectoriales, por ejemplo en agricultura, minería o energía;
- gobiernos subnacionales correspondientes a la primera división administrativa; y
- gobiernos de las principales unidades administrativas de segundo nivel en términos de contribución al PIB nacional, cuando este nivel territorial resultaba relevante para identificar ciudades o territorios productivamente importantes.

La construcción del mapa de unidades fue, por tanto, una decisión sustantiva: determina **dónde busca el agente** y condiciona directamente la cobertura posible del levantamiento.

### 3.3. Política de evidencia

La política de evidencia establece cómo debe localizarse, evaluar y documentar la información.

Un primer elemento es la **jerarquía de fuentes**. Para este ejercicio se priorizaron fuentes con mayor autoridad institucional y cercanía al programa, tales como:

- sitios web oficiales;
- documentos institucionales de los programas;
- normativa o documentos administrativos;
- informes de organismos públicos.

Estas fuentes tienen prioridad frente a comunicados de prensa, noticias periodísticas u otras fuentes secundarias.

Un segundo elemento son las **reglas para resolver discrepancias entre fuentes**. Dependiendo del tipo de información, puede ser razonable privilegiar la fuente más oficial, la más reciente o la que entregue mayor nivel de detalle. Si la contradicción no puede resolverse con seguridad, el registro debe conservar la discrepancia o quedar marcado para revisión humana.

Esta lógica puede ilustrarse con documentos institucionales como un informe de DIPRES: no basta con que una fuente mencione un programa; también interesa evaluar su autoridad, fecha, nivel de detalle y relación directa con la variable que se busca documentar.

---

## 4. Diseño de la aplicación: dos etapas secuenciales

Una sola ejecución no era suficiente para resolver simultáneamente dos problemas distintos: **descubrir el universo de iniciativas** y **caracterizar cada iniciativa con profundidad**.

Por esa razón, la aplicación se organizó en dos etapas.

### Etapa 1. Identificación de iniciativas candidatas

En la primera etapa, el mapa de unidades estuvo compuesto por las posibles **entidades promotoras**.

Para cada entidad, el agente debía buscar programas, instrumentos o iniciativas vinculados con temas como:

- desarrollo de proveedores;
- encadenamientos productivos;
- clusters;
- compras locales;
- integración a cadenas de valor; o
- relaciones entre empresas ancla y proveedores locales.

El objetivo de esta etapa era privilegiar la **sensibilidad del levantamiento**: era preferible incorporar algunos casos que después pudieran descartarse antes que excluir tempranamente una iniciativa relevante.

Los resultados de esta fase se revisan manualmente para:

- eliminar duplicados;
- descartar iniciativas que no cumplen los criterios definidos; y
- resolver casos ambiguos.

### Etapa 2. Caracterización de los programas

Una vez depurada la primera base, cada programa candidato pasa a constituir una **unidad de búsqueda independiente**.

En esta segunda etapa, el agente aplica un instrumento más detallado para caracterizar aspectos como:

- objetivos;
- población beneficiaria;
- mecanismos de intervención;
- cobertura territorial;
- instrumentos o servicios ofrecidos; y
- evidencia disponible sobre alcance o resultados.

La primera etapa, por tanto, cumple una función de **descubrimiento y delimitación del universo**, mientras que la segunda produce una **caracterización comparable y auditable** de las iniciativas seleccionadas.

---

## 5. Ajuste iterativo del instrumento antes de la ejecución

Un aprendizaje importante fue que el protocolo no debía asumirse como definitivo desde el primer intento.

En los apuntes de trabajo este proceso fue denominado “fine-tuning”, pero en la práctica correspondió principalmente a un **ajuste iterativo del instrumento, el prompt y, en algunos casos, del propio mapa de unidades**, a partir de pruebas controladas.

La lógica fue doble:

- el agente debe aprender, a través de instrucciones cada vez más precisas, qué tipo de comportamiento se espera de él; y
- quien diseña el levantamiento también debe aprender qué instrucciones producen el comportamiento deseado y cuáles permiten atajos no previstos.

### 5.1. Casos utilizados para las pruebas

Se seleccionaron tres países con diferencias importantes de tamaño y complejidad institucional:

- Argentina;
- República Dominicana; y
- Trinidad y Tobago.

Para cada versión del protocolo se registraron en una planilla algunos indicadores simples:

- tiempo de ejecución;
- número de filas de salida;
- número de programas identificados;
- número de entidades para las que se encontraron más de un programa; y
- notas cualitativas sobre el comportamiento observado.

El objetivo no era evaluar el desempeño con una única métrica, sino identificar señales de que el agente estuviera **acortando la búsqueda o satisfaciendo la instrucción de manera demasiado superficial**.

### 5.2. Tiempo de ejecución como señal diagnóstica

El tiempo de ejecución se utilizó como una señal indirecta.

Dado que los tres países tenían niveles distintos de complejidad institucional, resultaba sospechoso que el agente demorara muy poco o prácticamente el mismo tiempo en todos ellos. Esto podía sugerir que la búsqueda no estaba siendo suficientemente exhaustiva.

El tiempo, por sí solo, no prueba la calidad del levantamiento. Su utilidad fue principalmente **diagnóstica**, al combinarlo con los demás indicadores.

### 5.3. Filas de salida y cobertura de las unidades

El número de filas permitía verificar rápidamente si el agente había respetado la estructura solicitada y si había buscado información para todas las unidades entregadas.

Esto ayudaba a detectar omisiones evidentes o ejecuciones en las que parte del mapa de unidades quedaba sin procesar.

### 5.4. Número de programas identificados

El número total de programas fue útil para detectar patrones demasiado regulares.

Por ejemplo, si países muy distintos producían sistemáticamente una cantidad similar de programas, podía existir un punto implícito en que el agente consideraba que ya había encontrado una cantidad “suficiente” y detenía la búsqueda.

### 5.5. Entidades con más de un programa

También se observó cuántas entidades tenían **más de un programa identificado**.

Si prácticamente todas las entidades producían como máximo una iniciativa, podía ser señal de que el agente estaba interpretando la tarea como “encontrar un programa por entidad” en lugar de buscar exhaustivamente todas las iniciativas relevantes.

Este indicador fue especialmente útil para revisar si el agente continuaba investigando después de encontrar una primera respuesta plausible.

---

## 6. Ajustes al tamaño de las ejecuciones

Las pruebas mostraron que no siempre era conveniente ejecutar mapas de unidades muy grandes en una sola interacción.

En algunos casos se modificó el tamaño del *unit space*. Brasil y México, por ejemplo, terminaron dividiéndose en dos ejecuciones.

La razón práctica era evitar que, frente a una tarea demasiado extensa, el agente comenzara a tomar **decisiones de optimización no explícitas**, reduciendo la profundidad de búsqueda o cerrando prematuramente algunos casos.

No se dispone de una explicación causal de este comportamiento. La interpretación de trabajo fue que el agente busca producir una respuesta satisfactoria dentro de restricciones de contexto y procesamiento y, ante tareas muy extensas, puede priorizar implícitamente unas partes por sobre otras.

Por eso, la supervisión humana sigue siendo central. En un levantamiento cuyo objetivo es la exhaustividad, no basta con que la respuesta “parezca razonable”: es necesario diseñar controles que permitan detectar cuándo el agente está simplificando la tarea de una manera que entra en conflicto con el objetivo de investigación.

---

## 7. Congelamiento del protocolo y ejecución

Una vez terminada la fase de pruebas, el protocolo debe quedar **congelado** para que las distintas ejecuciones sean comparables.

Esto es importante porque modificar las instrucciones durante el levantamiento puede introducir diferencias sistemáticas entre grupos de unidades.

Se identificaron dos formas posibles de ejecutar el protocolo.

### Opción 1. Uso de un agente

La alternativa más sencilla consiste en crear un agente con toda la documentación e instrucciones necesarias y ejecutar el mapa de unidades por bloques.

Esta opción facilita la experimentación y la supervisión directa durante las primeras aplicaciones.

### Opción 2. Ejecución mediante API

Una segunda alternativa es interactuar directamente con la API y estructurar entradas y salidas, por ejemplo, en formato JSON.

Este enfoque facilita una ejecución más sistemática y reproducible cuando el protocolo ya se encuentra suficientemente estabilizado.

En ambos casos, el principio es el mismo: **las reglas de búsqueda, codificación y evidencia deben permanecer constantes durante la producción de la base definitiva**.

---

## 8. La intensidad del ajuste depende del objetivo

La cantidad de pruebas necesarias depende del tipo de problema que se intenta resolver.

En este ejercicio, la **exhaustividad** era una propiedad central. Por esa razón fue necesario prestar especial atención a posibles comportamientos de detención temprana y realizar varias iteraciones del instrumento.

En otras aplicaciones de DRIL, el costo de una omisión puede ser mucho menor.

Por ejemplo, la metodología también fue utilizada para automatizar el mapeo y *screening* de oportunidades internacionales de financiamiento y estancias de investigación. En ese caso, el objetivo no era construir un universo exhaustivo, sino identificar las oportunidades principales que mejor se ajustaran al perfil de los investigadores. Por ello, se requirió mucho menos ajuste previo.

Algo similar ocurre cuando el diseño exige solamente una respuesta por país o por unidad. Ese tipo de tarea está más cerca de la lógica habitual del agente: encontrar una respuesta adecuada y discriminar entre alternativas. El problema se vuelve metodológicamente más exigente cuando se busca asegurar que **no existan respuestas adicionales relevantes que hayan quedado fuera**.

---

## 9. Productos de la aplicación

La ejecución produjo tres bases complementarias.

### 9.1. Base del mapa de unidades

Registra las entidades incluidas en el *mapped unit space* e indica si se encontraron programas asociados a cada una.

Su función es permitir evaluar la cobertura de la búsqueda y conservar información también sobre aquellas unidades en que no se encontraron iniciativas.

### 9.2. Base de caracterización

Contiene las iniciativas o programas candidatos identificados. En esta aplicación se caracterizaron **265 iniciativas**.

Para cada pregunta de interés se generaron:

- una columna con la información extraída; y
- una columna paralela de **estado o *status***.

Esta estructura permite distinguir, por ejemplo, entre un valor efectivamente encontrado, información no disponible o casos que requieren revisión.

### 9.3. Base de evidencia

Vincula cada respuesta con su fuente.

Incluye elementos como:

- referencia o URL;
- localizador detallado dentro de la fuente;
- cita o fragmento relevante;
- fecha de la fuente; y
- fecha de acceso.

Esta base es fundamental para la auditabilidad del ejercicio: permite volver desde el dato codificado hasta la evidencia que lo sustenta.

### 9.4. Diccionario de variables

Para facilitar el uso de los resultados por terceras personas, se solicitó al agente que generara un **diccionario de variables a partir del instrumento**.

Esto ayuda a mantener alineados el protocolo de investigación, la estructura de la base y la documentación destinada a usuarios posteriores.

---

## 10. Resultados preliminares y control de calidad

Hasta el momento no se han identificado problemas mayores en los resultados.

Sí aparecen algunos casos en que un programa contiene **algún componente de desarrollo de proveedores sin que éste constituya su objetivo principal**, particularmente en países donde se identificaron pocas iniciativas candidatas.

Este tipo de falso positivo era esperable dado el diseño del levantamiento: se privilegió deliberadamente la exhaustividad en la etapa de descubrimiento, dejando parte del filtrado para la revisión posterior.

Como control adicional, se realizaron revisiones externas de algunos países:

- las iniciativas de Colombia fueron revisadas por una revisora externa;
- las iniciativas de Chile fueron revisadas por tres revisores externos.

Hasta el momento, esas revisiones no han identificado inconsistencias ni vacíos relevantes. Esto constituye una señal positiva sobre el funcionamiento del procedimiento, aunque no reemplaza una evaluación sistemática de cobertura y precisión para todo el universo.

---

## 11. Límites de la información disponible

DRIL puede sistematizar y ampliar sustantivamente la búsqueda, pero no puede recuperar información que **no está publicada o no es accesible en línea**.

Algunos campos resultaron mucho más difíciles de completar que otros.

El caso más claro es el presupuesto: **202 de las 265 iniciativas caracterizadas no contaban con información disponible**, equivalente al 76 % de los casos.

Problemas similares aparecen en variables como:

- reglamentos específicos de los programas; y
- criterios de selección de las empresas participantes.

Este tipo de información administrativa no siempre se publica en internet, aun cuando el programa esté claramente documentado en otras dimensiones.

---

## 12. Sesgos propios de la fuente

El levantamiento se restringió a iniciativas cuya existencia durante los **últimos cinco años** pudiera demostrarse a partir de fuentes disponibles.

Esto introduce al menos dos limitaciones.

### 12.1. Mayor visibilidad de los inicios que de los cierres

En internet suele existir abundante información sobre:

- lanzamientos;
- inauguraciones;
- anuncios; y
- puesta en marcha de programas.

En cambio, es mucho menos frecuente encontrar documentación explícita sobre:

- discontinuación;
- cierre;
- pérdida de financiamiento; o
- término efectivo de una iniciativa.

Por ello, demostrar que un programa existió recientemente suele ser más sencillo que determinar con seguridad si continúa vigente.

### 12.2. Diferencias entre países en disponibilidad de información

La cantidad y calidad de información pública disponible en línea varía considerablemente entre países.

Este problema fue particularmente visible en algunos países pequeños del Caribe, donde existe menos documentación de gestión pública disponible en internet.

Por lo tanto, una menor cantidad de programas identificados no debe interpretarse automáticamente como evidencia de una menor actividad de política pública: también puede reflejar diferencias en la **observabilidad digital** de las intervenciones.

---

## 13. Principales aprendizajes metodológicos

La aplicación deja varios aprendizajes que pueden ser útiles para explicar DRIL en una presentación.

**Primero, DRIL no elimina las decisiones de diseño de investigación.** Por el contrario, obliga a explicitarlas. El agente necesita saber qué buscar, dónde buscar, qué cuenta como evidencia y cómo convertir lo encontrado en datos.

**Segundo, el mapa de unidades es tan importante como el prompt.** Una búsqueda exhaustiva solo puede serlo dentro del espacio que se definió previamente. Si una institución relevante no está incluida, el agente no necesariamente compensará esa omisión por sí solo.

**Tercero, la exhaustividad requiere controles específicos.** Los agentes están bien preparados para encontrar una respuesta plausible, pero un levantamiento exhaustivo exige comprobar además que no estén deteniendo la búsqueda después de encontrar una cantidad que parezca suficiente.

**Cuarto, las pruebas deben reflejar el objetivo sustantivo del proyecto.** Tiempo de ejecución, número de programas o cantidad de entidades con múltiples iniciativas no son métricas universales de calidad; en este caso fueron indicadores útiles porque permitían detectar señales de búsqueda incompleta.

**Quinto, la revisión humana sigue siendo parte de la metodología.** Cumple al menos tres funciones: calibrar el instrumento, detectar comportamientos no deseados durante las pruebas y revisar casos ambiguos o posibles falsos positivos después de la ejecución.

**Sexto, la trazabilidad es uno de los principales aportes del enfoque.** La combinación de una base de caracterización con una base de evidencia permite que terceras personas revisen cómo se construyó cada dato y vuelvan a la fuente original.
