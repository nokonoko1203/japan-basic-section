import geopandas as gpd
from shapely.geometry import Polygon

from .origin_coords import OriginCoords, SystemNumber


class BaseSection:
    def __init__(self, number: int) -> None:
        self.number = number
        self.system_name: str = SystemNumber(number).name
        self.origin = OriginCoords[self.system_name].value
        self.bbox = [-160000, -300000, 160000, 300000]
        self.top_left = (self.bbox[0], self.bbox[3])
        self.x_grid = 8
        self.y_grid = 20
        self.grid_size = self._get_grid_size()
        self.grid = self._get_grid()

    def _get_grid_size(self) -> tuple[float, float]:
        return (
            (self.bbox[2] - self.bbox[0]) / self.x_grid,
            (self.bbox[3] - self.bbox[1]) / self.y_grid,
        )

    def _get_grid(self) -> gpd.GeoDataFrame:
        grid = []
        for j in range(self.y_grid):
            for i in range(self.x_grid):
                prefix = str(self.number).zfill(2)
                index = prefix + chr(ord("A") + j) + chr(ord("A") + i)
                grid.append(
                    {
                        "index": index,
                        "polygon": [
                            (self.top_left[0] + self.grid_size[0] * i, self.top_left[1] - self.grid_size[1] * j),
                            (self.top_left[0] + self.grid_size[0] * (i + 1), self.top_left[1] - self.grid_size[1] * j),
                            (
                                self.top_left[0] + self.grid_size[0] * (i + 1),
                                self.top_left[1] - self.grid_size[1] * (j + 1),
                            ),
                            (
                                self.top_left[0] + self.grid_size[0] * i,
                                self.top_left[1] - self.grid_size[1] * (j + 1),
                            ),
                        ],
                    }
                )

        indexes = [g["index"] for g in grid]
        geometries = [Polygon(g["polygon"]) for g in grid]
        gdf = gpd.GeoDataFrame(index=indexes, geometry=geometries)  # type: ignore
        return gdf
