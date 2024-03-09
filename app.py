import requests
import json
import gradio as gr

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)

    data={
        "model":"AIguru",
        "prompt":final_prompt,
        "stream":False
    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)


# interface=gr.Interface(
#     fn=generate_response,
#     inputs=gr.Textbox(lines=4,placeholder="Enter your Prompt"),
#     outputs="text"
# )
# interface.launch()


interface_html = """
<div style="font-family: Arial, sans-serif; max-width: 500px; margin: auto;">
    <h2 style="text-align: center; color: #333;">Interactive Response Generator</h2>
    <p style="text-align: center; color: #666;">Enter your prompt below:</p>
    <textarea id="input-text" style="width: 100%; height: 100px; padding: 10px; box-sizing: border-box; border: 1px solid #ccc;"></textarea>
    <button onclick="generateResponse()" style="display: block; margin: 20px auto; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;">Generate Response</button>
    <p id="output-text" style="color: #333;"></p>
</div>

<script>
    function generateResponse() {
        var inputText = document.getElementById("input-text").value;
        var outputText = document.getElementById("output-text");
        // Call the Python function with the input text
        outputText.innerHTML = gr.Interface.send(inputText);
    }
</script>
"""

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label=None),
    outputs=gr.Textbox(label=None),
    title="AI code generator"
 

)

interface.launch()

