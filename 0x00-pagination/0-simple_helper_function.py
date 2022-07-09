#!/usr/bin/env python3
"""Defines the function index_range."""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing start index and an end index."""
    end = page_size * page
    start = end - page_size
    return (start, end)
