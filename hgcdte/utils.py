import yaml
from importlib import resources

def load_material_model(name: str) -> dict:
    """
    Load a material model YAML file from hgcdte/material_sets/.
    Returns a dictionary of coefficients and metadata.
    """
    filename = f"{name}.yaml"

    with resources.files("hgcdte.material_sets").joinpath(filename).open("r") as f:
        return yaml.safe_load(f)
