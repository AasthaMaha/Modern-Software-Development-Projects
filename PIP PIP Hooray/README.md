# Interactive Rotating Globe with Population Density

## Purpose

> The goal of this script was to create an interactive rotating globe that visualizes
> population density using a log scale, using python. As well as allowing the users
> to interact with the globe by rotating and zooming in on different regions.
> Additionally, it includes geospatial data manipulation using the gepandas
> and teaches how to integrate and visualize the data using Plotly, a very useful for
> creating interactive visualizations.

> In this project, we also did dependency management within the virtual python
> environment, practicing tracking and installing only the necessary packages
> with tools like pip and pipreqs.

## Steps Followed

1. **Set up the project virtual environment**
2. **Installed the Packages**
3. **Generated the full list of installed dependencies using `pip freeze` and saved it to `all_requirements.txt`.
   Then refined that list.**
4. **Reinstalled the required packages and verified that the project works as expected.**
5. **Analyzed the project dependencies and save it the dependency tree to `dependency_tree.txt`. Then ran the globe.py
   file.**

## Output of pipdeptree

### Dependency Tree

```txt
geopandas==1.0.1
  ├── numpy==1.26.4
  ├── packaging==24.2
  ├── pandas==2.2.3
  │    ├── numpy==1.26.4
  │    ├── python-dateutil==2.9.0.post0
  │    │    └── six==1.17.0
  │    ├── pytz==2025.1
  │    └── tzdata==2025.1
  ├── pyogrio==0.10.0
  │    ├── certifi==2025.1.31
  │    ├── numpy==1.26.4
  │    └── packaging==24.2
  ├── pyproj==3.6.1
  │    └── certifi==2025.1.31
  └── shapely==2.0.7
       └── numpy==1.26.4
pipdeptree==2.25.0
  ├── packaging==24.2
  └── pip==25.0.1
...
```

## Observations or issues:

> I had issue with activating the virtual envrionment and with the installating
> of the packages. But figure out the problem had to with my settings which I changed,
> and everything was working fine again. 
