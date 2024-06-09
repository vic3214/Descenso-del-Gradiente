# Método de Descenso del Gradiente

# Descripción

El método de descenso del gradiente es una técnica de optimización utilizada para minimizar (o maximizar) funciones. Es ampliamente utilizado en el aprendizaje automático y el ajuste de modelos, donde el objetivo es encontrar el mínimo de una función de costo. La idea central es iterativamente ajustar los parámetros del modelo en la dirección opuesta al gradiente de la función de costo con respecto a esos parámetros. Al hacerlo, se espera llegar al punto donde la función de costo alcanza su mínimo valor.

## Requisitos

1.  **Función de Costo**: Una función diferenciable J(θ) que se desea minimizar, donde θ representa los parámetros del modelo.
2.  **Gradiente de la Función de Costo**: El vector de derivadas parciales ∇J(θ), que indica la dirección del mayor incremento de la función de costo.
3.  **Tasa de Aprendizaje**: Un escalar α que determina el tamaño del paso que se da en cada iteración. La elección adecuada de α\alphaα es crucial para la convergencia del algoritmo.
4.  **Condición de Convergencia**: Un criterio para detener el algoritmo, que puede ser un número fijo de iteraciones, un cambio mínimo en la función de costo, o que el gradiente se acerque a cero.

## Pseudocódigo

1. Inicializar los parámetros θ (pueden ser inicializados aleatoriamente o con valores específicos).

2. Repetir hasta que se cumpla la condición de convergencia:
 a. Calcular el gradiente de la función de costo respecto a θ:
       ∇J(θ) = (∂J/∂θ₁, ∂J/∂θ₂, ..., ∂J/∂θₙ)

    b. Actualizar los parámetros θ en la dirección opuesta al gradiente:
       θ = θ - α * ∇J(θ)

3. Devolver los parámetros θ optimizados.`

## Ejemplo en Pseudocódigo

### Inicialización
θ = θ_inicial
α = tasa_de_aprendizaje
convergencia = False

### Ciclo de optimización
mientras no convergencia:
    # Calcular gradiente
    gradiente = calcular_gradiente(J, θ)
 ### Actualizar parámetros
    θ = θ - α * gradiente

    # Verificar condición de convergencia
    si norma(gradiente) < umbral:
        convergencia = True
### Retornar los parámetros optimizados
retornar θ

## Notas Adicionales

-   **Tasa de Aprendizaje**: Si la tasa de aprendizaje es muy grande, el algoritmo puede no converger y oscilar alrededor del mínimo. Si es muy pequeña, la convergencia puede ser extremadamente lenta.
-   **Tipos de Descenso del Gradiente**:
    -   **Descenso del Gradiente Estocástico (SGD)**: Actualiza los parámetros usando un solo ejemplo de entrenamiento por iteración.
    -   **Descenso del Gradiente por Mini-lotes**: Utiliza un pequeño lote de ejemplos de entrenamiento en cada iteración.
    -   **Descenso del Gradiente Batch**: Utiliza todos los ejemplos de entrenamiento para calcular el gradiente en cada iteración.

El método de descenso del gradiente es fundamental para muchos algoritmos de aprendizaje automático y su comprensión es esencial para el desarrollo de modelos eficientes y efectivos.


## Ejemplo

En este caso vamos a optimizar la función:


![sin(1/2 * x^2 - 1/4 *y^2 +3) * cos(2*x +1 - e^y)](https://www.sciweavers.org/tex2img.php?eq=sin%281%2F2%20%2A%20x%5E2%20-%201%2F4%20%2A%20y%5E2%20%2B%203%29%20%2A%20cos%282%2Ax%20%2B%201%20-%20e%5Ey%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit)

Evaluando la superficie de la función nos encontramos el siguiente resultado:

![Alt text](/img/Superficie.png)

Generando un punto aleatorio para el gradiente y realizando 1000 iteraciones con una tasa de aprendizaje de 0.001 obtenemos el siguiente resultado:

![Alt text](/img/Gradiente.png)

Se muestra con puntos rojos cada 100 iteraciones el progreso de la obtención del punto mínimo observándose como se acerca a zonas de mínimos en la superficie



