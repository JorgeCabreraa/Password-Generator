Nota de Seguridad
Este script ha sido diseñado evitando el uso de generadores pseudo-aleatorios deterministas. Al utilizar secrets.choice(), el tiempo estimado para descifrar una contraseña de 15 caracteres generada por este script mediante fuerza bruta es de billones de años, superando ampliamente la edad actual del universo.
Desarrollado con ❤️ por un entusiasta de la ciberseguridad.
Secure Password Generator (CSPRNG)

Este es un mini proyecto desarrollado en Python que genera contraseñas robustas y criptográficamente seguras. El objetivo de este script es proporcionar una herramienta simple pero profesional para la creación de claves de acceso, priorizando la seguridad y la robustez del código.

Características Principales
> Seguridad Criptográfica: Utiliza la librería `secrets` (en lugar de `random`), lo que garantiza que las contraseñas sean impredecibles y aptas para uso en seguridad real.
> Manejo de Errores Robusto: Implementa validaciones con bloques `try/except` para asegurar que el programa no se detenga ante entradas inválidas (como letras en el campo de longitud).
> Personalización de Longitud: Permite definir la extensión de la contraseña, con límites de seguridad recomendados.
> Alta Entropía: Combina letras (mayúsculas/minúsculas), dígitos y caracteres especiales de la librería `string`.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x
Librerías Nativas:
    * `secrets`: Para generación de aleatoriedad segura.
    * `string`: Para manipulación de sets de caracteres.

💻 Cómo Ejecutar el Proyecto
1.  Asegúrate de tener Python 3 instalado.
2.  Clona este repositorio o descarga el archivo `contra.py`.
3.  Ejecuta el script desde tu terminal:
    ```bash
    python contra.py
    ```
4.  Ingresa la longitud deseada cuando el programa lo solicite.

🛡️ Nota de Seguridad
A diferencia de los generadores que usan la librería `random`, este script utiliza fuentes de aleatoriedad del sistema operativo. Una contraseña de **15 caracteres** generada con esta herramienta tardaría billones de años en ser descifrada por fuerza bruta, superando incluso la edad del universo
