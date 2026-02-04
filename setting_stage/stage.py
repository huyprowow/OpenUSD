from pxr import Usd, Sdf
import os

# Create a new stage:
stage: Usd.Stage = Usd.Stage.CreateNew("_assets/root_layer_example.usda")

# Get the root layer object:
root_layer: Sdf.Layer = stage.GetRootLayer()
# Use relpath to avoid printing build machine filesystem info.
print("Root layer identifier:", os.path.relpath(root_layer.identifier))

# Add a simple prim so the stage is not empty:
stage.DefinePrim("/World", "Xform")

# Create an additional layer (in a different format) and add it as a sublayer:
extra_layer: Sdf.Layer = Sdf.Layer.CreateNew("_assets/extra_layer.usdc")
# Anchor the path relative to the root layer for better portability
rel_path = "./" + os.path.basename(extra_layer.identifier)
root_layer.subLayerPaths.append(rel_path)

# Save both layers:
stage.Save()
extra_layer.Save()

# Print the contents of the root layer:
print("Root layer contents:")
print(root_layer.ExportToString())