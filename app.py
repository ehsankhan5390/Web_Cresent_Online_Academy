import gradio as gr
from controller import app as fastapi_app

# ZeroGPU کو سیف طریقے سے ہینڈل کرنا (Local PC اور Hugging Face دونوں کے لیے)
try:
    import spaces
    @spaces.GPU
    def gpu_keepalive(text="init"):
        return f"GPU Active: {text}"
except ImportError:
    # اگر local pc پر spaces نہ ملے تو یہ سمپل فنکشن چلے گا
    def gpu_keepalive(text="init"):
        return f"Local Mode Active: {text}"

# Startup check
try:
    gpu_keepalive("startup_check")
except Exception:
    pass

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Web Crescent Online Academy")
    txt_input = gr.Textbox(value="Init", visible=False)
    txt_output = gr.Textbox(visible=False)
    btn = gr.Button("Run", visible=False)
    btn.click(fn=gpu_keepalive, inputs=txt_input, outputs=txt_output)

# FastAPI App کو Mount کرنا
app = gr.mount_gradio_app(fastapi_app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)