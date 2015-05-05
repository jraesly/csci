import fiona
from shapely.geometry import shape
preflood = fiona.open("/home/john/Downloads/CSCI4830/project/StreamChannel/StreamChannel.shp")
postflood = fiona.open("/home/john/Downloads/CSCI4830/project/StreamChannelPostFlood/StreamChannelPostFlood.shp")


[not shape(i['geometry']).difference(shape(j['geometry'])).is_empty for i, j in zip(list(preflood), list(postflood))]
[False, False, False, True]

for geom in [shape(i['geometry']).difference(shape(j['geometry'])) for i, j in zip(list(preflood), list(postflood))]:
    print geom



[not shape(i['geometry']).difference(shape(j['geometry'])).is_empty for i, j in zip(list(postflood), list(preflood))]
[True, False, False, False]

for geom in [shape(i['geometry']).difference(shape(j['geometry'])) for i, j in zip(list(postflood), list(preflood))]:
    print geom


from shapely.geometry import mapping
schema = {
    'geometry': 'Polygon',
    'properties': {
        'test': 'int'
    }
}
with fiona.open('diff.shp', 'w', 'ESRI Shapefile', schema) as e:
	for geom  in [shape(i['geometry']).difference(shape(j['geometry'])) for i, j in zip(list(preflood),list(postflood)]:
        if not geom.is_empty:
        e.write({'geometry': mapping(geom),'properties':{'test': 1}})
        for geom in [shape(i['geometry']).difference(shape(j['geometry'])) for i, j in zip(list(postflood), list(preflood))]:
        if not geom.is_empty:
        e.write({'geometry': mapping(geom),'properties': {'test': 2}})
