import math
import sys
from typing import Any, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt


def setup() -> None:
    """
    Call all 'setup_*' methods.
    """
    setup_colorblind()
    setup_latex_fonts()


def setup_colorblind() -> None:
    """
    Change the color palette used to the 'seaborn-colorblind' palette.
    """
    availables = plt.style.available
    colorblinds = [x for x in availables if "colorblind" in x]
    if len(colorblinds) == 0:
        print(
            "pltpublish: could nto find any colorblind style installed!",
            file=sys.stderr,
        )
    else:
        seaborn_like = [x for x in colorblinds if "seaborn" in x]
        if seaborn_like:
            style = seaborn_like.pop(0)
        else:
            style = colorblinds.pop(0)
    plt.style.use(style)


def setup_latex_fonts() -> None:
    """
    Change the default font and the mathtext font and thei size to match those of LaTeX.
    More precisely, uses Bitstream Vera Sans as mathtext and STIXGeneral as general font family.
    """
    matplotlib.rcParams.update({"font.size": 14})
    matplotlib.rcParams["mathtext.fontset"] = "custom"
    matplotlib.rcParams["mathtext.rm"] = "Bitstream Vera Sans"
    matplotlib.rcParams["mathtext.it"] = "Bitstream Vera Sans:italic"
    matplotlib.rcParams["mathtext.bf"] = "Bitstream Vera Sans:bold"
    matplotlib.rcParams["mathtext.fontset"] = "cm"
    matplotlib.rcParams["font.family"] = "STIXGeneral"


def set_size_pixels(width: Optional[int] = None, height: Optional[int] = None) -> None:
    """
    Only works if NOT in a notebook and a figure has already been created.
    """
    fig = plt.gcf()
    current_dpi = fig.dpi
    dw = width or fig.get_figwidth() * current_dpi
    dh = height or fig.get_figheight() * current_dpi
    fig.set_size_inches(dw / current_dpi, dh / current_dpi)


def save_fig(file: str, scale: float = 1, **kwargs: Any) -> None:
    """
    Save a figure to file but ensure that:
    - the grid is shown
    - the figure is compact, that is there is no white space around the figure

    Offer scale parameter to scale up or down the figure before saving, note that this is approximate as this is before removing white space.

    Additional arguments are passed to pyplot.save_fig.
    """
    plt.grid(True)
    if "bbox_inches" not in kwargs:
        kwargs["bbox_inches"] = "tight"
    fig = plt.gcf()
    current_dpi = fig.dpi
    kwargs["dpi"] = kwargs.get("dpi", current_dpi) * scale
    plt.savefig(file, **kwargs)


def extract_legend_as_figure(figure: Any, ncol: int = 1) -> matplotlib.figure.Figure:  # type: ignore
    """
    Extract the legend of the given figure object and plot it on antoher new figure that is returned.
    **figure** may not necesserarily may be a Figure object, it should support the majority objects that have a legend.
    **ncol** is the number of columns to use for the legend.
    """
    figlegend = plt.figure()

    if hasattr(figure, "axes"):
        patches, labels = figure.axes[0, 0].get_legend_handles_labels()
    elif hasattr(figure, "get_legend_handles_labels"):
        patches, labels = figure.get_legend_handles_labels()
    figlegend.legend(handles=patches, labels=labels, ncol=ncol)
    return figlegend


def layout_for_subplots(nplots: int, screen_ratio: float = 16 / 9) -> Tuple[int, int]:
    """
    Find a good number of rows and columns for organizing the specified number of subplots.

    Parameters
    -----------
    - **nplots**: the number of subplots
    - **screen_ratio**: the ratio width/height of the screen

    Return
    -----------
    [nrows, ncols] for the sublopt layout.
    It is guaranteed that ```nplots <= nrows * ncols```.
    """
    nrows = int(math.floor(math.sqrt(nplots / screen_ratio)))
    ncols = int(math.floor(nrows * screen_ratio))
    # Increase size so that everything can fit
    while nrows * ncols < nplots:
        if nrows < ncols:
            nrows += 1
        elif ncols < nrows:
            ncols += 1
        else:
            if screen_ratio >= 1:
                ncols += 1
            else:
                nrows += 1
    # If we can reduce the space, reduce it
    while (nrows - 1) * ncols >= nplots and (ncols - 1) * nrows >= nplots:
        if nrows > ncols:
            nrows -= 1
        elif nrows < ncols:
            ncols -= 1
        else:
            if screen_ratio < 1:
                ncols -= 1
            else:
                nrows -= 1
    while (nrows - 1) * ncols >= nplots:
        nrows -= 1
    while (ncols - 1) * nrows >= nplots:
        ncols -= 1
    return nrows, ncols


__all__ = [
    "extract_legend_as_figure",
    "save_fig",
    "setup",
    "setup_colorblind",
    "setup_latex_fonts",
    "set_size_pixels",
    "layout_for_subplots",
]
