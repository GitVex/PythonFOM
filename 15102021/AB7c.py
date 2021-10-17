band = ['Richie Kotzen (Gitarre,Gesang)', 'Billy Sheehan (Bass)', 'Mike Portnoy (Schlagzeug)']

# -=-=-=-=-=-=-= Nr.1 -=-=-=-=-=-=-=
band.sort(key=lambda x: x.split(' ')[1])

# -=-=-=-=-=-=-= Nr.2 -=-=-=-=-=-=-=
album_name = 'The Winery Dogs', 'Hot Streak', 'Dog Years (EP)'
album_jahr = 2013, 2015, 2017

album_dict = dict(zip(album_name, album_jahr))
# for i, x in enumerate(album_dict):
#    print("Album", str(i+1) + ")", x, "(" + str(album_dict[x]) + ")")

# -=-=-=-=-=-=-= Nr.3 -=-=-=-=-=-=-=
album_tuple = list(zip(album_name, album_jahr))
# print(album_tuple)

# -=-=-=-=-=-=-= Nr.4 -=-=-=-=-=-=-=
band_vornamen = tuple([x.split(" ")[0] for x in band])
band_nachnamen = tuple([x.split(" ")[1] for x in band])
band_instrumente = tuple([x.split(" ")[2][1:len(x.split(" ")[2]) - 1] for x in band])

# print(band_vornamen, band_nachnamen, band_instrumente)

# -=-=-=-=-=-=-= Nr.6 -=-=-=-=-=-=-=
try:
    if band_instrumente.index(" "):
        print("Leere Elemente vorhanden")

except ValueError:
    print("Keine leeren Elemente vorhanden")
