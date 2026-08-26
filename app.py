import gradio as gr
from controller import app

# FastAPI ایپ کو Gradio کے ساتھ جوڑنا
demo = gr.mount_gradio_app(app, gr.Blocks(), path="/")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)