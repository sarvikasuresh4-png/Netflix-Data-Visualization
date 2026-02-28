import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("BestMoviesNetflix.csv")

# Genre distribution
data["MAIN_GENRE"].value_counts().plot(kind="bar")
plt.title("Genre Distribution")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# Production country
data["MAIN_PRODUCTION"].value_counts().plot(kind="bar")
plt.title("Production Country Distribution")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()
