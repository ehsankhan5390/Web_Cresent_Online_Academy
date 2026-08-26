import gradio as gr
from controller import app as fastapi_app

# Create a Gradio interface shell
with gr.Blocks() as demo:
    gr.Markdown("# Web Crescent Online Academy Running...")

# Mount FastAPI inside Gradio
app = gr.mount_gradio_app(fastapi_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)