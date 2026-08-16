"""
generate.py — Minimal Stable Diffusion XL image generator.

This is the "whole program" — read it top to bottom before the demo.
Designed for an RTX 4080 (16GB VRAM).

Usage:
    python generate.py "a corgi wearing a graduation cap, oil painting style"
"""

import sys
import torch
from diffusers import StableDiffusionXLPipeline

MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"


def load_pipeline():
    """Download (first run only) and load the model onto the GPU."""
    pipe = StableDiffusionXLPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
    )
    pipe = pipe.to("cuda")
    # Saves VRAM with a small speed tradeoff — good safety margin on 16GB.
    pipe.enable_model_cpu_offload()
    return pipe


def generate_image(pipe, prompt, negative_prompt="", steps=30, guidance_scale=7.0, seed=None):
    """Run the diffusion process and return a PIL image."""
    generator = None
    if seed is not None:
        generator = torch.Generator(device="cuda").manual_seed(seed)

    result = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,
        guidance_scale=guidance_scale,
        generator=generator,
    )
    return result.images[0]


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or "a corgi wearing a graduation cap, oil painting style"

    print(f"Loading model ({MODEL_ID})... this can take a minute on first run.")
    pipe = load_pipeline()

    print(f"Generating: {prompt!r}")
    image = generate_image(pipe, prompt)

    output_path = "output.png"
    image.save(output_path)
    print(f"Saved to {output_path}")
