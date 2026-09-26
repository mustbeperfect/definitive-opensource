def slugify(name: str) -> str:
    """Generate a markdown anchor-friendly slug from a heading or section name."""
    return name.lower().replace(" ", "-").replace("(", "").replace(")", "")


def sanitize_table_cell(text: str | None) -> str:
    """Sanitize string for inclusion in markdown table cells by replacing pipe delimiters."""
    if not text:
        return ""
    return text.replace("|", "-").strip()


def format_stars(stars: int | None, compact: bool = True) -> str:
    """Format star count for markdown display.

    If compact is True (default for main READMEs), formats large numbers with 'k' or 'M'
    (e.g., 1500 -> '1.5k', 1000000 -> '1M', None -> '').
    If compact is False (used for backlog tables), formats with commas (e.g., 1500 -> '1,500', None -> '0').
    """
    if stars is None:
        return "" if compact else "0"
    if not compact:
        return f"{stars:,}"
    if stars >= 1_000_000:
        formatted = f"{stars / 1_000_000:.1f}M"
        return formatted.replace(".0M", "M")
    elif stars >= 1_000:
        formatted = f"{stars / 1_000:.1f}k"
        return formatted.replace(".0k", "k")
    else:
        return str(stars)
