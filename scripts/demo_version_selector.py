"""
This is a demo extension demonstrate a method of enabling or disabling scripts.Script

The concept is simple you create a setting entry that allows the user to select the scripts / module that they wish to use
then fetch the module class and store it under a global variable of this file

To be a scripts.Script loaded by webui, it simply needs to store in a global variable in any python script under <extensions>/<extensions_name>/scripts/<your_python_script>.py
Other class such as Script scripts_postprocessing.ScriptPostprocessing can also be loaded in this fashion

This is simply a concept demo script, you don't have to structure extensions in the same way, other methods can achieve similar effect
"""

from multi_version_extension_demo_modules import single_modules, multi_modules
from modules import shared, ui_components
import gradio as gr

shared.options_templates.update(shared.options_section(('demo-version-selector', "Demo extension version selector"), {
    "demo_selected_version": shared.OptionInfo(
        'v1', 'Demo selected module (single)', gr.Dropdown,
        {'choices': list(single_modules)}).needs_restart(),
    "demo_selected_version_m": shared.OptionInfo(
        ['v1'], 'Demo enable modules (multi)', ui_components.DropdownMulti,
        {'choices': list(multi_modules)}).needs_restart(),
}))

# single module
single_selected_module = single_modules.get(shared.opts.demo_selected_version)

# multiple modules
for index, selected_version in enumerate(shared.opts.demo_selected_version_m):
    globals()[f'script_{index}'] = multi_modules.get(selected_version)
