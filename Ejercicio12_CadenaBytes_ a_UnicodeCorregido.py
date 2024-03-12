# Crear una variable que contenga el texto que ustedes quieran en formato byte , en lo posible extenso, y convertirlo a Unicode.

#### Lo que se puede hacer es usar la clase bytes donde le tenes que pasar una cadena de texto y la codificacion
#### en este caso le pasamos utf-8, para que tenga en cuenta los acentos y demas caracteres que no tiene ASCII
#### ademas fijate que podemos utilizar la triple comilla y ahora si podemos poner los puntos y aparte, ya que
#### de esta forma cuando lo imprime lo representa tal cual como lo pongas vos entre ese triple comillado.

byte = bytes("""El preludio es uno de los géneros más singulares del periodo barroco. Concebido como pieza introductoria a una obra más extensa y compleja (p.e. una fuga) o a una suite de danzas, las características musicales del preludio remiten a dos funciones básicas que todo instrumentista ha ejercitado: tantear la afinación o las cualidades sonoras del instrumento (especialmente si es la primera vez que se toca) y «calentar» los dedos antes de acometer la interpretación de una obra exigente. En esta primera entrada dedicada al preludio estudiaremos uno de los más famosos de la era barroca, el que abre la primera Suite para violonchelo solo BWV 1007, en Sol mayor, de J. S. Bach. Un aficionado al cello de la familia Van der Mersch [1736], óleo de Cornelis Troost.Como hemos adelantado en la introducción, el acto de preludiar es una acción inseparable del oficio del instrumentista. 

Esta acción suele ser llevada a cabo mediante el encadenamiento libre de elementos variopintos, como escalas, arpegios, pasajes de diversas obras o fragmentos improvisados. Esta actividad, en principio puramente mecánica, pero de gran importancia desde el punto de vista de la preparación física y psíquica del intérprete, ha alcanzado en determinados contextos una cierta categoría artística, desembocando eventualmente en la escritura de obras -por lo general de pequeña extensión- que nos permiten hoy en día hacernos una ligera idea del sofisticado arte improvisatorio de otras épocas. 

Fue Louis Couperin -tío del más famoso de los Couperin, François– quien instituyó a mediados del siglo XVII un influyente modelo de este género, gracias a los préludes non mesurés (preludios en ritmo libre) que incluyó en sus suites para clave. El origen improvisatorio de estas piezas queda reflejado de forma elocuente en su renuncia al compás y al empleo de un sistema de notación rítmica que deja al intérprete una libertad total en cuanto a la elección de las duraciones de las notas. En cuanto a Bach -un improvisador excepcional, según los testimonios de la época-, desarrolló este género a partir de modelos que contaban con una notable raigambre en Alemania, y que habían sido practicados -o lo siguieron siendo- por grandes maestros organistas -como Dietrich Buxtehude o Johann Pachelbel– o laudistas, como su amigo Sylvius Leopold Weiss, cuyas suites instrumentales guardan notables semejanzas con las del compositor de Leipzig.""", 'utf-8')

print(byte.decode()) 


