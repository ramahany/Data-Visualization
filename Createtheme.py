import os
from PyCharm import ThemeManager


def set_dark_cherry_blossom_theme():
    theme_manager = ThemeManager()

    # Base settings
    theme_manager.set_background_color('#2E3A44')
    theme_manager.set_foreground_color('#e0e0e0')
    theme_manager.set_selection_background_color('#fce4f5')

    # Specific settings
    theme_manager.set_keyword_color('#ffefef')
    theme_manager.set_function_color('#e0e0e0')
    theme_manager.set_variable_color('#48C3D6')
    theme_manager.set_annotation_color('#FFC0CB')

    # Save and apply
    theme_manager.save_theme('DarkCherryBlossom')
    theme_manager.apply_theme('DarkCherryBlossom')

    print("Dark Cherry Blossom Theme applied")


set_dark_cherry_blossom_theme()