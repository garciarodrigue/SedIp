import requests
import json

# Obtener los datos de las IPs desde la API de Firebase
firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
response = requests.get(firebase_url)
data = json.loads(response.content)

# Verificar si existen IPs en la respuesta
if data and 'ips' in data:
    ips = data['ips']

    # Generar el contenido HTML con las IPs
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="css/style.css">
        <title>Bases de Datos Ip</title>
    </head>
    <body class="cuerpo">
    <div class="div-ip">
        <h1 class="h1-tt">IPs almacenadas <sub>base de datos</h1>
        <br>
        <ul>
    '''

    for ip in ips:
        html_content += f'<li class="ips">{ip}</li>'

    html_content += '''
        </ul>
        <br>
        <br>
        <br>
        </div>
        <div class="info">
          <h3 class="des">Sed Ip<h3>
         <div>
         <p class="nota">Todas las ip's mostradas <br> estan en la base de datos<p>
      <div>
      <a class="url" href="https://github.com/garciarodrigue">GITHUB </a>
     <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
</svg>
<br>
 <a class="url" href="https://t.me/Sc_Hckrs">TELEGRAM </a>
    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-telegram" id="teleg" viewBox="0 0 16 16">
  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.287 5.906c-.778.324-2.334.994-4.666 2.01-.378.15-.577.298-.595.442-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294.26.006.549-.1.868-.32 2.179-1.471 3.304-2.214 3.374-2.23.05-.012.12-.026.166.016.047.041.042.12.037.141-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8.154 8.154 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629.093.06.183.125.27.187.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.426 1.426 0 0 0-.013-.315.337.337 0 0 0-.114-.217.526.526 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09z"/>
</svg>
      </i>
        
      </div>   
    </body>
    </html>
    '''

    # Guardar el contenido HTML en un archivo
    with open('ips.html', 'w') as file:
        file.write(html_content)

    print("El archivo HTML 'ips.html' se generó correctamente.")

else:
    print("No se encontraron IPs en la base de datos.")

