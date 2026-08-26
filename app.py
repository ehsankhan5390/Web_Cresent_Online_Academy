import gradio as gr
from controller import app

# Mount FastAPI app inside Gradio for Hugging Face Spaces compatibility
demo = gr.mount_gradio_app(app, gr.Blocks(), path="/")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)