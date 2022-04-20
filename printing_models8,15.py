from MinaGrejer import printer_goes_brr

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printer_goes_brr.print_models(unprinted_designs[:], completed_models)
printer_goes_brr.show_completed_models(completed_models)