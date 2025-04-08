from praisonaiagents import Agent, MCP
import gradio as gr 

def search_bnb(query):
    agent = Agent(
        instructions="""You help book apartments on Airbnb.""",
        llm="groq/llama-3.2-90b-vision-preview",
        tools=MCP("npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
    )
    result = agent.start(query)
    return f"Airbnb search results\n\n {result}"

demo = gr.Interface(
    fn=search_bnb,
    inputs=gr.Textbox(placeholder="I want to book an apartment in paris for 2 nights."),
    outputs=gr.Markdown(),
    title="AIRBNB Bookings AI",
    description="Enter your booking requirements below:"
)

if __name__=="__main__":
    demo.launch(share=True)
