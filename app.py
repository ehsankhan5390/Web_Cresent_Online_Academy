import gradio as gr
from controller import app as fastapi_app
import spaces

# ZeroGPU کو مطمئن رکھنے کے لیے ڈمی جی پی یو فنکشن
@spaces.GPU
def check_gpu():
    return "GPU Active"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Web Crescent Online Academy")

# FastAPI App کو Gradio پر ماؤنٹ کرنا
app = gr.mount_gradio_app(fastapi_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)