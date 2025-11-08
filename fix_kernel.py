import json

kernel_file = "/trinity/home/hasaan.maqsood/.local/share/jupyter/kernels/transformers_cv_env/kernel.json"

data = {
    "argv": [
        "/trinity/home/hasaan.maqsood/Transformers_Computer-Vision/env/bin/python",
        "-m",
        "ipykernel_launcher",
        "-f",
        "{connection_file}"
    ],
    "display_name": "Python (Transformers_CV)",
    "language": "python",
    "metadata": {
        "debugger": True
    }
}

with open(kernel_file, "w") as f:
    json.dump(data, f, indent=4)
