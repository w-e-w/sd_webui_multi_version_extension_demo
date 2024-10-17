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
