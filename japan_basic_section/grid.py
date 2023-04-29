import geopandas as gpd
from shapely.geometry import Polygon

from .base_section import BaseSection


class Grid:
    def __init__(self, system_number: int, level: int = 50000) -> None:
        self.system_number = system_number
        self.level_list = [50000, 5000, 2500, 1000, 500]

        if level not in self.level_list:
            raise ValueError(f"level must be one of {self.level_list}")

        self.level = level
        self.base = BaseSection(self.system_number)

    def _get_grid_size(self, level: int) -> tuple[int, int]:
        if level == 5000:
            return (10, 10)
        if level == 2500:
            return (2, 2)
        if level == 1000:
            return (5, 5)
        return (10, 10)

    def _make_number_name(self, index: str, j: int, i: int, level: int) -> str:
        if level == 5000:
            return f"{index}{j}{i}"

        if level == 2500:
            if (j, i) == (0, 0):
                return f"{index}1"
            if (j, i) == (0, 1):
                return f"{index}2"
            if (j, i) == (1, 0):
                return f"{index}3"
            if (j, i) == (1, 1):
                return f"{index}4"

        if level == 1000:
            return f"{index}{j}{chr(ord('A') + i)}"

        return f"{index}{j}{i}"

    def _make_geo_dataframe(self, base_grid: gpd.GeoDataFrame, level: int):
        grid = []

        x_grid, y_grid = self._get_grid_size(level)

        for index, row in base_grid.iterrows():
            polygon = row.geometry
            x_min, y_min, x_max, y_max = polygon.bounds

            x_size = (x_max - x_min) / x_grid
            y_size = (y_max - y_min) / y_grid

            top_left = (x_min, y_max)

            for j in range(y_grid):
                for i in range(x_grid):
                    number = self._make_number_name(index, j, i, level)
                    grid.append(
                        {
                            "index": number,
                            "polygon": [
                                (top_left[0] + x_size * i, top_left[1] - y_size * j),
                                (top_left[0] + x_size * (i + 1), top_left[1] - y_size * j),
                                (top_left[0] + x_size * (i + 1), top_left[1] - y_size * (j + 1)),
                                (top_left[0] + x_size * i, top_left[1] - y_size * (j + 1)),
                            ],
                        }
                    )

        indexes = [g["index"] for g in grid]
        geometries = [Polygon(g["polygon"]) for g in grid]
        return gpd.GeoDataFrame(index=indexes, geometry=geometries)  # type: ignore

    def make_grid(self) -> gpd.GeoDataFrame:
        if self.level == 50000:
            return self.base.grid

        # 1/5000以下は全て1/5000をベースに分割されるため、ベースとなるグリッドを作成
        base_grid = self._make_geo_dataframe(self.base.grid, 5000)
        if self.level == 5000:
            return base_grid

        grid = self._make_geo_dataframe(base_grid, self.level)
        return grid
