import ipywidgets as widgets

prueba = widgets.ToggleButton(
    value=False,
    description='Iniciar prueba',
    button_style='success',
    tooltip='prueba de instalacion',
    icon='rocket'
)

output = widgets.Output()

display(prueba, output)

def on_value_change(change):
    with output:
        if change['new'] == True:
            print("Prueba iniciada")
        else:   
            print("Prueba detenida")

prueba.observe(on_value_change, names='value')