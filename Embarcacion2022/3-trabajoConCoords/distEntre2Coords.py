import geopy.distance

coords_1 = (6.1495, -74.6369)
coords_2 = (6.5239, -74.6369)

print(geopy.distance.geodesic(coords_1, coords_2).km)