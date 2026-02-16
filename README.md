# Taller Independiente - Programación Distribuida  
## Primer Sistema Cliente-Servidor con Sockets en Linux

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" height="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="60" height="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="60" height="60"/>
</p>

**Estudiante:** Esteban Murillo Gómez  
**Asignatura:** Programación Distribuida  

# README - Investigación Cliente-Servidor

## 1. ¿Qué es cliente-servidor?
El modelo cliente-servidor es básicamente una forma de organizar cómo se comunican las computadoras en una red, funciona de la siguiente manera tienes un cliente que puede ser tu navegador, una app en tu celular o cualquier programa que pide algo, y del otro lado está el servidor, que es como una computadora más potente que recibe esa petición, busca lo que necesitas y te lo envía de vuelta.

Lo vemos todos los días cuando entramos por internet, usamos plataformas de streaming, revisamos el correo o jugamos en línea, básicamente, cada vez que tu dispositivo le pide información a otro sistema y recibe una respuesta, ahí está funcionando este modelo, es la base de casi todo lo que hacemos en internet y en las redes de las empresas.

## 2. Diferencia entre proceso e hilo
Un proceso es como abrir un programa completo en el computador, por ejemplo cuando abro Chrome o Word, cada uno es un proceso independiente que tiene su propia memoria y recursos, es como si cada programa viviera en su propia casa con sus propias cosas.

Los hilos son diferentes, es como si dentro de Chrome hay varias pestañas abiertas haciendo cosas al mismo tiempo, una reproduce un video, otra carga una página y otra descarga un archivo, esos serían los hilos, pequeñas tareas que corren en paralelo dentro del mismo proceso compartiendo los recursos.

La diferencia clave es que un proceso consume más recursos porque necesita su propio espacio, mientras que los hilos son más eficientes porque comparten memoria y pueden comunicarse más rápido entre ellos.

## 3. ¿Qué hicimos?
En la clase armamos nuestro primer sistema cliente-servidor desde cero usando Python en Linux, creamos dos archivos separados, servidor.py y cliente.py.  
Lo interesante fue que los ejecutamos en terminales diferentes, como si fueran dos programas totalmente independientes hablando entre sí.

Para que se pudieran comunicar usamos sockets TCP, que básicamente es la forma en que los programas se conectan y envían mensajes a través de la red. técnicamente hicimos nuestro primer sistema distribuido funcional.

además, instalamos Git en Linux y configuramos el repositorio para subir el proyecto a GitHub utilizando autenticación con token en lugar de contraseña, porque para mi es mas seguro, aunque también tuve algunos conflictos con la contraseña.

## 4. ¿Qué aprendimos?
Este ejercicio nos mostró lo que realmente es la Programación Distribuida, no fue solo escribir código en un archivo, sino entender cómo dos programas separados pueden comunicarse y trabajar juntos.

Aprendimos sobre procesos independientes, ya que cada terminal ejecutaba su propio programa (servidor y cliente) y ambos debían coordinarse para funcionar correctamente.  
También usamos sockets TCP como canal de comunicación entre procesos a través de la red.

Igualmente notamos conceptos reales como la latencia, es decir, el pequeño tiempo de espera cuando se envían y reciben datos, y la importancia del orden de ejecución (primero el servidor y luego el cliente).

### Conceptos observados en la práctica:
- Procesos independientes: ejecución de servidor.py y cliente.py  
- Comunicación por red: uso de sockets TCP  
- Latencia: tiempo de espera en la respuesta del servidor  
- Fallos: posibles errores de conexión o timeout  
- Coordinación: orden correcto de ejecución servidor → cliente  

## 5. Dificultades
Tuve bastantes dificultades con la autenticación en GitHub, ya que el sistema solicitaba contraseña, y realmente yo no recuerdo mi password de github, asi que debi generar un token para asi usar el token como password.  
También fue necesario entender que el servidor debía ejecutarse primero para que el cliente pudiera conectarse correctamente. 
