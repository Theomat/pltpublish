# pltpublish

This project on [PyPi](https://pypi.org/project/pltpublish/)|[GitHub](https://github.com/Theomat/pltpublish).

Utility package that takes care of configuring Matplotlib for publication-ready figures!

```bash
pip install pltpublish
```

**Before**                            **After**

```python
                                                  > import pltpublish as pub
                                                  > pub.setup()
# your plot code using plt                        > # your plot code using plt
plt.savefig("my_fig.eps")                         > pub.save_fig("my_fig.eps")
```

|**Without `pltpublish`**|**With `pltpublish`**|
|-|-|
| <img src="https://github.com/Theomat/pltpublish/raw/main/examples/images/classic.png" width="400" height="300">|<img src="https://github.com/Theomat/pltpublish/raw/main/examples/images/pltpublish.png" width="400" height="300"> |

## Recommendation

If you are using LaTeX then perhaps [TikzPlotLib](https://github.com/nschloe/tikzplotlib) will be highly relevant.

## All Features

- `setup` calls all `setup_*` methods
- `setup_colorblind` configures matplotlib to use a colorblind palette
- `setup_latex_fonts` configures matplotlib to use LaTeX fonts
- `set_size_pixels` enables to set the size of an existing figure in pixels
- `save_fig` acts like `pyplot.savefig` but guarantees that the grid is on and removes outer white space and also enables to scale up or down the figure before saving
- `extract_legend_as_figure` extracts the legend of your figure and plots it on another new figure
- `layout_for_subplots` finds automatically a good layout given the number of plots you have to plot on the same figure
- `get_color_cycle` gets you the current default color cycle
- `set_color_cycle` sets the current default color cycle
