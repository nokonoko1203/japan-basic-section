# japan-basic-section

国土基本図図郭に沿ったgeopandas.GeoDataFrameを作成するためのシンプルなPythonパッケージです。
図郭のレベルは50000, 5000, 2500, 1000, 500から選択できます。

## インストール

```bash
pip install japan-basic-section
```

## 使い方

※ 詳細はnotebooks/sample.ipynbを参照してください。

```python
from japan_basic_section.grid import Grid
from japan_basic_section.origin_coords import get_coord_info


g = Grid(system_number, 50000)
grid_50000 = g.make_grid()

crs = info[1]["JGD2011"]
grid_50000.set_crs(crs, inplace=True)

os.makedirs("../data/output", exist_ok=True)
grid_50000.to_file("../data/output/grid_50000.fgb", driver="FlatGeobuf")
```
