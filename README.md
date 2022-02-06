# pltpublish

This project on [PyPi](https://pypi.org/project/pltpublish/)|[GitHub](https://github.com/Theomat/pltpublish).

Utility package that takes care of configuring Matplotlib for publication-ready figures!


## Easy to use

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

## All Features

- `setup` calls all `setup_*` methods
- `setup_colorblind` configures matplotlib to use a colorblind palette
- `setup_latex_fonts` configures matplotlib to use LaTeX fonts
- `save_fig` acts like `pyplot.savefig` but guarantees a minimum dpi, that the grid is on and removes outer white space
- `extract_legend_as_figure` extracts the legend of your figure and plots it on another new figure
- `layout_for_subplots` finds automatically a good layout given the number of plots you have to plot on the same figure
