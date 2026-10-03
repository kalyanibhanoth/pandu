import streamlit as st
import torch 
from diffusers import StableDiffusionPipeline

st.set_page_config(page_title = "AI Image generator", page_icon = "")
st.title("AI Image Generator")
@st.cache_resource
def load_resource():
    pipe = StableDiffusionPipeline.from_pretrained("segmind/tiny-sd",torch_dtype=torch.float32)
    return pipe
pipe = load_resource()
st.caption("Model loaded!")
st.session_state.setdefault("generated_image",None)
st.session_state.setdefault("generated_prompt",None)
prompt = st.text_input("enter a prompt", placeholder = "a cat working sunglasses")
generate = st.button("generate")
if prompt and generate:
    with st.spinner("generating image... This might take a while."):
        image = pipe(prompt, num_inference_steps = 8).images[0]
    st.session_state.generated_image = image
    st.session_state.generated_prompt = prompt

if st.session_state.generated_image is not None:
    st.image(st.session_state.generated_image, caption = st.session_state.generated_prompt) 