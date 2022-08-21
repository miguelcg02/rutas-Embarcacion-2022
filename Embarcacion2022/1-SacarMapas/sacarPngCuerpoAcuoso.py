import osmnx as ox
import matplotlib.pyplot as plt

tags = {'water': 'river'}
agua = ox.geometries_from_bbox(6.5053,6.1673,-74.3321,-74.6046, tags)

with open('berrio-nare.geojson', 'w') as f:
    f.write(agua.to_json())

print("3")

print(len(agua))
print("4")

fig, ax = plt.subplots(figsize=(12,8))
print("5")

# Plot Agua
agua.plot(ax=ax, facecolor='blue', alpha=0.7)
print("6")

plt.tight_layout()
print("7")

plt.show()
print("8")