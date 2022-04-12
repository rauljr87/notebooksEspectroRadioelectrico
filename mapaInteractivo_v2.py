import folium
from folium import plugins
from folium.plugins import MarkerCluster
import webbrowser


# Definiendo Función
def mapa_interactivo(latitud, longitud, servicio, tipo_estacion, frecuencia_tx,
                     nombre_emisora, potencia_salida, potencia_efectiva, name_map):

    # Creación mapa con coordenas de Ecuador
    maps = folium.Map (location=[-1.831239, -78.183406], zoom_start=7)

    # Creación capa cartográfica
    folium.TileLayer('openstreetmap').add_to(maps)

    # Creación grupo con características
    feature_group = folium.FeatureGroup(
        name=servicio,
        overlay=False,
        control=True,
        show=False
    )

    # Creación del Marker Cluster
    marker_cluster = MarkerCluster().add_to(feature_group)

    # Creación marcador para mostrar en el mapa
    folium.Marker(
        location=[latitud, longitud],
        popup="""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                table {{width:100%}}
                table, th, td {{border: 1px solid black; border-collapse: collapse}}
                th, td {{padding: 5px; text-align: left}}
                table#t01 tr:nth-child(odd) {{background-color: #eee}}
                table#t01 tr:nth-child(even) {{background-color: #fff}}
                </style>
            </head>
              
            <p>DESCRIPCIÓN:</p>
            
            <body>
                <table id="t01">
                    <tr>
                        <td>TIPO_ESTACION: </td><td>{}</td>
                    </tr>
                        <tr><td>RED: </td><td>{}</td>
                    </tr>
                    <tr>
                        <td>FRECUENCIA_TX: </td><td>{} MHz</td>
                    </tr>
                    <tr>
                        <td>POTENCIA_SALIDA: </td><td>{} W</td>
                    </tr>
                    <tr>
                        <td>PER: </td><td>{} W</td>
                    </tr>
                    <tr>
                        <td>SERVICIO: </td><td>{}</td>
                    </tr>
                    <tr>
                        <td>LATITUD: </td><td>{}</td>
                    </tr>
                    <tr>
                        <td>LONGITUD: </td><td>{}</td>
                    </tr>
                </table>
            </body>
            </html>""".format(tipo_estacion, nombre_emisora, frecuencia_tx, potencia_salida,
                              potencia_efectiva, servicio, latitud, longitud)
    ).add_to(marker_cluster)

    # Añadiendo el feature group al mapa
    feature_group.add_to(maps)

    # Añadiendo plugins
    plugins.LocateControl().add_to(maps)
    plugins.Fullscreen().add_to(maps)
    plugins.MousePosition().add_to(maps)

    # Creación caja de control
    folium.LayerControl().add_to(maps)

    # Save
    maps.save(name_map)

    # apertura automática en el web browser
    return webbrowser.open(name_map)


# Variables para la función
# Tipo de servicio: FM, TV, etc
servicio = 'Frecuencia Modulada'
# Coordenadas en Grado Decimal
latitud = -0.2941944444444444
longitud = -78.51149166666667
# Información a mostrar en el popup:
tipo_estacion = 'MATRIZ'
nombre_emisora = 'Emisora FM'
frecuencia_tx = 88.9
potencia_salida = 250
potencia_efectiva = 1500.4
# Nombre de archivo html
name_map = 'prueba_03.html'


# Ejecución
mapa_interactivo(latitud, longitud, servicio, tipo_estacion,
                 frecuencia_tx,nombre_emisora, potencia_salida,
                 potencia_efectiva, name_map)