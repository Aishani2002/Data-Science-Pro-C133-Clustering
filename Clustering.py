import csv
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])
headers[0] = "row_num"

temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
  if star_data[1].lower() == "hd 100546 b":
    star_data_rows.remove(star_data)

star_masses = []
star_radiuses = []
star_names = []
for star_data in star_data_rows:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[4])
  star_names.append(star_data[1])
star_gravity = []
for index, name in enumerate(star_names):
  gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000) * 6.674e-11
  star_gravity.append(gravity)

fig = px.scatter(x=star_radiuses, y=star_masses, size=star_gravity, hover_data=[star_names])
fig.show()

low_gravity_stars = []
for index, gravity in enumerate(star_gravity):
  if gravity < 10:
    low_gravity_stars.append(star_data_rows[index])

print(len(low_gravity_stars))

star_type_values = []

star_masses = []
star_radiuses = []
for star_data in low_gravity_stars:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[4])

fig = px.scatter(x =star_radiuses, y=star_masses)
fig.show()


x = []
for index, star_mass in enumerate(star_masses):
  tempList = [
            star_radiuses[index],
            star_mass
  ]
  x.append(tempList)

wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss, marker="o", color="yellow")
plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

star_masses = []
star_radiuses = []
star_type = []

for star_data in low_gravity_stars:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[4])

fig = px.scatter(x=star_radiuses, y=star_masses, color=star_type)
fig.show()