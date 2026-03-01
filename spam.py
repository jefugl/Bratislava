# main.py
import inputdata
import folium
from folium.plugins import BeautifyIcon
import pandas as pd
from pathlib import Path
import webbrowser

def main():
    start = (48.148, 17.107)

    # Bygg en konsistent bildeliste (samme antall som lat/lon/name/addr)
    images = [
        inputdata.fabrika,
        inputdata.slovak,
        inputdata.mestiansky,
        inputdata.goblins,
        inputdata.zbrojnos,
        inputdata.uisce,
        inputdata.cierny,
        inputdata.dubliner,
    ]

    data = pd.DataFrame({
        "lat":  inputdata.latitude,
        "lon":  inputdata.longitude,
        "name": inputdata.pubname,
        "addr": inputdata.pubaddress,
        "img":  images,
    })
    assert data.apply(len).nunique() == 1, "Alle kolonner i DataFrame må ha samme lengde"

    m = folium.Map(
        location=start,
        zoom_start=16,
        min_zoom=10,
        max_zoom=18,
        width="60%",
        height="80%",
    )

    for i in range(len(data)):
        name = data.iloc[i]["name"]
        addr = data.iloc[i]["addr"]
        img  = data.iloc[i]["img"]
        lat  = data.iloc[i]["lat"]
        lon  = data.iloc[i]["lon"]
        num  = i + 1

        html = (
            '<div style="max-width:360px;">'
            f'  <div style="font-weight:700; margin-bottom:6px;">{name}</div>'
            # f'  {img}'
            f'  <div style="margin-top:6px;"><span>{addr}</span></div>'
            '</div>'
        )
        popup = folium.Popup(folium.IFrame(html=html), min_width=200, max_width=350)

        marker = folium.Marker(
            location=[lat, lon],
            popup=popup,
            icon=BeautifyIcon(
                number=num,
                icon_shape="marker",
                border_color="#1e88e5",
                text_color="#ffffff",
                background_color="#1976d2",
                inner_icon_style="margin-top:2px;"
            ),
        ).add_to(m)

        folium.Tooltip(
            f"{num}. {name}",
            permanent=True,
            direction="right",
            sticky=False
        ).add_to(marker)

    title = "Bratislava 2026"
    title_html = f"""
        <h3 align="left" style="font-size:22px"><b>{title}</b></h3>
    """
    m.get_root().html.add_child(folium.Element(title_html))

    m.save("index.html")
    webbrowser.open(Path("index.html").resolve().as_uri())

if __name__ == '__main__':
    main()