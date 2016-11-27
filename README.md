# General course assignment

Build a map-based application, which lets the user see geo-based data on a map and filter/search through it in a meaningfull way. Specify the details and build it in your language of choice. The application should have 3 components:

1. Custom-styled background map, ideally built with [mapbox](http://mapbox.com). Hard-core mode: you can also serve the map tiles yourself using [mapnik](http://mapnik.org/) or similar tool.
2. Local server with [PostGIS](http://postgis.net/) and an API layer that exposes data in a [geojson format](http://geojson.org/).
3. The user-facing application (web, android, ios, your choice..) which calls the API and lets the user see and navigate in the map and shows the geodata. You can (and should) use existing components, such as the Mapbox SDK, or [Leaflet](http://leafletjs.com/).

## Example projects

- Showing nearby landmarks as colored circles, each type of landmark has different circle color and the more interesting the landmark is, the bigger the circle. Landmarks are sorted in a sidebar by distance to the user. It is possible to filter only certain landmark types (e.g., castles).

- Showing bicykle roads on a map. The roads are color-coded based on the road difficulty. The user can see various lists which help her choose an appropriate road, e.g. roads that cross a river, roads that are nearby lakes, roads that pass through multiple countries, etc.

## Data sources

- [Open Street Maps](https://www.openstreetmap.org/)
- [Geofabric](http://download.geofabrik.de/)

## My project

Fork this repository and fill in:

**Application description**: `Application show you gas stations in Slovak Republic. You can choose what you want to see. It is possible to find all gas stations or selected type of gas stations, for example: Slovnaft, OMV, LPG, etc. 
You can also mark your position on map and the application will show you 10 nearest gas stations. There are also possibility to select prefered type of station or biggest distance, which could be between you and station. You can also see a legend with description of colors of markers shown in the map. When you click on the each marker, the type of gas station and distance between you in kilometers will be showen.`

**Data source**: `openstreetmap, geofabric`

**Technologies used**: `python, javascritp, postgis, postresql`
